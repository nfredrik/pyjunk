class Color:
    """ANSI color codes for terminal text formatting."""
    # Text colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Text styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    INVERSE = '\033[7m'
    
    # Reset all attributes
    RESET = '\033[0m'


def print_color(s: str, *colors: str, end: str = '\n', **kwargs) -> None:
    """
    Print colored text to the terminal using ANSI escape codes.

    :param s: The string to be printed
    :param colors: One or more color/style constants from the Color class
    :param end: String appended after the last value, default is newline
    :param kwargs: Additional keyword arguments to pass to the built-in print function
    
    Example usage:
        print_color("Error!", Color.RED, Color.BOLD)
        print_color("Warning!", Color.YELLOW, end=' ')
        print_color("This is important!", Color.BG_RED, Color.WHITE)
    """
    # Start with all the color codes
    color_codes = ''.join(colors)
    # Reset formatting at the end of the string
    reset_code = Color.RESET if colors else ''
    # Print with colors and reset at the end
    print(f"{color_codes}{s}{reset_code}", end=end, **kwargs)


print_color('hej hopp', Color.BLUE)