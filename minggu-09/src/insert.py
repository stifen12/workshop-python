>>> l = ['a', 'b', 123]
>>> l.append(234) #inserts an element at the end of the list
>>> l
['a', 'b', 123, 234]
>>> l.insert(2, 'c') #inserts an element into the third position
>>> l
['a', 'b', 'c', 123, 234]
>>> l.insert(-1, 111) #inserts an element into the second from last position of the list (negative indices start from the end of the list)
>>> l
['a', 'b', 'c', 123, 111, 234]
>>> l.remove(111) #removes an element based on value
>>> l
['a', 'b', 'c', 123, 234]
>>> l.remove('does not exist in the list') 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list