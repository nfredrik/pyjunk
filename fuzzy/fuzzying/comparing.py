from difflib import SequenceMatcher
from typing import Set, Tuple, List


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def compare_strings(
        s1: Set[str],
        s2: Set[str],
        threshold: float = 0.6
) -> Tuple[List[str], List[Tuple[str, str, float]], List[str]]:
    exact_matches = sorted(s1 & s2)

    remaining_s1 = s1 - set(exact_matches)
    remaining_s2 = s2 - set(exact_matches)

    best_matches = []
    used_s2 = set()

    for a in remaining_s1:
        best = None
        best_score = 0.0

        for b in remaining_s2 - used_s2:
            score = similarity(a, b)
            if score > best_score:
                best = b
                best_score = score

        if best and best_score >= threshold:
            best_matches.append((a, best, best_score))
            used_s2.add(best)

    matched_s1 = {a for a, _, _ in best_matches}
    matched_s2 = {b for _, b, _ in best_matches}

    others = sorted(
        (remaining_s1 - matched_s1) |
        (remaining_s2 - matched_s2)
    )

    return exact_matches, best_matches, others
