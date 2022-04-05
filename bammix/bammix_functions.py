#!/usr/bin/env python3

# imports of built-ins
import os
import sys
import argparse
from collections import Counter

import pysam
import matplotlib.pyplot as plt

#Extracts all of the nucleotides at a given position
def get_bases(bam, position, reference, bq, mq):
    bases = ""

    for c in bam.pileup(reference, (position - 1), position, min_base_quality = bq):
        for r in c.pileups:
            #Check if read mapping quality is high enough to include
            if r.alignment.mapping_quality >= mq:
                if c.pos == (position - 1):
                    if r.query_position is not None:
                        bases += r.alignment.query_sequence[r.query_position]
    
    return(bases)

#Counts the number and calculates the proportion of each nucleotide at each of a given set of positions
def extract_nucleotides(bam, pos, reference, bq, mq, outFile):

    #Lists for plotting
    positions = list()
    read_depth = list()
    nA = list()
    nC = list()
    nG = list()
    nT = list()

    #Iterate through the positions, identify the nucleotide in each read and count each base
    for p in pos:
        position = int(p)

        bases = get_bases(bam, position, reference, bq, mq)

        bc = Counter(bases)

        tr = float(sum(bc.values()))

        outFile.write(p + "," + str(tr) + ",")
        if "A" in bc:
            outFile.write(str(bc["A"]) + ",")
        else:
            outFile.write("0,")
        if "C" in bc:
            outFile.write(str(bc["C"]) + ",")
        else:
            outFile.write("0,")
        if "G" in bc:
            outFile.write(str(bc["G"]) + ",")
        else:
            outFile.write("0,")
        if "T" in bc:
            outFile.write(str(bc["T"]) + ",")
        else:
            outFile.write("0,")
        
        if "A" in bc:
            outFile.write(str(float(bc["A"])/tr) + ",")
            nA.append(float(bc["A"])/tr)
        else:
            outFile.write("0,")
            nA.append(float(0))
        if "C" in bc:
            outFile.write(str(float(bc["C"])/tr) + ",")
            nC.append(float(bc["C"])/tr)
        else:
            outFile.write("0,")
            nC.append(float(0))
        if "G" in bc:
            outFile.write(str(float(bc["G"])/tr) + ",")
            nG.append(float(bc["G"])/tr)
        else:
            outFile.write("0,")
            nG.append(float(0))
        if "T" in bc:
            outFile.write(str(float(bc["T"])/tr) + "\n")
            nT.append(float(bc["T"])/tr)
        else:
            outFile.write("0\n")
            nT.append(float(0))
        
        #Append to plot lists
        positions.append(p)
        read_depth.append(tr)
    
    return(positions, read_depth, nA, nC, nG, nT)

#Plots the proportion of each nucleotide at each position
def plot_nucleotides(positions, read_depth, nA, nC, nG, nT, outPlot):
    fig, ax = plt.subplots()

    #Plot nucleotide proportions
    ax.bar(positions, nA, label = "A", color = "red")
    ax.bar(positions, nC, label = "C", bottom = nA, color = "blue")
    ax.bar(positions, nG, label = "G", bottom = [x + y for x, y in zip(nA, nC)], color = "purple")
    ax.bar(positions, nT, label = "T", bottom = [x + y + z for x, y, z in zip(nA, nC, nG)], color = "orange")

    #Add read depth labels
    for i in range(len(positions)):
        ax.text(i, 1.02, int(read_depth[i]), ha = "center", rotation = "vertical")

    #Read depth label
    if len(positions) <= 5:
        ax.text(-1.5, 1.05, "Read depth:")
    elif len(positions) <= 10:
        ax.text(-2.5, 1.05, "Read depth:")
    else:
        ax.text(-3.5, 1.05, "Read depth:")
    ax.set_xticklabels(positions, rotation = 90)
    ax.set_xlabel("Position")
    ax.set_ylabel("Nucleotide proportion")
    ax.legend(bbox_to_anchor = (1.04, 0.6))

    plt.savefig(outPlot, bbox_inches = "tight")