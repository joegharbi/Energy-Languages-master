#!/bin/bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FASTA_SCRIPT="$ROOT_DIR/fasta.python3-3.py"

echo "Generating input for k-nucleotide benchmark"
python "$FASTA_SCRIPT" 25000000 > "$ROOT_DIR/knucleotide-input25000000.txt"

echo "Generating input for reverse-complement benchmark"
python "$FASTA_SCRIPT" 25000000 > "$ROOT_DIR/revcomp-input25000000.txt"

echo "Generating input for regex-redux benchmark"
python "$FASTA_SCRIPT" 5000000 > "$ROOT_DIR/regexredux-input5000000.txt"
