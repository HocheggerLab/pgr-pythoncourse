
def get_sequence():
    """
    Get a valid DNA sequence from the user.

    Returns:
        str: A valid DNA sequence.
    """
    while True:
        input_sequence = input("Enter a DNA sequence: ")
        input_sequence = input_sequence.upper()

        # Check if the input only contains valid characters (G, C, T, A)
        if all(char in 'GCTA' for char in input_sequence):
            return input_sequence
        else:
            print("Invalid input. Please enter a sequence containing only G, C, T, or A.")


def count_gc_content(sequence):
    """
    Count the number of G and C in a DNA sequence.

    Args:
        sequence (str): A DNA sequence.

    Returns:
        int: The number of G and C in the sequence.
    """
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    return g_count + c_count

def calculate_gc_content(sequence):
    """
    Calculate the GC content of a DNA sequence.

    Args:
        sequence (str): A DNA sequence.

    Returns:
        float: The GC content of the sequence as a percentage.
    """
    total_gc_content = count_gc_content(sequence)
    dna_length = len(sequence)
    return (total_gc_content / dna_length) * 100

def main():
    sequence = get_sequence()
    gc_content = calculate_gc_content(sequence)
    print(f"The GC content of the DNA sequence is {gc_content:.2f}%")

if __name__ == "__main__":
    main()