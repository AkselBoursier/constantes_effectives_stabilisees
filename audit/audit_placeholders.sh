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
# Aucune dependance externe requise.

ROOT="${1:-.}"

echo "=== Audit des placeholders d'extraction ==="
echo "Repertoire : $ROOT"
echo "Date       : $(date '+%Y-%m-%d %H:%M')"
echo ""

TOTAL_FILES=0
TOTAL_PLACEHOLDERS=0
FOUND=0

echo "Fichiers avec placeholders :"
echo ""

while IFS= read -r -d '' file; do
    count=$(grep -c '\[  \]\|\[ [A-Za-z_^{}]*=\s*\]\|\[ [A-Za-z_^{}]* \]' "$file" 2>/dev/null || true)
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
    echo "Action recommandee :"
    echo "  Verifier les passages correspondants dans les DOCX originaux."
    echo "  Voir CONVENTION_PLACEHOLDERS.md pour la convention de signalement."
    exit 1
else
    echo "Aucun placeholder detecte."
    exit 0
fi
