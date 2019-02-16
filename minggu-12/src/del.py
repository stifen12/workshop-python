>>> vowels = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5:'u'}
>>> del(vowels[1])
>>> vowels
{2: 'e', 3: 'i', 4: 'o', 5: 'u'}
>>> del(vowels[10])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 10
>>>