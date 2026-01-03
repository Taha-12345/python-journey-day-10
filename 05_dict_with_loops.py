students = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 78
}

# Loop through dictionary
for name, marks in students.items():
    print(name, "scored", marks)

print("-" * 30)

# Word frequency example
sentence = "python is easy and python is powerful"
words = sentence.split()

count = {}
for word in words:
    count[word] = count.get(word, 0) + 1

print(count)