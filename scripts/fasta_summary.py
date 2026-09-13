import sys


def read_fasta(path):
    records = {}
    current_id = None

    with open(path) as fasta:
        for raw_line in fasta:
            line = raw_line.strip()

            if not line:
                continue

            if line.startswith(">"):
                current_id = line[1:]
                records[current_id] = ""
            else:
                records[current_id] += line.upper()
    return records


def gc_percent(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    return 100 * gc_count / len(sequence)


if len(sys.argv) != 2:
    print("Usage: python scripts/fasta_summary.py <fasta-file>")
    sys.exit(1)

records = read_fasta(sys.argv[1])

print("sequence_id\tlength\tgc_percent")

for sequence_id, sequence in records.items():
    allowed_bases = set("ACGTN")
    invalid_bases = set(sequence) - allowed_bases
    if invalid_bases:
        print(f"Invalid bases found in sequence {sequence_id}: {', '.join(invalid_bases)}", file=sys.stderr)
        sys.exit(1)
    print(
    f"{sequence_id}\t{len(sequence)}\t{gc_percent(sequence):.2f}"
)

