shopping_list = []

while True:
    item = input("Enter an item for your shopping list (press q to quit): ")
    if item == "q":
        break
    shopping_list.append(item)

print("Your shopping list:")
for item in shopping_list:
    print(item)
