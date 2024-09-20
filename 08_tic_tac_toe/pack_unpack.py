# PACKING

print(1,2,3,4,5)
numbers = [1,2,3,4,5]
print(numbers)
print(*numbers)
print()

# prints:
# 1 2 3 4 5
# [1, 2, 3, 4, 5]
# 1 2 3 4 5

print("abc")
print(*"abc")
print("a","b","c")
print()

# prints:
# abc
# a b c
# a b c

# UN-PACKING

def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add(1,2,3,4,5,6,7,8,9))
print()

# prints:
# 45

def about(name, age, likes):
    output = f"Meet {name}. They are {age} and like {likes}."
    return output

print(about("joe", 99, "cheese"))
print()

# prints:
# Meet joe. They are 99 and like cheese.

dictionary = {"name": "steve", "age": 40, "likes": "pizza"}
print(about(*dictionary)) # one asterisk
print(about(**dictionary)) # versus two (kwargs - keyword arguments)
print()

# prints:
# Meet name. They are age and like likes.
# Meet steve. They are 40 and like pizza.

def foo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

foo(huda="female", ziyad="male", john="male", alice="female", bob="male")
print()

# prints:
# huda:female
# ziyad:male
# john:male
# alice:female
# bob:male

