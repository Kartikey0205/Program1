f = open("lexical.txt", "r")  # open and read file
content = f.read().replace('\n', ' ')  # store the read content in the variable content
print(content)
content_list = content.split(" ")  # split content of file to convert it into list when there is a space
f.close()  # close the file
print(content_list)
kw = ['auto', 'double', 'int', 'struct', 'break', 'else', 'long', 'switch', 'case', 'enum', 'register', 'typedef',
      'char', 'extern', 'return', 'union', 'continue', 'for', 'signed', 'void',
      'do', 'if', 'static', 'while', 'default', 'goto', 'sizeof', 'volatile', 'const', 'float', 'short', 'unsigned']
# specialchar= ['~', '%','|','@','+','<','_','-','>','^','#','=','&','$','/','(','*','\','\)','`',':','[','\"',';',
# '\,',']','!','{','?','.','}'


c = 1
for word in content_list:

    if word in kw:
        c = c + 1
        print(word, "is a keyword")
    elif word.isdigit():
        c = c + 1
        print(word, "is a constant")
    elif len(word) == 1:
        if (33 <= ord(word) <= 47) or (58 <= ord(word) <= 64) or (
                123 <= ord(word) <= 126):
            print(word, "is a special character")
            c = c + 1
    elif ".h" in word:
        c = c + 1
        print(word, "is a header")
    elif "#" not in word:
        c = c + 1
        print(word, "is an identifier")
    else:
        for w in word:
            if w[0] == "#":
                print(word, "is a preprocessor")

        c = c + 1
print("The number of tokens are", c)
