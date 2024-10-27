import os
import sys
import numpy as np
import logging
from itertools import islice

# my_dict = {"apple": 1, "banana": 3, "pire": 5}
#
# print(my_dict.items())
# path = os.path.join("C:/Users/LZAAA/Desktop/intern_apply/Vertrag", "Lebenslauf.pdf")
#
# if os.path.exists(path):
#     print(f"文件 {path} 存在")
# else:
#     print(f"文件 {path} 不存在")

# def my_function(**test):
#
#     my_name = test["YourName"]
#     my_age = test["YourAge"]
#     my_address = test.get("YourAddress", "Another")
#     return my_name, my_age, my_address
#
# NAME, AGE, ADDRESS = my_function(YourName="liuziang", YourAge=25, my_address3="789")
# print(NAME, AGE, ADDRESS)
#
# def setup_profile(**test):
#
#     for key, value in test.items():
#         print(f"{key}: {value}")
#
# additional_info = {"hobby": "painting", "profession": "engineer"}
# setup_profile(name="liuziang", age=18, **additional_info)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#
# def log_function(x_zi):
#     def wrapper(*args, **kwargs):
#         logging.info(f"Running {x_zi.__name__} with arguments {args} and keyword arguments {kwargs}")
#         result = x_zi(*args, **kwargs)
#         logging.info(f"{x_zi.__name__} returned {result}")
#         return result
#
#     return wrapper
#
# @log_function
# def my_func(x,y):
#
#     return x+y
#
# result = my_func(3, 4)
# print("Result:", result)

# logger = logging.getLogger("my")
# print(f"name is {logger.name}")
# logger.setLevel(logging.DEBUG)
# print(f"name is {logger.level}")
# flter = logging.Filter('')

# date = {
#         "key1": "ai",
#         "key2": "wo"
#         }
# print('ni shuo ni %(key1)s %(key2)s' % date)
#
# formatted_string = "Hello %s, you have %d new messages." % ("Alice", 5)
# print(formatted_string)
#
# price = 9.99
# quantity = 3
# print("The total price is %.2f for %d items." % (price, quantity))

# np.random.seed(57)
#
# x = np.random.rand(50)
#
# print(x)
#
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])  #将列表转化为numPY数组
# # print(np.concatenate([a, b], axis=1))
# c = np.hstack([a,b])
# print(c.shape)

# a = np.array([1, 2, 3]).reshape(1, -1)
# b = np.array([1, 2, 3]).reshape(1, -1)
# c = np.concatenate([a,b],axis=0)
# print(c)
# print(c.shape)

# class vector:
#     def __init__(self, x, y: dict):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return vector(self.x+other.x,self.y + other.y)
#
# v1 = vector(10,20)
# v2 = vector(40,30)
# v3 = v1+v2
# print(v3.x)

# list = [1,2,3]
#
# list2 = [4,5,6]
#
# list3 = list[0]+list2[1]
# list4 = list+list2
# print(list3)
# print(list4)

# path = os.path.dirname(os.getcwd())
#
# print(f"the path is {path}")
# print(sys.argv[0])
# # sys.exit(1)
# print(sys.path)


import copy

# original = {'a': [1, 2, 3], 'b': [4, 5, 6]}
# shallow_copy = copy.copy(original)
# deep_copy = copy.deepcopy(original)
# deep_copy['b'][1] = 77
# print(original)       # 输出: {'a': [99, 2, 3], 'b': [4, 5, 6]}
# print(deep_copy)
#
#
# # 修改浅拷贝
# shallow_copy['a'][0] = 99
# print(original)       # 输出: {'a': [99, 2, 3], 'b': [4, 5, 6]}
# print(shallow_copy)   # 输出: {'a': [99, 2, 3], 'b': [4, 5, 6]}

# 修改深拷贝
# deep_copy['b'][1] = 77
# print(original)       # 输出: {'a': [99, 2, 3], 'b': [4, 5, 6]}
# print(deep_copy)


# my_list = [5, 6]
# my_list.append([4, 6])
#
# print(my_list)
#
# my_list_1 = [5, 6]
# my_list_1.extend([4, 6])
# print(my_list_1)


# my_dict = {'a': 1, 'b': 2, 'c': 3}
#
# keys = my_dict.keys()
# items = my_dict.items()
# print(items)
# print(keys)
# for key in my_dict.keys():
#     print(key)
# values = my_dict.values()
# print(values)
my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
for index, value in enumerate(items):
    print(index, value)
# 获取字典的键、值和键值对
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

print(list(items)[0])

result = next(islice(items, 1, 2))
print(result)

# def divide(a, b):
#     # if b == 0:
#     #     raise ValueError("除数不能为零")
#     return a / b
# try:
#     result = divide(10, 0)
# except ValueError as e:
#     print(f"捕获到异常: {e}")
# finally:
#     print("都会执行的")

# def food_generator(foods):
#     for food in foods:
#         yield food
#
# food_gen = food_generator(["meat","rice"])
# for food in food_gen:
#     print(f"This is {food}")

#
# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#     @property
#     def nameCus(self):
#         return self._name, self._age
#
#     @nameCus.setter
#     def nameCus(self, value):
#         name, age = value
#         if not isinstance(name, str):
#             raise TypeError("Name must be a stringaaa")
#         self._name = name
#         self._age = age
#
# name1 = Person("ziang", 25)
#
# print(name1._name)
# name1.nameCus = ("rong", 38)
# print(name1.nameCus)
#
#
