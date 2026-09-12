#!/usr/bin/env bash

input_file="$1"

if [[ -z "$input_file" ]]; then
    echo "Usage: bash scripts/fasta_summary.sh <fasta-file>" >&2
    exit 1
fi

if [[ ! -f "$input_file" ]]; then
    echo "Error: file not found: $input_file" >&2
    exit 1
fi

echo -e "sequence_id\tlength\tgc_percent"

awk '
/^>/ {
    id = substr($0, 2)
    next
}

{
    sequence = toupper($0)
    sequence_length = length(sequence)

    gc_sequence = sequence
    gsub(/[^GC]/, "", gc_sequence)

    gc_percent = 100 * length(gc_sequence) / sequence_length

    printf "%s\t%d\t%.2f\n", id, sequence_length, gc_percent
}
' "$input_file"