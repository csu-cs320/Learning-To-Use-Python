# Python basics
# in ipython3


# from the shell, type 'ipython3' and hit enter to start the interpreter
denver:~$ ipython3<enter>
Python 3.5.2+ (default, Sep 22 2016, 12:18:14)

IPython 2.4.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

# notice the different ways you can inspect objects or get help
# try ?, and type 'q' when you want to leave the introduction


# we exit the interpreter with Ctrl-D or by running the exit function
In [1]: exit()
# now we are back at the shell, let's get back in


In [1]: x = 5 # variables hold any type

In [2]: x ** 100 # x raised to the hundred, the int type is arbitrary precision
Out[2]: 7888609052210118054117285652827862296732064351090230047702789306640625

In [3]: x = 5.0

In [4]: type(x)
Out[4]: float

In [5]: x ** 100 # float types have limited precision
Out[5]: 7.888609052210118e+69

In [6]: 5 / 2 # in python 3, division doesn't truncate
Out[6]: 2.5

In [7]: 5 // 2 # use this in python 3 to get truncation
Out[7]: 2

In [8]: int(2.5) # you can always force it to an int
Out[8]: 2

In [9]: float(2) # or to a float
Out[9]: 2.0

In [10]: x = 5

In [11]: if 3 <= x < 7: # you can chain comparisons
   ....:     print(x) # print is a function in python 3
   ....:     
5

In python, code blocks are not defined by {} but rather by indentation
*for sanity, always indent with spaces
How many spaces is up to you, four is recommended.
But as long as all the lines you want inside the block have the _same_
indentation, python will treat them as a block

In [12]: type('hello')
Out[12]: str

In [13]: type("hello")
Out[13]: str

In [14]: for c in "hello":
   ....:     print(c)
   ....:     
h
e
l
l
o

In [15]: for x in range(1, 5):
   ....:     print(x)
   ....:     
1
2
3
4

In [16]: range(1, 5)
Out[16]: range(1, 5)

In [17]: list(_)
Out[17]: [1, 2, 3, 4]

In [18]: for x in range(5):
   ....:     print(x, end=' ')
   ....:     
0 1 2 3 4 
In [19]: list(range(5))
Out[19]: [0, 1, 2, 3, 4]

In [20]: list(range(2, 5))
Out[20]: [2, 3, 4]

In [21]: list(range(2, 5, 2))
Out[21]: [2, 4]

In [22]: list(range(5, 2))
Out[22]: []

In [23]: list(range(5, 2, -1))
Out[23]: [5, 4, 3]

In [24]: "Hello, {}!".format("world")
Out[24]: 'Hello, world!'

In [25]: if True or False:
   ....:     print("T")
   ....:     
T

In [26]: if True and False:
   ....:     print("F")
   ....:     

In [27]: if True and not False:
   ....:     print("T")
   ....:     
T

In [28]: x, y = 'yes', 'no'

In [29]: x if 3 < 4 else y
Out[29]: 'yes'

In [30]: x if 3 > 4 else y
Out[30]: 'no'

In [31]: if "hello":
   ....:     print('truthy')
   ....:     
truthy

In [32]: if None:
   ....:     print('truthy')
   ....:     

In [33]: if False or None or "" or [] or () or {}:
   ....:     print('At least one is ' + 'truthy')
   ....:     

In [34]: '''hello
   ....: multiline strings!'''
Out[34]: 'hello\nmultiline strings!'

In [35]: def my_function():
   ....:     '''This function currently
   ....:     does nothing useful'''
   ....:     pass
   ....: 

In [36]: my_function()

In [37]: my_function
Out[37]: <function __main__.my_function>

In [38]: help(my_function)


In [39]: list('hello')
Out[39]: ['h', 'e', 'l', 'l', 'o']

In [40]: L = _

In [41]: L.append(5)

In [42]: L
Out[42]: ['h', 'e', 'l', 'l', 'o', 5]

In [43]: L.extend(range(6, 14, 3))

In [44]: L
Out[44]: ['h', 'e', 'l', 'l', 'o', 5, 6, 9, 12]

In [45]: len(L)
Out[45]: 9

In [46]: len(['a', 'b', 'c'])
Out[46]: 3

In [47]: len('hello')
Out[47]: 5

In [48]: L[0]
Out[48]: 'h'

In [49]: L[1]
Out[49]: 'e'

In [50]: L[-1]
Out[50]: 12

In [51]: L[-2]
Out[51]: 9

In [52]: L[1:4]
Out[52]: ['e', 'l', 'l']

In [53]: L[:3]
Out[53]: ['h', 'e', 'l']

In [54]: L[-3:]
Out[54]: [6, 9, 12]

