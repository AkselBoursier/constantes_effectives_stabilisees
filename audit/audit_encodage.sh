#!/usr/bin/env bash
# audit_encodage.sh
# Verifie l'encodage UTF-8 des fichiers Markdown et detecte les titres dupliques.
#
# Controles effectues :
#   1. Fichiers Markdown non valides UTF-8
#   2. Titres de niveau 1 (# ...) dupliques dans le corpus
#   3. Titres de niveau 2 (## ...) dupliques dans un meme fichier
#
# Usage : bash audit/audit_encodage.sh [repertoire]
#   Si aucun repertoire n'est fourni, utilise le repertoire courant.
#
# Dependances standard : iconv, awk, sort, uniq (outils Unix standards)

ROOT="${1:-.}"
ROOT="$(cd "$ROOT" && pwd)"

echo "=== Audit d'encodage et de titres dupliques ==="
echo "Repertoire : $ROOT"
echo "Date       : $(date '+%Y-%m-%d %H:%M')"
echo ""

ENCODING_ERRORS=0
H1_DUPLICATES=0
H2_DUPLICATES=0

# --- 1. Verifier l'encodage UTF-8 ---
echo "1. Verification de l'encodage UTF-8"
echo ""

while IFS= read -r -d '' mdfile; do
    if ! iconv -f utf-8 -t utf-8 "$mdfile" > /dev/null 2>&1; then
        printf "  NON-UTF-8  %s\n" "${mdfile#$ROOT/}"
        ENCODING_ERRORS=$((ENCODING_ERRORS + 1))
    fi
done < <(find "$ROOT" -name "*.md" -not -path "*/.git/*" -print0 | sort -z)

if [ "$ENCODING_ERRORS" -eq 0 ]; then
    echo "  Tous les fichiers Markdown sont en UTF-8 valide."
fi

echo ""

# --- 2. Titres H1 dupliques dans le corpus ---
echo "2. Titres H1 (# ...) dupliques dans le corpus"
echo ""

TMPFILE=$(mktemp)
while IFS= read -r -d '' mdfile; do
    grep -n '^# ' "$mdfile" | while IFS=: read -r lineno title; do
        echo "${title}	${mdfile#$ROOT/}:${lineno}"
    done
done < <(find "$ROOT" -name "*.md" -not -path "*/.git/*" -print0 | sort -z) > "$TMPFILE"

awk -F'\t' '{print $1}' "$TMPFILE" | sort | uniq -d | while read -r dup_title; do
    echo "  DUPLIQUE : $dup_title"
    grep "^${dup_title}	" "$TMPFILE" | awk -F'\t' '{print "    " $2}'
    H1_DUPLICATES=$((H1_DUPLICATES + 1))
done

if [ "$H1_DUPLICATES" -eq 0 ]; then
    echo "  Aucun titre H1 duplique detecte."
fi

rm -f "$TMPFILE"
echo ""

# --- 3. Titres H2 dupliques dans un meme fichier ---
echo "3. Titres H2 (## ...) dupliques dans un meme fichier"
echo ""

H2_DUP_FOUND=0
while IFS= read -r -d '' mdfile; do
    dups=$(grep '^## ' "$mdfile" | sort | uniq -d)
    if [ -n "$dups" ]; then
        printf "  %s\n" "${mdfile#$ROOT/}"
        echo "$dups" | while read -r dup; do
            printf "    DUPLIQUE : %s\n" "$dup"
        done
        H2_DUP_FOUND=$((H2_DUP_FOUND + 1))
    fi
done < <(find "$ROOT" -name "*.md" -not -path "*/.git/*" -print0 | sort -z)

if [ "$H2_DUP_FOUND" -eq 0 ]; then
    echo "  Aucun titre H2 duplique dans un meme fichier."
fi

echo ""
echo "--- Bilan ---"
echo "Fichiers non-UTF-8       : $ENCODING_ERRORS"

ISSUES=$((ENCODING_ERRORS))
if [ "$ISSUES" -gt 0 ]; then
    echo ""
    echo "Action recommandee :"
    echo "  Convertir les fichiers non-UTF-8 en UTF-8 (ex: iconv -f latin1 -t utf-8)."
    exit 1
else
    echo ""
    echo "Aucun probleme d'encodage detecte."
    exit 0
fi
