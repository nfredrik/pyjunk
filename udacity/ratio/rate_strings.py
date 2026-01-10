import difflib


def rate_similarity(s1:str, s2:str, ratio:float=0.9) -> bool:
    # Write a function that compare two strings using diff lib and
    # and decide if the ratio is good enough based on ratio
    diff = difflib.SequenceMatcher(None, s1, s2).ratio()
    """ Test function for rate_similarity """
    return diff >= ratio