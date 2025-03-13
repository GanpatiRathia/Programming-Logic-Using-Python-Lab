import os


if os.path.exists("existing_file.txt"):
  os.remove("existing_file.txt")

else:
  print("The file does not exist")
