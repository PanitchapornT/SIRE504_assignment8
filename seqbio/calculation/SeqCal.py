
# SeqCal module

def countBase(seq, base):
    """
    This function counts the number of occurrences of a specific base in a given DNA sequence.
    
    Parameters:
    seq (str): The DNA sequence in which to count the base (e.g., "ATGC").
    base (str): The base to count within the sequence (e.g., "A").
    
    Returns:
    int: The number of times the specified base appears in the sequence.
    """
    count_base = seq.upper().count(base.upper())
    return count_base

def gcContent(seq):
    """
    This function calculates the GC content of a DNA sequence.
    
    The GC content is the percentage of nucleotides in the sequence that are either 
    guanine (G) or cytosine (C). It is calculated as:
    
    GC Content = (Number of G + Number of C) / (Total Number of Bases) * 100
    
    Parameters:
    seq (str): The DNA sequence for which to calculate GC content (e.g., "ATGC").
    
    Returns:
    float: The GC content as a percentage of the total sequence length.
    """
    gc = (countBase(seq, 'G') + countBase(seq, 'C')) / len(seq) * 100
    return round(gc, 2)

def atContent(seq):
    """
    This function calculates the AT content of a DNA sequence.
    
    The AT content is the percentage of nucleotides in the sequence that are either 
    adenine (A) or thymine (T). It is calculated as:
    
    AT Content = (Number of A + Number of T) / (Total Number of Bases) * 100
    
    Parameters:
    seq (str): The DNA sequence for which to calculate AT content (e.g., "ATGC").
    
    Returns:
    float: The AT content as a percentage of the total sequence length.
    """
    at = (countBase(seq, 'A') + countBase(seq, 'T')) / len(seq) * 100
    return round(at, 2)

def countBasesDict(seq): # got bugs
    """
    Counts the occurrences of each nucleotide base in a given DNA sequence.

    Parameters:
    seq (str): The DNA sequence to be analyzed. The sequence should consist of characters representing nucleotide bases (e.g., 'A', 'T', 'C', 'G').

    Returns:
    dict: A dictionary where the keys are the nucleotide bases and the values are the counts of each base in the sequence.

    Example:
    >>> countBasesDict("ATCGATCGA")
    {'A': 3, 'T': 2, 'C': 2, 'G': 2}
    """
    upper_seq = seq.upper()
    bases = ['A','T','C','G']
    basesM = {}
    for base in bases:
        basesM[base] = countBase(upper_seq, base)
    return basesM


if __name__ == '__main__':
    seq = 'TCAGGGCTAAAGCGCATCCTAC'
    print("test: GC Content:", gcContent(seq))
