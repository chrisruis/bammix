#!/usr/bin/env python3

import sys
import os
import argparse
import pkg_resources
from collections import Counter

import pysam

from bammix import __version__
from .bammix_functions import *

thisdir = os.path.abspath(os.path.dirname(__file__))
cwd = os.getcwd()

def main(sysargs = sys.argv[1:]):

    parser = argparse.ArgumentParser(#prog = _program,
    description = "bammix",
    usage = '''bammix -b bam_file.bam -p positions [options]''')

    parser.add_argument("-b", "--bam", help = "BAM file to be examined")
    parser.add_argument("-p", "--positions", nargs = "+", help = "Set of positions to be checked")
    parser.add_argument("-r", "--reference", help = "Name of reference the reads were mapped against, will be extracted from the BAM if not provided", default = None)
    parser.add_argument("-q", "--base_quality", help = "Minimum base quality to include a base in counts, default is to include all bases regardless of quality", default = "0")
    parser.add_argument("-m", "--mapping_quality", help = "Minimum mapping quality to include a read in counts, default is to include all reads", default = "0")
    parser.add_argument("-o", "--output_prefix", help = "Optional prefix for output files, default is no prefix", default = None)

    if len(sysargs)<1:
        parser.print_help()
        sys.exit(-1)
    else:
        args = parser.parse_args(sysargs)
    
    #Import BAM
    bam = pysam.Samfile(args.bam, "rb")

    #Minimum base quality
    bq = int(args.base_quality)
    #Minimum mapping quality
    mq = int(args.mapping_quality)

    #Reference sequence name
    if args.reference:
        reference = args.reference
    else:
        reference = bam.get_reference_name(0)

    if args.output_prefix:
        outcsv = os.path.join(cwd + "/" + args.output_prefix + "_position_base_counts.csv")
    else:
        outcsv = os.path.join(cwd + "/" + "position_base_counts.csv")
    
    outFile = open(outcsv, "w")
    outFile.write("Position,Total_reads,A_reads,C_reads,G_reads,T_reads,A_proportion,C_proportion,G_proportion,T_proportion\n")

    positions, read_depth, nA, nC, nG, nT = extract_nucleotides(bam, args.positions, reference, bq, mq, outFile)
    
    outFile.close()

    if args.output_prefix:
        outPlot = os.path.join(cwd + "/" + args.output_prefix + "_position_base_counts.pdf")
    else:
        outPlot = os.path.join(cwd + "/" + "position_base_counts.pdf")

    plot_nucleotides(positions, read_depth, nA, nC, nG, nT, outPlot)

if __name__ == "__main__":
    main()
