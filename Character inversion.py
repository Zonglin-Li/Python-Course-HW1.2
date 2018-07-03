#Character inversion(I love China!->China! love I)

import string

a = 'I love China!'
b=list(a.split())
x=[]
for c in reversed (b):
    x.append(c)
print(' '.join(x))
