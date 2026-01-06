name = "king maker"
first_char = name[0]
print(first_char)
slice_name = name[0:4]
print(slice_name)

num_list = '0123456789'

print(num_list[:])
print(num_list[:7])
print(num_list[0:-7:1])

print(name.upper())

name1 = "     king      "
print(name1)
print(name.strip())

name2 = "Lemon Chai"
print(name2.replace("Lemon", "Ginger"))

name3 = "Lemon, Ginger, Masala, Mint"
print(name3.split(", "))

print(name3.count(','))
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of chai {}"
print(order.format(quantity, chai_type))
 

variety = ["Mobile", "Tablet", "Laptop"]
print(" ".join(variety))

print(len(name3))

print("Lemon" in name3)