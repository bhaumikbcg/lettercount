w = 'kjkjshhddhnjkshsqhskdh'
a = dict()
for z in w:
    a[z] = a.get(z,0)+1
print(a)



word= 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)
