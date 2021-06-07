from tkinter import *

## 클래스와 함수
def qSort(arr, start, end):
    if end <= start:
        return

    low = start
    high = end

    pivot = arr[(low+high) // 2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low+1, high-1

    mid = low

    qSort(arr, start, mid-1)
    qSort(arr, mid, end)

def quickSort(ary):
    qSort(ary, 0, len(ary)-1)


## 메인 코드
window = Tk()
window.geometry("600x600")
photo = PhotoImage(file = 'pet02.gif')

photoAry = []
h = photo.height()
w = photo.width()
for i in range(h):
    for k in range(w):
        r, g, b = photo.get(i, k)
        value = (r + g + b) // 3
        photoAry.append(value)

dataAry = photoAry[:]
quickSort(dataAry)
midValue = dataAry[h*w//2]  # [len(dataAry) // 2]  # 책은..??!!!!

for i in range(len(photoAry)):
    if photoAry[i] <= midValue:
        photoAry[i] = 0
    else:
        photoAry[i] = 255

pos = 0
for i in range(h):
    for k in range(w):
        r = g = b = photoAry[pos]
        pos += 1  # 한 번더 중첩하는 것보다 더 효율적일 듯
        photo.put("#%02x%02x%02x" % (r, g, b), (i, k))

paper = Label(window, image=photo)
paper.pack(expand=1, anchor=CENTER)
window.mainloop()