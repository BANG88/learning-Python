"""
example08
Created at: 2023/12/27 by bang
"""

"""
- 列表的定义
列表 list 有序的 可变的 可重复的 任意类型的 元素 用[]表示 用逗号分隔 用索引访问 用切片访问 用for循环遍历 用len()获取长度 用+拼接 用*重复
列表的方法 append() insert() pop() remove() clear() index() count() sort() reverse() copy() extend() del
列表的嵌套 [[],[],[]]
列表的推导式 [x for x in range(10) if x%2==0] [x+y for x in 'abc' for y in '123']
列表的解包 a,b,c = [1,2,3]
列表的切片 [start:end:step] [::] [::-1] [1::2] [1:5:2] [1:5:-1] [5:1:-1]
列表的排序 sort() reverse=True sorted() reverse=True
列表的拼接 + extend() append() insert()
列表的删除 del pop() remove() clear()
列表的复制 copy() [:] list()
列表的查找 index() count() in not in
列表的长度 len()
列表的遍历 for in while
列表的增删改查
列表的增加 append() insert() extend()

"""


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list.remove(5)

print(my_list)
# 修改列表中的元素
my_list[0] = 100
a, b, c, _, _, _, _, _, _ = my_list

print(a, b, c)

for my in my_list:
    print(my)

while len(my_list) > 0:
    print(my_list.pop())

"""
- 元组的定义
元组 tuple 有序的 不可变的 可重复的 任意类型的 元素 用()表示 用逗号分隔 用索引访问 用切片访问 用for循环遍历 用len()获取长度 用+拼接 用*重复
元组的方法 index() count() len() + * in not in del 
元组的嵌套 ((),(),())
元组的推导式 (x for x in range(10) if x%2==0) (x+y for x in 'abc' for y in '123')
元组的解包 a,b,c = (1,2,3)
元组的切片 [start:end:step] [::] [::-1] [1::2] [1:5:2] [1:5:-1] [5:1:-1]
元组的排序 sort() reverse=True sorted() reverse=True
元组的拼接 + extend() append() insert()
元组的删除 del pop() remove() clear()
元组的复制 copy() [:] tuple()
元组的查找 index() count() in not in
元组的长度 len()
元组的遍历 for in while
元组的增删改查
元组的增加 append() insert() extend()

"""


my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(my_tuple)

a, b, c, _, _, _, _, _, _, _ = my_tuple

print(a, b, c)

print(f"my_tuple[5] = {my_tuple[4]}")

for my in my_tuple:
    print(my)


"""
- 字典的定义

字典 dict 无序的 可变的 不可重复的 key不可变的 value任意类型的 元素 用{}表示 用逗号分隔 用key访问 用for循环遍历 用len()获取长度 用+拼接 用*重复
字典的方法 get() keys() values() items() update() pop() popitem() clear() del
字典的嵌套 {{},{},{}}
字典的推导式 {x:x for x in range(10) if x%2==0} {x+y:x for x in 'abc' for y in '123'}
字典的解包 a,b,c = {1:1,2:2,3:3}
字典的切片 [start:end:step] [::] [::-1] [1::2] [1:5:2] [1:5:-1] [5:1:-1]
字典的排序 sort() reverse=True sorted() reverse=True
字典的拼接 + extend() append() insert()
字典的删除 del pop() remove() clear()
字典的复制 copy() [:] dict()
字典的查找 index() count() in not in
字典的长度 len()
字典的遍历 for in while
字典的增删改查
字典的增加 append() insert() extend()

"""

my_dict = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
print(my_dict)

a, b, c, _, _ = my_dict

print(a, b, c)

print(f"my_dict[2] = {my_dict[2]}")

print(f"Keys: {my_dict.keys()}")
print(f"Values: {my_dict.values()}")
print(f"Items: {my_dict.items()}")

my_dict2 = {6: "f", 7: "g", 8: "h", 9: "i", 10: "j"}

my_dict.update(my_dict2)

print(my_dict)

for key, value in my_dict.items():
    print(f"key: {key}, value: {value}")
    print()

print(f"+{'-'*len(my_dict)}+{'-'*len(my_dict)}+")

# 根据字典长度生成好看的表格
for key, value in my_dict.items():
    print(f"|{key:^10}|{value:^10}|")
    print(f"+{'-'*len(my_dict)}+{'-'*len(my_dict)}+")
