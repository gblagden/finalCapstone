
#  N.B.  I didn't know if the instructions meant that we were supposed to have the
#  user create an initial grid or not, but I have created a program that
#  starts by asking the user to choose where they place 8 mines on a 5x5 grid.


#  I have started by putting all of my functions at the top of the code, as advised
#  in previous exercises and lectures:




############                       ###############
########       F U N C T I O N S         #########
############                       ###############



# 1)  MINE INPUT FUNCTION  #


def mine_input(name, num):
    while True:
        name = input(f"Mine {num}: ")
        print()

        name = name.lower()
        acceptable_chars_1 = ["a", "b", "c", "d", "e"]
        acceptable_chars_2 = ["1", "2", "3", "4", "5"]

        name_chars = [char for char in name]
        if not name_chars[0] in acceptable_chars_1 or not name_chars[1] in acceptable_chars_2:
            print("You have entered an incorrect grid code.  Please enter a letter followed by a single number.")
            print()
        else:
            if len(name_chars) != 2:
                print("You have entered too many characters.  Please try again!")
                print()
            else:
                name = name.upper()
                if name in mines_placed:
                    print("You have already entered a mine at this place!")
                else:
                    print(f"You have placed Mine {num} at {name}")
                    print()
                    mines_placed.append(name)
                    break



# 2)  MINE PLACEMENT FUNCTION  #


def mine_placement():
    for i in mines_placed:
        if i == "A1":
            empty_grid[0][0] = "#"
        elif i == "A2":
            empty_grid[0][1] = "#"
        elif i == "A3":
            empty_grid[0][2] = "#"
        elif i == "A4":
            empty_grid[0][3] = "#"
        elif i == "A5":
            empty_grid[0][4] = "#"

        elif i == "B1":
            empty_grid[1][0] = "#"
        elif i == "B2":
            empty_grid[1][1] = "#"
        elif i == "B3":
            empty_grid[1][2] = "#"
        elif i == "B4":
            empty_grid[1][3] = "#"
        elif i == "B5":
            empty_grid[1][4] = "#"

        elif i == "C1":
            empty_grid[2][0] = "#"
        elif i == "C2":
            empty_grid[2][1] = "#"
        elif i == "C3":
            empty_grid[2][2] = "#"
        elif i == "C4":
            empty_grid[2][3] = "#"
        elif i == "C5":
            empty_grid[2][4] = "#"

        elif i == "D1":
            empty_grid[3][0] = "#"
        elif i == "D2":
            empty_grid[3][1] = "#"
        elif i == "D3":
            empty_grid[3][2] = "#"
        elif i == "D4":
            empty_grid[3][3] = "#"
        elif i == "D5":
            empty_grid[3][4] = "#"

        elif i == "E1":
            empty_grid[4][0] = "#"
        elif i == "E2":
            empty_grid[4][1] = "#"
        elif i == "E3":
            empty_grid[4][2] = "#"
        elif i == "E4":
            empty_grid[4][3] = "#"
        elif i == "E5":
            empty_grid[4][4] = "#"

    for row in empty_grid:
        print(row)
    print()



# 3)  FUNCTIONS FOR CHANGING THE 'COMPASS' POINTS  #


def change_grid_element(list, num1, num2):
    if list[num1][num2] == "#":
        pass
    elif list[num1][num2] == "-":
        list[num1][num2] = 1
    elif int(list[num1][num2]):
        list[num1][num2] += 1


def change_nw_element(list, num1, num2):
    if list[num1-1][num2-1] == "#":
        pass
    elif list[num1-1][num2-1] == "-":
        list[num1-1][num2-1] = 1
    elif int(list[num1-1][num2-1]):
        list[num1-1][num2-1] += 1


def change_n_element(list, num1, num2):
    if list[num1-1][num2] == "#":
        pass
    elif list[num1-1][num2] == "-":
        list[num1-1][num2] = 1
    elif int(list[num1-1][num2]):
        list[num1-1][num2] += 1


def change_ne_element(list, num1, num2):
    if list[num1-1][num2+1] == "#":
        pass
    elif list[num1-1][num2+1] == "-":
        list[num1-1][num2+1] = 1
    elif int(list[num1-1][num2+1]):
        list[num1-1][num2+1] += 1


