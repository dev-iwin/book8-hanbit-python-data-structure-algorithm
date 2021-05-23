import os
##
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

##
memory = []
root = None
fnameAry = []

##
folderName = 'C:/Program Files/Common Files'
for dirName, subDirList, fnames in os.walk(folderName):
    for fname in fnames:
        fnameAry.append(fname)

# === 여기까지 배열 만들었고, 다음부터 트리 만들고
# 이게 첫 노드이자 루트 노드고
node = TreeNode()
node.data = fnameAry[0]
root = node
memory.append(node)

dupNameAry = []  # 복사본 배열이고

for name in fnameAry[1:]:

    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name == current.data:
            dupNameAry.append(name)
            break
        elif name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right

print('중복 제거 안 함:', dupNameAry)
dupNameAry = list(set(dupNameAry))
print('중복 제거함:', dupNameAry)