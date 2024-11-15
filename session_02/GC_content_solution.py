# Step 1: Get user input for the DNA sequence
dna_sequence = input("Enter a DNA sequence: ")

# Step 2: Convert the sequence to uppercase
dna_sequence = dna_sequence.upper()

# Step 3: Count the number of G's and C's in the sequence
g_count = dna_sequence.count("G")
c_count = dna_sequence.count("C")

# Step 4: Calculate the total GC content
total_gc_content = g_count + c_count

# Step 5: Calculate the length of the DNA sequence
dna_length = len(dna_sequence)

# Step 6: Compute the GC content as a percentage
gc_content = (total_gc_content / dna_length) * 100
# Step 7: Output the result
print(f"The GC content of the DNA sequence is {gc_content:.2f}%")
