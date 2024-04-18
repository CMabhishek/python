#dictionaries creating

word = input()
print(word)
store = dict()
print(store)

store['q'] = 12
store['p'] = 23
store['W'] = 18
store["channaveeresh"] = 17
print(store)

allkeys = store.keys()
print(allkeys)

allvalues = store.values()
print(allvalues)

#for each loop
for ele in allkeys:
    print(ele)

for ch in "channaveeresh":
    print(ch)


output:DICTIONARIES
{}
{'q': 12, 'p': 23, 'W': 18, 'channaveeresh': 17}
dict_keys(['q', 'p', 'W', 'channaveeresh'])
dict_values([12, 23, 18, 17])
q
p
W
channaveeresh
c
h
a
n
n
a
v
e
e
r
e
s
h
   word = input()
print(word)
store = dict()

for ch in word:
    if ch in store:
        store[ch] = store[ch] + 1
    else:
        store[ch] = 1
print(store)


output:
	abeabedrtdrtksrdkfv
{'a': 2, 'b': 2, 'e': 2, 'd': 3, 'r': 3, 't': 2, 'k': 2, 's': 1, 'f': 1, 'v': 1}



   
    	word = input()
print(word)
store = dict()

for ch in word:
    if ch in store:
        store[ch] = store[ch] + 1
    else:
        store[ch] = 1
print(store)
resultchar = '#'
resultfrequency = 0

allkeys = store.keys()
for ele in allkeys:
    if store[ele] > resultfrequency:
       resultfrequency = store[ele]
       resultchar = ele
print(resultchar, resultfrequency) 


OUTPUT:
abeabedrtrtkasrdkfva
{'a': 4, 'b': 2, 'e': 2, 'd': 2, 'r': 3, 't': 2, 'k': 2, 's': 1, 'f': 1, 'v': 1}
a 4

   word = input()
print(word)
store = dict()

for ch in word:
    if ch in store:
        store[ch] = store[ch] + 1
    else:
        store[ch] = 1
print(store)


output:
	abeabedrtdrtksrdkfv
{'a': 2, 'b': 2, 'e': 2, 'd': 3, 'r': 3, 't': 2, 'k': 2, 's': 1, 'f': 1, 'v': 1}



   
    	word = input()
print(word)
store = dict()

for ch in word:
    if ch in store:
        store[ch] = store[ch] + 1
    else:
        store[ch] = 1
print(store)
resultchar = '#'
resultfrequency = 0

allkeys = store.keys()
for ele in allkeys:
    if store[ele] > resultfrequency:
       resultfrequency = store[ele]
       resultchar = ele
print(resultchar, resultfrequency) 


OUTPUT:
abeabedrtrtkasrdkfva
{'a': 4, 'b': 2, 'e': 2, 'd': 2, 'r': 3, 't': 2, 'k': 2, 's': 1, 'f': 1, 'v': 1}
a 4

