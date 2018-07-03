#Variable parameter

def func(*args, **kwargs):
    print (args)
    print (kwargs)

func(1,2,3,a=1,b=2,c=3)
func(1,2,3)
func(*[1,2,3])
func(**{'a':1,'b':2,'c':3})
