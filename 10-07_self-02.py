## 10-07
def gugu(dan, num):
    print('%d * %d = %d' % (dan, num, dan * num))
    if num < 9:
        gugu(dan, num+1)

for dan in range(2, 10):
    print('## %d단 ##' % dan)
    gugu(dan, 1)

print('====='*22)

## self 10-2
def gugu2(dan, num):
    print('%d x %d = %2d' % (dan, num, dan * num), end='    ')
    if dan < 9:
        gugu2(dan+1, num)

for num in range(1, 10):
    gugu2(2, num)
    print()
