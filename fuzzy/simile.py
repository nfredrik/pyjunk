
# Implement a function that compare two sets of strings
# First return where strings they have in common.
def compare_strings(set1, set2):
    common = set1.intersection(set2)
    #similar = common - set(s for s in set1 if any(distance(s, t) < 2 for t in set2))
    # [uttryck for yttre_element in yttre_lista for inre_element in inre_lista]
    similar = set() #= set(outer for outer in set1 for set1 for inner for inner in set2)
    for s2 in set2:
        for s1 in set1:
            if s1 not in common:
                if similarity(s1, s2):
                    similar.add((s1,s2))

    #different = set1.symmetric_difference(set2).union(similar)
    different = set2 - common - similar

    return common, similar, different

def distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def similarity(s1: str, s2: str, ratio:float=0.4) -> bool:
    t1 = s1.split("_")
    t2 = s2.split("_")

    common = set(t1) & set(t2)
    max_len = max(len(t1), len(t2))

    return len(common) / max_len >= ratio
