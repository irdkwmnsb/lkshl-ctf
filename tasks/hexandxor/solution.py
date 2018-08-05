out = "b 40 13 5b 17 6c 24 17 6f 30 4 6a e 51 29 19 6b 34 0 72 41 1e 6a 5a 2a 57"
out = out.split()
int_out = []
for n in out:
    int_out.append(int(n, 16))
flag = []
for i in range(len(int_out) - 1, -1, -1):
    flag.append(chr(int_out[i] ^ int_out[i - 1]))
print("".join(reversed(flag)))
