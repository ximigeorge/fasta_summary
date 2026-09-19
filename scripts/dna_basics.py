sequences = {
    "sample_1": "ATGCGTAA",
    "sample_2": "GGGGCCCC",
    "sample_3": "ATATATAT",
    "sample_4": "ACGT",
}



def calculate_gc(sequence):
    gc_count = sequence.count("G") + sequence.count("C")
    gc_percent = (gc_count / len(sequence)) * 100
    return gc_percent   

print("sample_id\tsequence\tlength\ta_count\tgc_percent\tclassification")
for sample_id, sequence in sequences.items():
    a_count = sequence.count("A")
    sequence_length = len(sequence)
    
    gc_percent = calculate_gc(sequence)

    if gc_percent >= 50:
        classification = "High GC"
    else:
        classification = "Low GC"
    print(f"{sample_id}\t{sequence}\t{sequence_length}\t{a_count}\t{gc_percent:.2f}\t{classification}")
