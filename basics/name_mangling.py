
class User:
    def __init__(self, name):
        self.name = name
        self.__id = 1
        self.id = 1

u = User('John')
print(f'name: {u.name}, id: {u._User__id}')
print(f'name: {u.name}, id: {u.id}')
#print(f'name: {u.name}, id: {u.__id}') # AttributeError: 'User' object has no attribute '__id'


numbers = [1, 2, 3, 4]
target = 3

for num in numbers:
    if num == target:
        print("Found it!")
        break 
else:  # This WILL execute, target not found
    print("Target not in the list.")
