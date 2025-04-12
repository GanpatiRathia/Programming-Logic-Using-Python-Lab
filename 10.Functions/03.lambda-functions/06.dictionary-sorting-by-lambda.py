d = {'apple': 2, 'banana': 1, 'cherry': 3}
sorted_items = sorted(d.items(), key=lambda x: x[1])
print(sorted_items)  # [('banana', 1), ('apple', 2), ('cherry', 3)]
