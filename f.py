list1 = [
    '1.Just do It',
    '2.一切皆有可能',
    '3.让编程改变世界',
    '4.Impossible is Nothing'
]

list2 = [
    '4.阿迪达斯',
    '2.李宁',
    '3.鱼C',
    '1.耐克'
]

list3 = [x + ': ' + y[2:] for x in list2 for y in list1 if x[:2] == y[:2]]

list3.sort()

for i in list3:
    print(i)
