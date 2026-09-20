def calculate_gc(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    gc_percent = (gc_count / len(sequence)) * 100
    return gc_percent   

input_file = "data/sample_sequences.tsv"

with open(input_file) as file:
    header = next(file)
    print("sample_id\tsequence\tgc_percent")

    for line in file:
        cleaned_line = line.strip()
        sample_id, sequence = cleaned_line.split("\t")
        gc_percent = calculate_gc(sequence)
        print(f"{sample_id}\t{sequence}\t{gc_percent:.2f}")

