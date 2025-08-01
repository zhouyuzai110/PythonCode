import itertools

a = ["one", "two", "three"]
b = ["xxx", "yyy", "zzz"]
c = ["if", "for", "while"]

print("方法1: 使用 itertools.product() - 最推荐的方法")
for i, j, k in itertools.product(a, b, c):
    print(i, j, k)

print("\n方法2: 使用列表推导式")
combinations = [(i, j, k) for i in a for j in b for k in c]
for i, j, k in combinations:
    print(i, j, k)

print("\n方法3: 使用嵌套循环但改进格式")
for i in a:
    for j in b:
        for k in c:
            print(i, j, k)

print("\n方法4: 使用 itertools.chain() 连接列表")
s = list(itertools.chain(a, b))
print(s)

# 或者使用扩展解包（更现代的方法）
s = [*a, *b]
print(s)

print(s[0:3] * 3)
print("%s in %s" % (a, b))