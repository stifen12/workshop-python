>>> set1 = set([1, 2, 3])
>>> set2 = set([3, 4, 5])
>>> set1 | set2 #union
set([1, 2, 3, 4, 5])
>>> set1 & set2 #intersection
set([3])
>>> set1 -  set2 #difference
set([1, 2])
>>> set1 ^ set2 #symmetric difference (elements that are in the first set and the second, but not in both)
set([1, 2, 4, 5])
>>>