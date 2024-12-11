from utils import *

mat = Mat.from_input("example.txt", lambda x: int(x))

for (x, y) in iter(mat):
    print(mat.get(x, y))

print(mat.map)