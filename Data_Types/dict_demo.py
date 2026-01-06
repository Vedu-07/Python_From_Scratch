chai_types = {"Masala" : "Spicy", "Ginger":"Zesty","Green" :"Mild"}
print(chai_types.get("Ginger"))

for chai in chai_types: 
    print(chai, chai_types[chai])


for key, values in chai_types.items():
    print(key, values)


chai_types["Earl Gray"] = "Citrus"

print(chai_types)

keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)