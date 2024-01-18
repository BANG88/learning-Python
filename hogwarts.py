"""
hogwarts
Created at: 2024/1/16 by bang
"""

students = ['bang', 'zhangsan', 'lisi', 'wangwu']

for _ in students:
    print(_)


for s in range(len(students)):
    print(students[s])

dict_students = {'bang': 100, 'zhangsan': 90, 'lisi': 80, 'wangwu': 70}

for k, v in dict_students.items():
    print(k, v)

print()

print(dict_students['bang'])

print(dict_students.get('bang'))

for s in dict_students:
    print(s, dict_students[s], sep=',')


students_list = [
    {
        "name": "bang",
        "age": 18,
    },
    {
        "name": "zhangsan",
        "age": 19,
    },
    {
        "name": "lisi",
        "age": 20,
    },
    {
        "name": "wangwu",
        "age": None,
    },
]

for s in students_list:
    print(s['name'], s['age'], s, sep=',')


