# inventory = {
#    "Laptop": 10,
#    "Mouse": 25,
#    "Keyboard": 12,
#}

inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 12,
}

# Display inventory
for key, value in inventory.items():
    print(f"{key} : {value}")

# Add product
inventory["usb"] = 50

# Update quantity
inventory["Keyboard"] = 15

# Remove product
inventory.pop("Mouse")