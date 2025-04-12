def print_list(lst, index=0):
    if index >= len(lst):
        return
    print(lst[index])
    print_list(lst, index + 1)

print_list([10, 20, 30, 40])