def change_w_element(list, num1, num2):
    if list[num1][num2-1] == "#":
        pass
    elif list[num1][num2-1] == "-":
        list[num1][num2-1] = 1
    elif int(list[num1][num2-1]):
        list[num1][num2-1] += 1


def change_e_element(list, num1, num2):
    if list[num1][num2+1] == "#":
        pass
    elif list[num1][num2+1] == "-":
        list[num1][num2+1] = 1
    elif int(list[num1][num2+1]):
        list[num1][num2+1] += 1


def change_sw_element(list, num1, num2):
    if list[num1+1][num2-1] == "#":
        pass
    elif list[num1+1][num2-1] == "-":
        list[num1+1][num2-1] = 1
    elif int(list[num1+1][num2-1]):
        list[num1+1][num2-1] += 1


def change_s_element(list, num1, num2):
    if list[num1+1][num2] == "#":
        pass
    elif list[num1+1][num2] == "-":
        list[num1+1][num2] = 1
    elif int(list[num1+1][num2]):
        list[num1+1][num2] += 1


def change_se_element(list, num1, num2):
    if list[num1+1][num2+1] == "#":
        pass
    elif list[num1+1][num2+1] == "-":
        list[num1+1][num2+1] = 1
    elif int(list[num1+1][num2+1]):
        list[num1+1][num2+1] += 1



# 4)  FUNCTION TO REPLACE '-' WITH '0'  #


def change_dash_element(list, num1, num2):
    if list[num1][num2] == "-":
        list[num1][num2] = 0









############                       ###############
########         P R O G R A M           #########
############                       ###############



#  I start with some introductory print statements:


print()
print("Welcome to Blagden's Minesweeper!")
print()
print("To start, please place your mines at any point on this 5x5 grid:")
print()

print("     1   2   3   4   5")
print("  A  *   *   *   *   *")
print("  B  *   *   *   *   *")
print("  C  *   *   *   *   *")
print("  D  *   *   *   *   *")
print("  E  *   *   *   *   *")
print()

print("To place a mine, please enter the grid square code, and press enter.")
print()
print("For example, 'B4' or 'D2', or to place your mine at the middle position of the grid, please enter 'C3'.")
print()
print("You have 8 mines to place on the grid.  Please enter them now: ")
print()


#  I then created an empty grid as a template for my user to place their 'mines' in:

#  EMPTY GRID CREATION  #

number_of_rows = 5
number_of_columns = 5

empty_grid = [["-"] * number_of_columns for _ in range(number_of_rows)]


#  I created a function that would ask the user where they would like to
#  place the 'mines' on this empty grid - 1) 'MINE INPUT FUNCTION' (see above)

#  I created another function that would update the empty grid positions with a
#  'mine' depending on what the user had entered, and then display the current
#  status of the grid back to the user - 2) 'MINE PLACEMENT FUNCTION' (see above)

#  I then executed both the above functions for each of the 8 mines - getting
#  the user to choose where they want the mines placed, and then placing the
#  mines into the grid.
#  The first function required an empty list called 'mines_placed' with global
#  scope, so I created this empty list before calling the two functions for
#  each of the 8 mines:


mines_placed = []

mine_1 = ""
mine_input(mine_1, 1)
mine_placement()
mine_2 = ""
mine_input(mine_2, 2)
mine_placement()
mine_3 = ""
mine_input(mine_3, 3)
mine_placement()
mine_4 = ""
mine_input(mine_4, 4)
mine_placement()
mine_5 = ""
mine_input(mine_5, 5)
mine_placement()
mine_6 = ""
mine_input(mine_6, 6)
mine_placement()
mine_7 = ""
mine_input(mine_7, 7)
mine_placement()
mine_8 = ""
mine_input(mine_8, 8)
mine_placement()


#  I then displayed the completed grid to the user, and updated the
#  'empty_grid' variable to 'grid':


print("Here is the grid that you have entered: ")
print()

for row in empty_grid:
    print(row)

grid = empty_grid


