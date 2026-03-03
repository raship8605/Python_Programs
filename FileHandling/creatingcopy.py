# Source file
source_file = "example.txt"

# Destination file
dest_file = "copy.txt"

with open(source_file, "r") as src, open(dest_file, "w") as dest:
    dest.write(src.read())

print(f"Content copied from {source_file} to {dest_file}")