In [55]: L[:]
Out[55]: ['h', 'e', 'l', 'l', 'o', 5, 6, 9, 12]

In [56]: L[5:2:-1]
Out[56]: [5, 'o', 'l']

In [57]: L[::-1]
Out[57]: [12, 9, 6, 5, 'o', 'l', 'l', 'e', 'h']

In [58]: [x ** 2 for x in range(4) if x % 2 == 0]
Out[58]: [0, 4]

In [59]: L = []

In [60]: for x in range(4):
   ....:     if x % 2 == 0:
   ....:         L.append(x ** 2)
   ....:         

In [61]: L
Out[61]: [0, 4]

# List comprehensions can model doubly nested for loops too! For example:
# [name * times for name in ['alice', 'bob', 'joe'] for times in range(1, 3)]
# gives us: ['alice', 'alicealice', 'bob', 'bobbob', 'joe', 'joejoe']

In [62]: S = {'a', 'b'}

In [63]: S.<tab> # shows methods you can call
S.add                 S.discard              S.issuperset                   S.union
S.clear               S.intersection         S.pop                          S.update
S.copy                S.intersection_update  S.remove                       
S.difference          S.isdisjoint           S.symmetric_difference         
S.difference_update   S.issubset             S.symmetric_difference_update  

In [63]: type(S)
Out[63]: set

In [64]: help(S.update)


In [65]: help(S.add)


In [66]: S.add('a')

In [67]: S
Out[67]: {'a', 'b'}

In [68]: S.add('c')

In [69]: S
Out[69]: {'a', 'b', 'c'}

In [70]: set('cat')
Out[70]: {'a', 'c', 't'}

In [71]: S.union(set('cat'))
Out[71]: {'a', 'b', 'c', 't'}

In [72]: S
Out[72]: {'a', 'b', 'c'}

In [73]: D = {'a': 1, 'b': 2}

In [74]: type(D)
Out[74]: dict

In [75]: D.
D.clear       D.fromkeys    D.items       D.pop         D.setdefault  D.values      
D.copy        D.get         D.keys        D.popitem     D.update      

In [75]: D.keys()
Out[75]: dict_keys(['b', 'a'])

In [76]: list(_)
Out[76]: ['b', 'a']

In [77]: list(D.values())
Out[77]: [2, 1]

In [78]: list(D.items())
Out[78]: [('b', 2), ('a', 1)]

In [79]: D['a'] = 5

In [80]: D
Out[80]: {'b': 2, 'a': 5}

In [81]: D['c'] = 3

In [82]: D
Out[82]: {'c': 3, 'b': 2, 'a': 5}

In [83]: D['b']
Out[83]: 2

In [84]: for item in D.items():
   ....:     print(item)
   ....:     
('c', 3)
('b', 2)
('a', 5)

In [85]: for k,v in D.items():
   ....:     print("D[{}] => {}!".format(k, v))
   ....:     
D[c] => 3!
D[b] => 2!
D[a] => 5!

In [86]: ord("a")
Out[86]: 97

In [87]: chr(_)
Out[87]: 'a'

In [88]: {chr(x) for x in range(ord('a'), ord('z') + 1) if x % 3 == 0}
Out[88]: {'c', 'f', 'i', 'l', 'o', 'r', 'u', 'x'}

In [89]: type(_)
Out[89]: set

In [90]: {x: chr(x) for x in range(ord('a'), ord('z') + 1) if x % 3 == 0}
Out[90]: {114: 'r', 99: 'c', 117: 'u', 102: 'f', 120: 'x', 105: 'i', 108: 'l', 111: 'o'}

In [91]: type(_)
Out[91]: dict

In [92]: D
Out[92]: {'c': 3, 'b': 2, 'a': 5}

In [93]: {v: k for k,v in D.items()}
Out[93]: {2: 'b', 3: 'c', 5: 'a'}

In [94]: [type(x) for x in [[], (), {}, "", set()]]
Out[94]: [list, tuple, dict, str, set]

In [95]: [type(x) for x in [list(), tuple(), dict(), str(), set()]]
Out[95]: [list, tuple, dict, str, set]

In [96]: type((1, 'a', 5.0))
Out[96]: tuple

In [97]: (1, 'a')
Out[97]: (1, 'a')

In [98]: (1,)
Out[98]: (1,)

In [99]: (1)
Out[99]: 1

In [100]: {{'a': 1}: 3}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-100-0fe99dab4d4d> in <module>()
----> 1 {{'a': 1}: 3}

TypeError: unhashable type: 'dict'

In [101]: {{'a', 1}: 3}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-101-65cdff7a42a5> in <module>()
----> 1 {{'a', 1}: 3}

TypeError: unhashable type: 'set'