#  I created a function for each 'compass' grid position that required
#  updating if adjacent to a 'mine'.  I labeled them as the 'compass' positions
#  in relation to the 'mine', and used the table provided in the instructions
#  for identifying what index to associate with each position
#  - 3) FUNCTIONS FOR CHANGING THE 'COMPASS' POINTS (see above):

#  I then used enumerate as demonstrated in the instructions to check every
#  position in the grid to see if its value was a 'mine'.
#  I realised that I needed to use if/elif statements to make sure that the
#  adjacent squares were only updated if they weren't 'out of bounds', as
#  explained in the instructions:


for current_row, row in enumerate(grid, start=0):
    for current_column, column in enumerate(row, start=0):
        if current_row == 0 and current_column == 0 and column == "#":
            change_e_element(grid, current_row, current_column)
            change_se_element(grid, current_row, current_column)
            change_s_element(grid, current_row, current_column)
        elif current_row == 0 and current_column > 0 and current_column < (len(row)-1) and column == "#":
            change_w_element(grid, current_row, current_column)
            change_sw_element(grid, current_row, current_column)
            change_s_element(grid, current_row, current_column)
            change_se_element(grid, current_row, current_column)
            change_e_element(grid, current_row, current_column)
        elif current_row == 0 and current_column == (len(row)-1) and column == "#":
            change_w_element(grid, current_row, current_column)
            change_sw_element(grid, current_row, current_column)
            change_s_element(grid, current_row, current_column)
        elif current_row > 0 and current_row < (len(grid)-1) and current_column == 0 and column == "#":
            change_n_element(grid, current_row, current_column)
            change_ne_element(grid, current_row, current_column)
            change_e_element(grid, current_row, current_column)
            change_se_element(grid, current_row, current_column)
            change_s_element(grid, current_row, current_column)
        elif current_row > 0 and current_row < (len(grid)-1) and current_column == (len(row)-1) and column == "#":
            change_n_element(grid, current_row, current_column)
            change_nw_element(grid, current_row, current_column)
            change_w_element(grid, current_row, current_column)
            change_sw_element(grid, current_row, current_column)
            change_s_element(grid, current_row, current_column)
        elif current_row == (len(grid)-1) and current_column == 0 and column == "#":
            change_n_element(grid, current_row, current_column)
            change_ne_element(grid, current_row, current_column)
            change_e_element(grid, current_row, current_column)
        elif current_row == (len(grid)-1) and current_column > 0 and current_column < (len(row)-1) and column == "#":
            change_w_element(grid, current_row, current_column)
            change_nw_element(grid, current_row, current_column)
            change_n_element(grid, current_row, current_column)
            change_ne_element(grid, current_row, current_column)
            change_e_element(grid, current_row, current_column)
        elif current_row == (len(grid)-1) and current_column == (len(row)-1) and column == "#":
            change_n_element(grid, current_row, current_column)
            change_nw_element(grid, current_row, current_column)
            change_w_element(grid, current_row, current_column)
        elif current_row > 0 and current_row < (len(grid)-1) and current_column > 0 and current_column < (len(row)-1) and column == "#":
            change_nw_element(grid, current_row, current_column)
            change_n_element(grid, current_row, current_column)
            change_ne_element(grid, current_row, current_column)
            change_w_element(grid, current_row, current_column)
            change_e_element(grid, current_row, current_column)
            change_sw_element(grid, current_row, current_column)
            change_s_element(grid, current_row, current_column)
            change_se_element(grid, current_row, current_column)


#  I then created a function that would change every position on the grid
#  that hadn't been updated to hold a value of '0', as the intended
#  output required - 4) FUNCTION TO REPLACE '-' WITH '0'

#  I then used enumerate to make this change throughout the grid:


for current_row, row in enumerate(grid, start=0):
    for current_column, column in enumerate(row, start=0):
        change_dash_element(grid, current_row, current_column)


#  I then displayed the required output to the user, converting all of the
#  the number positions to strings so that it would match the ouput example
#  in the instructions:


print()
print("And here is a grid where every 'mine-free' spot is replaced by a digit, indicating the number of mines immediately adjacent to that spot: ")
print()

for row in grid:
    row_str = [str(x) for x in row]
    print(row_str)

print()