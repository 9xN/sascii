import string
A = [[' ', '┌', '─', '┐'], [' ', '├', '─', '┤'], [' ', '┴', ' ', '┴']]
B = [[' ', '┌', '┐', ' '], [' ', '├', '┴', '┐'], [' ', '└', '─', '┘']]
C = [[' ', '┌', '─', '┐'], [' ', '│', ' ', ' '], [' ', '└', '─', '┘']]
D = [[' ', '┌', '┬', '┐'], [' ', ' ', '│', '│'], [' ', '─', '┴', '┘']]
E = [[' ', '┌', '─', '┐'], [' ', '├', '┤', ' '], [' ', '└', '─', '┘']]
F = [[' ', '┌', '─', '┐'], [' ', '├', '┤', ' '], [' ', '└', ' ', ' ']]
G = [[' ', '┌', '─', '┐'], [' ', '│', ' ', '┬'], [' ', '└', '─', '┘']]
H = [[' ', '┬', ' ', '┬'], [' ', '├', '─', '┤'], [' ', '┴', ' ', '┴']]
I = [[' ', ' ', '┬', ' '], [' ', ' ', '│', ' '], [' ', ' ', '┴', ' ']]
J = [[' ', ' ', '┬', ' '], [' ', ' ', '│', ' '], [' ', '└', '┘', ' ']]
K = [[' ', '┬', '┌', '─'], [' ', '├', '┴', '┐'], [' ', '┴', ' ', '┴']]
L = [[' ', '┬', ' ', ' '], [' ', '│', ' ', ' '], [' ', '┴', '─', '┘']]
M = [[' ', '┌', '┬', '┐'], [' ', '│', '│', '│'], [' ', '┴', ' ', '┴']]
N = [[' ', '┌', '┐', '┌'], [' ', '│', '│', '│'], [' ', '┘', '└', '┘']]
O = [[' ', '┌', '─', '┐'], [' ', '│', ' ', '│'], [' ', '└', '─', '┘']]
P = [[' ', '┌', '─', '┐'], [' ', '├', '─', '┘'], [' ', '┴', ' ', ' ']]
Q = [['┌', '─', '┐', ' '], ['│', '─', '┼', '┐'], ['└', '─', '┘', '└']]
R = [[' ', '┬', '─', '┐'], [' ', '├', '┬', '┘'], [' ', '┴', '└', '─']]
S = [[' ', '┌', '─', '┐'], [' ', '└', '─', '┐'], [' ', '└', '─', '┘']]
T = [[' ', '┌', '┬', '┐'], [' ', ' ', '│', ' '], [' ', ' ', '┴', ' ']]
U = [[' ', '┬', ' ', '┬'], [' ', '│', ' ', '│'], [' ', '└', '─', '┘']]
V = [['┬', ' ', ' ', '┬'], ['└', '┐', '┌', '┘'], [' ', '└', '┘', ' ']]
W = [[' ', '┬', ' ', '┬'], [' ', '│', '│', '│'], [' ', '└', '┴', '┘']]
X = [['─', '┐', ' ', '┬'], ['┌', '┴', '┬', '┘'], ['┴', ' ', '└', '─']]
Y = [[' ', '┬', ' ', '┬'], [' ', '└', '┬', '┘'], [' ', ' ', '┴', ' ']]
Z = [[' ', '┌', '─', '┐'], [' ', '┌', '─', '┘'], [' ', '└', '─', '┘']]
_1 = [[' ', '┐', ' ', ' '], [' ', '│', ' ', ' '], [' ', '┴', ' ', ' ']]
_2 = [[' ', '┌', '─', '┐'], [' ', '┌', '─', '┘'], [' ', '└', '─', '┘']]
_3 = [[' ', '┌', '─', '┐'], [' ', ' ', '─', '┤'], [' ', '└', '─', '┘']]
_4 = [[' ', '┬', ' ', '┬'], [' ', '└', '─', '┤'], [' ', ' ', ' ', '┴']]
_5 = [[' ', '┌', '─', '┐'], [' ', '└', '─', '┐'], [' ', '└', '─', '┘']]
_6 = [[' ', '┌', '─', '┐'], [' ', '├', '─', '┐'], [' ', '└', '─', '┘']]
_7 = [[' ', '┌', '─', '┐'], [' ', ' ', '┌', '┘'], [' ', ' ', '┴', ' ']]
_8 = [[' ', '┌', '─', '┐'], [' ', '├', '─', '┤'], [' ', '└', '─', '┘']]
_9 = [[' ', '┌', '─', '┐'], [' ', '└', '─', '┤'], [' ', '└', '─', '┘']]
_0 = [[' ', '┌', '─', '┐'], [' ', '│', ' ', '│'], [' ', '└', '─', '┘']]
A_ = [[' ', '╔', '═', '╗'], [' ', '╠', '═', '╣'], [' ', '╩', ' ', '╩']]
B_ = [[' ', '╔', '╗', ' '], [' ', '╠', '╩', '╗'], [' ', '╚', '═', '╝']]
C_ = [[' ', '╔', '═', '╗'], [' ', '║', ' ', ' '], [' ', '╚', '═', '╝']]
D_ = [[' ', '╔', '╦', '╗'], [' ', ' ', '║', '║'], [' ', '═', '╩', '╝']]
E_ = [[' ', '╔', '═', '╗'], [' ', '╠', '╣', ' '], [' ', '╚', '═', '╝']]
F_ = [[' ', '╔', '═', '╗'], [' ', '╠', '╣', ' '], [' ', '╚', ' ', ' ']]
G_ = [[' ', '╔', '═', '╗'], [' ', '║', ' ', '╦'], [' ', '╚', '═', '╝']]
H_ = [[' ', '╦', ' ', '╦'], [' ', '╠', '═', '╣'], [' ', '╩', ' ', '╩']]
I_ = [[' ', ' ', '╦', ' '], [' ', ' ', '║', ' '], [' ', ' ', '╩', ' ']]
J_ = [[' ', ' ', '╦', ' '], [' ', ' ', '║', ' '], [' ', '╚', '╝', ' ']]
K_ = [[' ', '╦', '╔', '═'], [' ', '╠', '╩', '╗'], [' ', '╩', ' ', '╩']]
L_ = [[' ', '╦', ' ', ' '], [' ', '║', ' ', ' '], [' ', '╩', '═', '╝']]
M_ = [[' ', '╔', '╦', '╗'], [' ', '║', '║', '║'], [' ', '╩', ' ', '╩']]
N_ = [[' ', '╔', '╗', '╔'], [' ', '║', '║', '║'], [' ', '╝', '╚', '╝']]
O_ = [[' ', '╔', '═', '╗'], [' ', '║', ' ', '║'], [' ', '╚', '═', '╝']]
P_ = [[' ', '╔', '═', '╗'], [' ', '╠', '═', '╝'], [' ', '╩', ' ', ' ']]
Q_ = [['╔', '═', '╗', ' '], ['║', '═', '╬', '╗'], ['╚', '═', '╝', '╚']]
R_ = [[' ', '╦', '═', '╗'], [' ', '╠', '╦', '╝'], [' ', '╩', '╚', '═']]
S_ = [[' ', '╔', '═', '╗'], [' ', '╚', '═', '╗'], [' ', '╚', '═', '╝']]
T_ = [[' ', '╔', '╦', '╗'], [' ', ' ', '║', ' '], [' ', ' ', '╩', ' ']]
U_ = [[' ', '╦', ' ', '╦'], [' ', '║', ' ', '║'], [' ', '╚', '═', '╝']]
V_ = [['╦', ' ', ' ', '╦'], ['╚', '╗', '╔', '╝'], [' ', '╚', '╝', ' ']]
W_ = [[' ', '╦', ' ', '╦'], [' ', '║', '║', '║'], [' ', '╚', '╩', '╝']]
X_ = [['═', '╗', ' ', '╦'], ['╔', '╩', '╦', '╝'], ['╩', ' ', '╚', '═']]
Y_ = [[' ', '╦', ' ', '╦'], [' ', '╚', '╦', '╝'], [' ', ' ', '╩', ' ']]
Z_ = [[' ', '╔', '═', '╗'], [' ', '╔', '═', '╝'], [' ', '╚', '═', '╝']]
_1_ = [[' ', '╗', ' ', ' '], [' ', '║', ' ', ' '], [' ', '╩', ' ', ' ']]
_2_ = [[' ', '╔', '═', '╗'], [' ', '╔', '═', '╝'], [' ', '╚', '═', '╝']]
_3_ = [[' ', '╔', '═', '╗'], [' ', ' ', '═', '╣'], [' ', '╚', '═', '╝']]
_4_ = [[' ', '╦', ' ', '╦'], [' ', '╚', '═', '╣'], [' ', ' ', ' ', '╩']]
_5_ = [[' ', '╔', '═', '╗'], [' ', '╚', '═', '╗'], [' ', '╚', '═', '╝']]
_6_ = [[' ', '╔', '═', '╗'], [' ', '╠', '═', '╗'], [' ', '╚', '═', '╝']]
_7_ = [[' ', '╔', '═', '╗'], [' ', ' ', '╔', '╝'], [' ', ' ', '╩', ' ']]
_8_ = [[' ', '╔', '═', '╗'], [' ', '╠', '═', '╣'], [' ', '╚', '═', '╝']]
_9_ = [[' ', '╔', '═', '╗'], [' ', '╚', '═', '╣'], [' ', '╚', '═', '╝']]
_0_ = [[' ', '╔', '═', '╗'], [' ', '║', ' ', '║'], [' ', '╚', '═', '╝']]
_ = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]

