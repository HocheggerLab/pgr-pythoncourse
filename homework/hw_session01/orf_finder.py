# Step 1: Define what an ORF is
# An Open Reading Frame (ORF) is a sequence of DNA that starts with a start codon (usually 'ATG')
# and ends with a stop codon ('TAA', 'TAG', or 'TGA').
# The ORF should be a multiple of three, as codons are made of three nucleotides.

# Step 2: Create a codon table (optional step with a dictionary)
# Define a dictionary with codons as keys and the corresponding amino acids as values.
# This will be useful if you want to translate the ORF to an amino acid sequence.
codon_table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGA':'_'
}

# Step 3: Get user input for a DNA sequence
# Ask the user to input a DNA sequence.
# Convert the sequence to uppercase and ensure it only contains valid nucleotides ('A', 'T', 'G', 'C').


# Step 4: Define start and stop codons
# Start codon is 'ATG'.
# Stop codons are 'TAA', 'TAG', and 'TGA'.

# Step 5: Find all ORFs
# Check all three possible reading frames (starting at position 0, 1, or 2).
# For each reading frame, look for a start codon ('ATG'), then scan forward until a stop codon is found.
# Store each valid ORF (from start codon to stop codon) in a list.


# Step 6: Select the largest ORF
# Compare the lengths of all found ORFs and choose the longest one.

# Step 7: Output the result
# Print the largest ORF found, or inform the user if no ORF was found.
