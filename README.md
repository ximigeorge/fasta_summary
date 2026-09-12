# FASTA Summary

A small bioinformatics project that calculates sequence length and GC percentage from a FASTA file.

The project contains:

* A Bash implementation for simple single-line FASTA records
* A Python implementation that supports sequences split across multiple lines

## Project structure

```text
fasta-summary/
├── data/
│   └── sequences.fasta
├── scripts/
│   ├── fasta_summary.sh
│   └── fasta_summary.py
├── results/
├── .gitignore
└── README.md
```

## Requirements

* Bash or Git Bash
* Python 3

The Python script uses only the standard library, so no additional packages are required.

## Run the Bash version

```bash
bash scripts/fasta_summary.sh data/sequences.fasta
```

Save the output:

```bash
bash scripts/fasta_summary.sh data/sequences.fasta > results/bash_summary.tsv
```

The Bash implementation expects each sequence to occupy one line.

## Run the Python version

```bash
python scripts/fasta_summary.py data/sequences.fasta
```

On Windows, you can alternatively use:

```bash
py scripts/fasta_summary.py data/sequences.fasta
```

Save the output:

```bash
python scripts/fasta_summary.py data/sequences.fasta > results/python_summary.tsv
```

The Python implementation supports FASTA sequences split across multiple lines.

## Output

Both scripts produce a tab-separated table:

```text
sequence_id    length    gc_percent
TP53_fragment  28        60.71
KRAS_fragment  28        32.14
EGFR_fragment  28        78.57
```

## Skills practised

* Parsing FASTA files
* Calculating sequence length and GC percentage
* Writing Bash and Python scripts
* Using VS Code and its debugger
* Tracking changes with Git
* Publishing a repository on GitHub