def print_banner(banner, init_color, chosen, prefix, suffix):
    final = []    
    txt_color = init_color
    cl = 0
    if chosen != True:
        print(f'\n{init_color}')
    for charset in range(0, 3):
        final.insert(len(final), prefix)
        for pos in range(0, len(banner)):
            for i in range(0, len(banner[pos][charset])):
                if chosen == True:
                    clr = f'\\033[38;5;{txt_color}m'
                else:
                    clr = f'\033[38;5;{txt_color}m'
                char = f'{clr}{banner[pos][charset][i]}'
                final.append(char)
                cl += 1
                txt_color = txt_color if cl <= 3 else txt_color
            cl = 0
            txt_color = init_color
        init_color += 1
        final.append(suffix)
        if charset < 2:
            final.append('\n   ')
    print(f"   {''.join(final)}")
double_pipe = input("Do you want single line or double line? (s/d) ")
if double_pipe != "s" and double_pipe != "d":
    print("Invalid selection. Exiting...")
    exit()
input_string = input("Enter a string: ")
input_string = input_string.upper()
banner = []
letters = string.ascii_uppercase
numbers = string.digits
for char in input_string:
    if char.isalnum():
        if char.isalpha():
            if double_pipe == "d":
                banner.append(letters[ord(char) - ord('A')] + "_")
            elif double_pipe == "s":
                banner.append(letters[ord(char) - ord('A')])
        elif char.isdigit():
            if double_pipe == "d":
                banner.append("_" + char + "_")
            elif double_pipe == "s":
                banner.append("_" + char)
    elif char == "_":
        banner.append("_")
evaluated_banner = [eval(var) for var in banner]
for i in range(0, 256):
    print_banner(evaluated_banner, init_color=i, chosen=False, prefix="", suffix="")
selection = input("Which one would you like to save? (enter the number) ")
if (selection.isdigit() and int(selection) >= 0 and int(selection) < 256):
    prefix = input("Enter a prefix for each line: (enter nothing for no prefix) ")
    suffix = input("Enter a suffix for each line: (enter nothing for no suffix) ")
    print_banner(evaluated_banner, init_color=int(selection), chosen=True, prefix=prefix, suffix=suffix)
else:
    print("Invalid selection. Exiting...")
    exit()