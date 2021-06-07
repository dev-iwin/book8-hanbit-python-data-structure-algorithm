from tkinter import *

window = Tk()
window.geometry("600x600")  # 문자열로 전달?
photo = PhotoImage(file = 'pet01.gif')

photoAry = []
h = photo.height()
w = photo.width()
for i in range(h):
    for k in range(w):
        r, g, b = photo.get(i, k)
        value = (r + g + b) // 3
        photoAry.append(value)

for i in range(len(photoAry)):
    if photoAry[i] <= 127:
        photoAry[i] = 0
    else:
        photoAry[i] = 255

pos = 0
for i in range(h):
    for k in range(w):
        r = g = b = photoAry[pos]
        pos += 1 # 한 번더 중첩하는 것보다 더 효율적일 듯
        photo.put("#%02x%02x%02x" % (r, g, b), (i, k))

paper = Label(window, image=photo)
paper.pack(expand=1, anchor=CENTER)
window.mainloop()
