tea_varieties = ['Mint', 'Masala', 'Boba', 'Ginger']
print(tea_varieties[-1])
print(tea_varieties[:3])

print(tea_varieties[1:2])

tea_varieties[1:2] = "Green"
print(tea_varieties)

tea_varieties = ['Mint', 'Masala', 'Boba', 'Ginger']
tea_varieties[1:2] = ["Green"]
print(tea_varieties)

print(tea_varieties[1:2]) 
tea_varieties[1:1]  = ["test", "test"]
print(tea_varieties)
print(tea_varieties[1:3])
tea_varieties[1:3]  = []
print(tea_varieties)

squared_nums = [x**2 for x in range(10)]
print(squared_nums)