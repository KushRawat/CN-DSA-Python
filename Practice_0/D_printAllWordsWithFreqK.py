# s = "this is a word string having many many word"
# k = 2

# words = s.split()
# # print(words)

# # return the frequency

# d = {}  
# for w in words:
#     if w in d:
#         d[w] = d[w] + 1
#     else:
#         d[w] = 1

# print(d)

# # a concise method

# d1 = {}
# for w in words:
#     d1[w] = d1.get(w, 0) + 1

# print(d1)

# for w in d1:
#     if d1[w] == k:
#         print(w)

def printKfreqWords(s, k):

    words = s.split()

    d = {}
    for w in words:
        d[w] = d.get(w, 0) + 1

    for w in d:
        if d[w] == 2:
            print(w)

    return

s = input()
k = int(input())
printKfreqWords(s, k)