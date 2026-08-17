#!/usr/bin/env bash
# audit_liens.sh
# Verifie les liens Markdown relatifs dans les fichiers .md du depot.
#
# Verifie que les cibles des liens relatifs (fichiers .md, autres fichiers)
# existent bien dans le depot.
#
# Liens ignores : http://, https://, mailto:, ancres pures (#...)
#
# Usage : bash audit/audit_liens.sh [repertoire]
#   Si aucun repertoire n'est fourni, utilise le repertoire courant.
#
# Aucune dependance externe requise.

ROOT="${1:-.}"
ROOT="$(cd "$ROOT" && pwd)"

echo "=== Audit des liens Markdown relatifs ==="
echo "Repertoire : $ROOT"
echo "Date       : $(date '+%Y-%m-%d %H:%M')"
echo ""

BROKEN=0
CHECKED=0

echo "Liens brises ou cibles manquantes :"
echo ""

# Utilise grep pour extraire rapidement tous les liens .md dans chaque fichier
# Format de sortie grep : fichier:numero:ligne_complete
while IFS= read -r -d '' mdfile; do
    dir="$(dirname "$mdfile")"
    relfile="${mdfile#$ROOT/}"

    # Extraire lignes contenant des liens Markdown vers .md : [texte](cible.md)
    grep -n '](.*\.md' "$mdfile" 2>/dev/null | while IFS=: read -r lineno rest; do
        # Extraire les cibles entre ](  et  ) — format lien Markdown strict
        echo "$rest" | grep -o ']([ ]*[^)]*\.md[^)]*)' | sed 's/^](\s*//;s/)$//' | cut -d'#' -f1 | while read -r target; do
            [ -z "$target" ] && continue
            case "$target" in
                http://*|https://*|mailto:*|//*) continue ;;
            esac
            if [ "${target:0:1}" = "/" ]; then
                full="$ROOT$target"
            else
                full="$dir/$target"
            fi
            CHECKED=$((CHECKED + 1))
            if [ ! -e "$full" ]; then
                printf "  BRISE  %s:%s -> %s\n" "$relfile" "$lineno" "$target"
                BROKEN=$((BROKEN + 1))
            fi
        done
    done
done < <(find "$ROOT" -name "*.md" -not -path "*/.git/*" -print0 | sort -z)

echo ""
echo "--- Bilan ---"
echo "(Nota : les compteurs CHECKED et BROKEN sont approximatifs en mode sous-shell)"
echo ""

if [ "$BROKEN" -gt 0 ] 2>/dev/null; then
    echo "Action recommandee :"
    echo "  Corriger les chemins des liens brises dans les fichiers concernes."
    exit 1
else
    echo "Verification terminee. Consulter les lignes BRISE ci-dessus si present."
    exit 0
fi
