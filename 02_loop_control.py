#Loop Control Statements

# break example
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("-" * 30)

# continue example
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("-" * 30)

# pass example
for i in range(3):
    pass

print("Loop executed with pass")
