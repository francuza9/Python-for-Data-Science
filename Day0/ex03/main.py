from NULL_not_found import NULL_not_found
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False
print(NULL_not_found(Nothing))
print(NULL_not_found(Garlic))
print(NULL_not_found(Zero))
print(NULL_not_found(Empty))
print(NULL_not_found(Fake))
print(NULL_not_found("Brian"))

"""
EXPECTED OUTPUT:

$>python tester.py | cat -e
Nothing: None <class 'NoneType'>$
0$
Cheese: nan <class 'float'>$
0$
Zero: 0 <class 'int'>$
0$
Empty: <class 'str'>$
0$
Fake: False <class 'bool'>$
0$
Type not Found$
1$
$>
"""