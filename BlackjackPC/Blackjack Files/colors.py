BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m' #Default color is white


RE = '\033[0m' #Reset

B_BLACK = '\033[90m' #Bright colors
B_RED = '\033[91m'
B_GREEN = '\033[92m'
B_YELLOW = '\033[93m'
B_BLUE = '\033[94m'
B_MAGENTA = '\033[95m'
B_CYAN = '\033[96m'
B_WHITE = '\033[97m'

if __name__ == "__main__":
    print(f"Colors:\n"
          f"{RED}Red\n"
          f"{GREEN}Green\n"
          f"{YELLOW}Yellow\n"
          f"{BLUE}Blue\n"
          f"{MAGENTA}Magenta\n"
          f"{CYAN}Cyan\n"
          f"{WHITE}White\n\n"
          f"{B_RED}BrightRed\n"
          f"{B_GREEN}BrightGreen\n"
          f"{B_YELLOW}BrightYellow\n"
          f"{B_BLUE}BrightBlue\n"
          f"{B_MAGENTA}BrightMagenta\n"
          f"{B_CYAN}BrightCyan\n"
          f"{B_WHITE}BrightWhite\n")