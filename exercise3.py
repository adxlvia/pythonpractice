groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

print("current grocery list:", groceries)

while True:
    item = input("enter an item to remove (or type 'stop' to quit): ").strip().lower()
    if item == "stop":
        break
    if item in groceries:
        groceries.remove(item)
        print("removed", item, ". updated list:", groceries)
    else:
        print(item, "not found in the list. try again.")

print("final grocery list:", groceries)