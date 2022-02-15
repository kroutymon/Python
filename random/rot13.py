#character library 
import string

lower = list(string.ascii_lowercase)
upper = list(string.ascii_lowercase)

def rot13(msg):
    result = ''
    for character in msg:
        if character in upper:
            result += upper[(upper.index(character) + 13) % 26]
        elif character in lower:
            result += lower[(lower.index(character) + 19) %26]
        else:
            result += character
    return result

  

print(rot13("Hallo das ist ein Test"))
print(rot13("Hnyyb qnf vfg rva Trfg"))