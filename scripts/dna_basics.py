sequences = [
    "ATGCGTAA",
    "GGGGCCCC",
    "ATATATAT",
    "ACGT"
]



for sequence in sequences:
    a_count = sequence.count("A")
    print(sequence)
    print(len(sequence))
    print(a_count)

    gc_percent = (sequence.count("G") + sequence.count("C")) / len(sequence) * 100
    print(gc_percent)

    if gc_percent >= 50:
        print("High GC")
    else:
        print("Low GC")