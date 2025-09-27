"""
Mellody Nguyen
COSC 2436
Program Set 2
References:
"""

def open_file(txtfile):
    """Input will be from a data file where input will contain a single integer 
    T in the range [1,10], the num of test cases, and first line of each test
    contains 2 integers, N and M, the number of rows and columns, range [1,100]
    
    Let the User input the file name from the keyboard
    """
    
    contents = open(txtfile).read()

    return contents

def main():
    """Determine how many fully black squares exist in an image
    image is of size N x M where each pixel is either white (.) or black (X)

    Program should ask if the user wants to run the program again (Check case)

    Example Output:

        >>> Enter Filename: square.txt
        3
        2 2
        XX
        .X
        2 2
        XX
        XX
        3 3
        XX.
        XXX
        .XX
        Image 1: 3
        Image 2: 5
        Image 3: 9
        Run Again (Y/N): n
    """

    # substance 
    
