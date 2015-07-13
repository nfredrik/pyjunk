
# https://www.pinterest.com/pin/317433473712609501/
# https://docs.python.org/2/library/sets.html

set_a = set([1,2,3,4,5,6,7,8,9,10])

set_b = set([1,2,9,10])


# Inner join
print(set_a.symmetric_difference_update(set_b))

# Left join
set_a.intersection_update(set_b)

# Left join excluding common A and B
set_a.difference_update(set_b)

# Right join

# Right join excluding common A B


# Full join
set_a.update(set_b)

# Full join utan intersect

#set_a.update(set_b) - set_a.symmetric_difference_update(set_b)

# 


