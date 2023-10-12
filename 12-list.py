fruits=["banana","apples","oranges","mangoes"]
print(fruits)
print(type(fruits))
print(len(fruits))
if "oranges" in fruits:
    print("banana is present in list")
if "kiwi" not in fruits:
    print("kiwi is not in the list")

# accesing list elements/-

# print(fruits[1])
# print(fruits[-1])
# print(fruits[0:3])

# append() add the items to the end of the list/-

# fruits.append(20)
# print(fruits)

# inset(index,element) will insert element at particular index/-

# fruits.insert(0,500)
# print(fruits)

#extend() function is used to extend an list with another list/-

fruits2=["pinaapple","kiwi"]
# fruits.extend(fruits2)
# print(fruits)

# pop(index) will remove element from given index
# pop() will remove  element from last/-
fruits.pop()
fruits2.pop(0)
print(fruits)
print(fruits2)

# updating list/-
# fruits[1]="grapes"
# print(fruits)

fruits[1:3]=["papaya"]

# sorting/-
fruits.sort()  # by default it will sort in ascending order
fruits.sort(reverse=True)  # this will sort it in descending order
print(fruits)

# to reverse/-
fruits.reverse()
print(fruits)