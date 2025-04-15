try:
    f = open("testfile.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("This block always runs.")
