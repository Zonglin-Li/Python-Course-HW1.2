#Sort

def compare(x, y,cmp=None):
    if not cmp:
        if x < y:
            return 1
        elif x > y:
            return -1
        else:
            return 0
 
nums = [3, 2, 8 ,0 ,1]
print (compare(nums,sorted))

