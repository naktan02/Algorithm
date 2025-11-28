n = input()
mius = input()
check = 1
mius_len = len(mius)
count = 0
stack = []
for i in n:
    stack.append(i)
    if len(stack) >= mius_len and "".join(stack[-mius_len:]) == mius:
        del stack[-mius_len:]
    
print( "".join(stack) if stack else 'FRULA')
        
