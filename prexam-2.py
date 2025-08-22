inventory = []

while True:
    item_name = input("\nEnter item name: ")
    category = input("Enter category: ").lower()
    quantity = int(input("Enter quantity: "))

    inventory.append({
        "name": item_name,
        "category": category,
        "quantity": quantity
    })

    more = input("Do you want to add more items? (y/n): ").lower()
    if more != 'y':
        break

print("\n=========== INVENTORY SUMMARY ===========\n")


total_items = len(inventory)
item_names = [item["name"] for item in inventory]
print(f"Total Different Items: {total_items}")
print(f"Explanation: You entered {total_items} different items: {', '.join(item_names)}.\n")


total_quantity = sum(item["quantity"] for item in inventory)
quantities = " + ".join(str(item["quantity"]) for item in inventory)
print(f"Total Quantity in Stock: {total_quantity}")
print(f"Explanation: Sum of all quantities: {quantities} = {total_quantity}\n")


average_quantity = total_quantity / total_items
print(f"Average Quantity per Item: {average_quantity}")
print(f"Explanation: Average = {total_quantity} total / {total_items} items\n")



most_stocked = max(inventory, key=lambda x: x["quantity"])
least_stocked = min(inventory, key=lambda x: x["quantity"])
print(f"Most Stocked Item: {most_stocked['name']} ({most_stocked['quantity']} units)")
print(f"Explanation: {most_stocked['name']} has the highest quantity among all items.\n")

print(f"Least Stocked Item: {least_stocked['name']} ({least_stocked['quantity']} units)")
print(f"Explanation: {least_stocked['name']} has the lowest quantity.\n")

print("-" * 40)


categories = {item["category"] for item in inventory}
print(f"Unique Categories in Inventory: {categories}")
print("Explanation: Categories are taken from user input and converted to lowercase.")
print("No duplicates are shown here.\n")