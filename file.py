# Read
with open('C:/Users/rathi/Documents/Python/pythonCodes/file.txt', 'r') as f:
    content = f.read()
print(content)
f.close
# Write
with open('C:/Users/rathi/Documents/Python/pythonCodes/file.txt', 'w') as f:
    f.write("Hello World")
    
    print(content)
    f.close
