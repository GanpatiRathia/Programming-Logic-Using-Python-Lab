# Sort by second item
pairs = [(1, 'a'), (3, 'c'), (2, 'b')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # [(1, 'a'), (2, 'b'), (3, 'c')]
