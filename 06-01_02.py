stack = [None, None, None, None, None]
top = -1

top += 1
stack[top] = "커피"

top += 1
stack[top] = "녹차"

top += 1
stack[top] = "꿀물"

print("----- 스택 상태 (세로형) -----")
for i in range(len(stack)-1, -1, -1):
    print(stack[i])

print("---------------------------")
data = stack[top]
stack[top] = None
top -= 1
print("pop --> ", data)

data = stack[top]
stack[top] = None
top -= 1
print("pop --> ", data)

data = stack[top]
stack[top] = None
top -= 1
print("pop --> ", data)

print("----- 스택 상태 (세로형) -----")
for i in range(len(stack)-1, -1, -1):
    print(stack[i])
