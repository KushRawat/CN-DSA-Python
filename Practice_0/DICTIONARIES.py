# Different methods of creating dictionaries

a = {"avc":123, "abc":45, 1234:"wef"}
print(a)

b = a.copy()
print(b)

c = dict([("abc", 34),("abcd", 234)])
print(c)

d = dict.fromkeys(["abc", 23, 4])
print(d)

e = dict.fromkeys(["abc", 23, 4], 10)
print(e)

a = {}