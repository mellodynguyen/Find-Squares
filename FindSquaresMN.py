"""
Mellody Nguyen
COSC 2436
Program Set 2
References:
https://docs.python.org/3/library/io.html#io.IOBase.readline
https://docs.python.org/3/library/functions.html#open
"""


def play_game():
    """Main function to run game."""
    
    # helper function to open, read, and disect  file
    def open_and_read_file():
        """Let the User input the file name from the keyboard and disect file.
        
        Input will be from a data file where input will contain a single 
        integer T in the range [1,10], the num of test cases, and first line of
        each test contains 2 integers, N and M, the number of rows and columns,
        range [1,100]
        """

        # get filename from user
        txtfile = input("Enter filename: ")

        with open(txtfile, "r") as f:
            # read first line to get number of test cases 
            num_cases = int(f.readline().strip())

            test_cases = []

            # get N and M (2 2)
            num_lines_and_chars = [f.readline().strip()]
            # get the image 
            image = [f.readline().strip()]

        print(image)
        print(num_cases)
        # return num_cases


    # helper function to find the pixels in each squares
    def square_finder(contents):
        """Determine how many fully black squares exist in an image.

        Image is of size N (lines) x M (characters) where each pixel is either 
        white (.) or black (X)

        Example Output:
            >>> Enter Filename: square.txt
            Image 1: 3
            Image 2: 5
            Image 3: 9
            Run Again (Y/N): n
        """

        # print output, for every "square" in the image 
        # print(f"Image{}: {}")
    
    image = open_and_read_file()
    square_finder(image)

play_game()

# Ask if the user wants to run the program again (Check case)
player_answer = input("Do you want to play again? (Y/N): ").upper()
if player_answer == "Y":
    play_game()
else:
    print("Thanks for playing")
    
