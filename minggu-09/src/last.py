>>> last_element = l.pop() #returns the last element, modifying the list
>>> last_element
234
>>> l
['a', 'b', 'c', 123]
>>> third_element = l.pop(2) #returns the third element, modifying the list
>>> third_element
'c'
>>> l
['a', 'b', 123]
>>> l.index('a') 
0
>>> l.index('does not exist in the list')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'does not exist in the list' is not in list
>>> l.count('a') #returns the number of occurrences of an element 
1