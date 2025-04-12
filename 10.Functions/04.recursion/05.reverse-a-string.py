def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))  # Output: "olleh"
