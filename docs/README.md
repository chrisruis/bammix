# Quick Start

## Basic usage

With a BAM file called bam\_file.bam, to identify the nucleotides at positions 1000, 2000, 3000 and 4000, run:
```
bammix -b bam_file.bam -p 1000 2000 3000 4000
```

## Output

bammix outputs 2 files - position\_base\_counts.csv containing the read depth, nucleotide counts and nucleotide proportions at each of the given positions and position\_base\_counts.pdf containing a plot of the proportion of each nucleotide at each of the given positions. These are the default file names, a prefix can be added with -o as outlined below

<h2>Additional options</h2>

-r Name of the reference that was mapped against. By default, this is extracted from the BAM file but can additionally be specified here

-m Minimum mapping quality for a read to be included in the counts. By default, this is set to include all reads. If -m is set, only reads with a mapping quality of at least the specified value will be included in the output

-q Minimum base quality for a nucleotide to be included in the counts. By default, this is set to include all bases regardless of quality. If -q is set, only bases with a quality of at least the specified value will be included in the output

-o Prefix to add to output files
