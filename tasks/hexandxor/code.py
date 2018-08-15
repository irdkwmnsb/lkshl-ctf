flag = 'some string'
key = ''  # one byte key was removed for security reasons
output = ""
for character in flag:
    temp = ord(character) ^ ord(key)
    output += (hex(temp))[2:] + ' '
    key = chr(temp)
print(output)
