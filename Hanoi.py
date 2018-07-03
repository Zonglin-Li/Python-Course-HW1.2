#Hanoi

def move(n,start,buffer,end):
    if n == 1:
        print(start,'->',end)
    else:
        move(n-1,start,end,buffer)
        move(1,start,buffer,end)
        move(n-1,buffer,start,end)
move(3,'a','b','c')
