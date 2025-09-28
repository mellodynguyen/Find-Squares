"""
Mellody Nguyen
COSC 2436
Program Set 2
References:
https://docs.python.org/3/library/io.html#io.IOBase.readline
https://docs.python.org/3/library/functions.html#open
"""

# helper function to find the black pixels in each square
def square_finder(N, M, image):
    """Determine how many fully black squares exist in an image.

    Image is of size N (lines) x M (characters) where each pixel is either 
    white (.) or black (X)
    """
    # variable to hold num of squares
    total = 0

    max_squares = min(N, M)
    
    # Try all square sizes from 1x1 up to min(n, m)
    for k in range(1, max_squares + 1):
        # Slide a N x M window over the grid
        for i in range(N - k + 1):
            for j in range(M - k + 1):
                # Check if all cells in this N x M block are "X"
                all_black = True
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        if image[r][c] != "X":
                            all_black = False
                            break
                    if not all_black:
                        break
                if all_black:
                    total += 1
    return total


def play_game():
    """Main function to run game."""
    
    # helper function to open, read, and disect  file
    def open_and_read_file():
        """Let the User input the file name from the keyboard and disect file.
        
        Input will be from a data file where input will contain a single 
        integer T in the range [1,10], the num of test cases, and first line of
        each test contains 2 integers, N and M, the number of rows and columns,
        range [1,100]

        Example Output:
            # >>> Enter Filename: square.txt
            # Image 1: 3
            # Image 2: 5
            # Image 3: 9
            # Run Again (Y/N): n
        """

        # get filename from user
        txtfile = input("Enter filename: ")

        with open(txtfile, "r") as f:
            # read first line to get number of test cases 
            num_cases = int(f.readline().strip())

            for case in range(1, num_cases + 1):
                # get N and M (2 2)
                N, M = map(int, f.readline().strip().split())
                # get the image 
                image = [list(f.readline().strip()) for _ in range(N)]
                # print output, for every "square" in the image 
                result = square_finder(N, M, image)
                print(f"Image {case}: {result}")


    # print(image)
    # print(num_cases)
    open_and_read_file()

play_game()

# Ask if the user wants to run the program again (Check case)
player_answer = input("Do you want to play again? (Y/N): ").upper()
if player_answer == "Y":
    play_game()
else:
    print("Thanks for playing")
    
