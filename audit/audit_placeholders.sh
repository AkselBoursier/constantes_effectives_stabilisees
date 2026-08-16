#!/usr/bin/env bash
# audit_placeholders.sh
# Detecte les placeholders d'extraction dans les fichiers Markdown.
#
# Placeholders cibles :
#   [  ]         passage vide non extrait
#   [ X= ]       formule non rendue (ex: [ M_W= ], [ m_f= ], [ s_{12}= ])
#   [ Lambda ]   symbole non rendu
#
# Usage : bash audit/audit_placeholders.sh [repertoire]
#   Si aucun repertoire n'est fourni, utilise le repertoire courant.
#
# Ce controle est informatif : la presence de placeholders signale une dette
# d'extraction a verifier contre les sources DOCX, pas une invalidite du corpus.
# Une impossibilite technique d'effectuer l'inventaire reste une erreur.
#
# Aucune dependance externe requise.

ROOT="${1:-.}"

if [ ! -d "$ROOT" ]; then
    echo "ERREUR : repertoire introuvable : $ROOT" >&2
    exit 2
fi

echo "=== Inventaire des placeholders d'extraction ==="
echo "Repertoire : $ROOT"
echo "Date       : $(date '+%Y-%m-%d %H:%M')"
echo ""

TOTAL_FILES=0
TOTAL_PLACEHOLDERS=0
FOUND=0

echo "Fichiers avec placeholders :"
echo ""

while IFS= read -r -d '' file; do
    count=$(grep -c '\[  \]\|\[ [A-Za-z_^{}]*=\s*\]\|\[ [A-Za-z_^{}]* \]' "$file" 2>/dev/null)
    grep_status=$?
    if [ "$grep_status" -eq 1 ]; then
        count=0
    elif [ "$grep_status" -ne 0 ]; then
        echo "ERREUR : lecture impossible pendant l'inventaire : ${file#$ROOT/}" >&2
        exit 2
    fi

    if [ "${count:-0}" -gt 0 ] 2>/dev/null; then
        printf "  %4d  %s\n" "$count" "${file#$ROOT/}"
        TOTAL_PLACEHOLDERS=$((TOTAL_PLACEHOLDERS + count))
        FOUND=$((FOUND + 1))
    fi
    TOTAL_FILES=$((TOTAL_FILES + 1))
done < <(find "$ROOT" -name "*.md" -not -path "*/.git/*" -print0 | sort -z)

echo ""
echo "--- Bilan ---"
echo "Fichiers Markdown analyses : $TOTAL_FILES"
echo "Fichiers avec placeholders : $FOUND"
echo "Total de placeholders      : $TOTAL_PLACEHOLDERS"
echo ""

if [ "$TOTAL_PLACEHOLDERS" -gt 0 ]; then
    echo "Inventaire informatif :"
    echo "  Verifier les passages correspondants dans les DOCX originaux selon leur priorite."
    echo "  Voir CONVENTION_PLACEHOLDERS.md pour la convention de signalement."
else
    echo "Aucun placeholder detecte."
fi

exit 0
