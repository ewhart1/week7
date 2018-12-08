#!/usr/bin/env python

# This script is to read a sequence of DNA and count the separate nucleotides

# When entering a sequence, please use all upper case letters (ex: AGCTCA)

dnaSeq = input("Input DNA Sequence:")

# total sequence length
print ("Total Sequence length (characters):")
print (len(dnaSeq))

# number of A's in the nucleotide sequence
print ("Amount of A's within the sequence:")
print (dnaSeq.count("A"))

# T's
print ("Amount of T's within the sequence:")
print (dnaSeq.count("T"))

# G's
print ("Amount of G's within the sequence:")
print (dnaSeq.count("G"))

# C's
print ("Amount of C's within the sequence:")
print (dnaSeq.count("C"))

