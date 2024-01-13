from pathlib import Path

path = Path("projectswithmosh")

# path = Path("projectswithmosh")
# print(path.exists())

# path = Path("projectswithmosh")
# print(path.mkdir())

# path = Path("projectswithmosh")
# print(path.rmdir())

for file in path.glob('*'):
    print(file)

# list(path.glob('**/*.py'))

# Absolute path - start from the root of the hard disk
# example = c:\Program Files\Microsoft
# Relative path - path starting from the current directory