In [102]: {['a', 1]: 3}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-102-c07fc7bedaea> in <module>()
----> 1 {['a', 1]: 3}

TypeError: unhashable type: 'list'

In [103]: {('a', 1): 3}
Out[103]: {('a', 1): 3}

In [104]: {'a 1': 3}
Out[104]: {'a 1': 3}

In [105]: tuple([1, 2, 3])
Out[105]: (1, 2, 3)

In [106]: FS = frozenset({'a', 1})

In [107]: {FS: 3}
Out[107]: {frozenset({1, 'a'}): 3}

In [108]: set([1, 2, 1, 2, 3])
Out[108]: {1, 2, 3}

In [109]: L, T, S, D, STR = [1, 2], (1, 2), {1, 2}, {1: 'a', 2: 'a'}, 'aa'

In [110]: [len(coll) for coll in [L, T, S, D, STR]]
Out[110]: [2, 2, 2, 2, 2]

In [111]: [2 in coll for coll in [S, D]]
Out[111]: [True, True]

In [112]: [2 in coll for coll in [L, T]]
Out[112]: [True, True]

In [113]: 'cat' in 'hello, caterpiller!'
Out[113]: True

In [114]: 3 not in D
Out[114]: True

In [115]: Sab = {'a', 'b'}

In [116]: Sabc = set('abc')

In [117]: Scde = set('cde')

In [118]: Sab <= Sabc # Sab.issubset(Sabc) # there is also strict subset, <
Out[118]: True

In [119]: Sab == set(['a', 'b'])
Out[119]: True

In [120]: Sabc >= Sab # Sabc.issuperset(Sab) # there is also strict superset, >
Out[120]: True

In [121]: Sabc | Scde # Sabc.union(Scde)
Out[121]: {'a', 'b', 'c', 'd', 'e'}

In [122]: Sabc & Scde # Sabc.intersection(Scde)
Out[122]: {'c'}

In [123]: Sabc - Scde # Sabc.difference(Scde)
Out[123]: {'a', 'b'}

In [124]: Sabc ^ Scde # Sabc.symmetric_difference(Scde)
Out[124]: {'a', 'b', 'd', 'e'}

# Double equal signs (==) in Python is like .equals in Java.
# You use it on all different types.
# There is also the 'is' keyword, which is rarely used in Python,
# and means 'lives at the same memory address', like == for objects in Java!

In [125]: 2 == 2.0
Out[125]: True

In [126]: L = list(range(3))

In [127]: L == [0, 1, 2]
Out[127]: True

In [128]: T = tuple(range(3))

In [129]: T == (0, 1, 2)
Out[129]: True

In [130]: L == T
Out[130]: False

In [131]: set('abc') == {'a', 'b', 'c'}
Out[131]: True

In [132]: dict(zip(range(5), 'abcde')) == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}
Out[132]: True

In [133]: [1, 2, 3] < [1, 2, 4]
Out[133]: True

In [134]: (1, 2, 3) < (2, 0)
Out[134]: True

In [135]: (1, 2, 3) < (1, 2, 3, 4)
Out[135]: True

In [136]: 'hello' == 'hel' + 'lo'
Out[136]: True

In [137]: {'a': 1, 'b': 2, 'c': 3}.keys() <= set('abcde')
Out[137]: True

In [138]: def gcd(x, y):
   .....:     x, y = sorted([x, y])
   .....:     return x if y % x == 0 else gcd(x, y % x)
   .....: 

In [139]: gcd(252, 105)
Out[139]: 21

In [140]: %cd ~/cs320/python/Learning-Python/
/home/cole/cs320/python/Learning-Python

In [141]: %ls
haiku_Matsuo-Basho.txt helper_functions.py  python_foundation.py  README.md

In [142]: import helper_functions

In [143]: helper_functions.gcd(33, 108)
Out[143]: 3

# haiku_Matsuo-Basho.txt contains:
# An old pond!
# A frog jumps in--
# the sound of water.

In [144]: with open('haiku_Matsuo-Basho.txt') as poem_file:
   .....:     poem_lines = poem_file.readlines()
   .....:     

In [145]: len(poem_lines)
Out[145]: 3

In [146]: poem_lines
Out[146]: ['An old pond!\n', 'A frog jumps in--\n', 'the sound of water.\n']

In [147]: %cpaste
Pasting code; enter '--' alone on the line to stop or use Ctrl-D.
:with open('poem_word_count.txt', mode='w') as f:
:    for line in poem_lines:
:        words = len(line.strip().split())
:        print(words, line, end='', file=f)
:--

# poem_word_count.txt contains:
# 3 An old pond!
# 4 A frog jumps in--
# 4 the sound of water.
