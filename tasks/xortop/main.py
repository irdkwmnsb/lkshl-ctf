with open("output.txt", "w") as f: 
    key = # some x 0<x<256
    flag = "some string"
    encrypted_flag = []
    for i in range(len(flag)):
        encrypted_flag.append(ord(flag[i]) ^ key)
    encrypted_flag.reverse()
    print(" ".join(str(e) for e in encrypted_flag), file=f)
    
    
