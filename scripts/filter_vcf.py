import sys

def filter_vcf(input_path, output_path, min_quality):
    with open(input_path) as input_file, open(output_path, "w") as output_file:
        total_variants = 0
        kept_variants = 0
        for line in input_file:
            if line.startswith("#"):
                output_file.write(line)
                continue
            total_variants += 1

            fields = line.strip().split("\t")
            quality = float(fields[5])
            filter_status = fields[6]

            if quality >= min_quality and filter_status == "PASS":
                output_file.write(line)
                kept_variants += 1

        print(f"Kept {kept_variants} out of {total_variants} variants")

if len(sys.argv) != 4:
    print("Usage: python scripts/filter_vcf.py <input-vcf> <output-vcf> <minimum-quality>")
    sys.exit(1)

input_vcf = sys.argv[1]
output_vcf = sys.argv[2]
min_quality = float(sys.argv[3])
filter_vcf(input_vcf, output_vcf, min_quality)