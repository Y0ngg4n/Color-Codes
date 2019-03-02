def getUserInput():
    filename = input("Please enter Filepath: ")
    objectname = input("Please enter objects name to replace: ")
    replacename = input("Please enter objects name to replace with: ")
    replace(filename, objectname, replacename)

def replace(filename, objectname, replacename):
    replacement = ""
    with open(filename, 'r') as f:
        replacement = f.read()
    replacement = replacement.replace(objectname, replacename)
    with open(filename, 'w') as f:
        f.write(replacement)

def main():
    getUserInput()

if __name__ == "__main__": main()
