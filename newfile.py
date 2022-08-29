#3.1
msg = 'Vitalii Dyshchakivskyi'
print(msg)

#3.6
s = 'colorless'
s =s[0:4]+ 'u' + s[4:9]
print(s)

#3.9
msg = 'Vitalii Dyshchakivskyi'
print(msg[0:22:2])

#3.15
phrase1 = ['Vitalii', 'Petrovych', 'Dyshchakivskyi']
print(phrase1[2][2])

#3.18
phrase1 = ['Vitalii', 'Petrovych', 'Dyshchakivskyi']
lengths=[]
for word in phrase1:
    lengths.append(len(word))
print(lengths)

#3.23
silly = 'newly formed bland ideas are inexpressible in an infuriating way'
silly2 = silly.split(' ')
silly2.sort()
print(silly2)

#3.26
silly = 'newly formed bland ideas are inexpressible in an infuriating way'
phrase = silly.split('in ')
print (phrase)
