out = input()
out = out.split()
int_out = []
for n in out:
    int_out.append(int(n, 16))
flag = []
for i in range(len(int_out) - 1, -1, -1):
    flag.append(chr(int_out[i] ^ int_out[i - 1]))
print("".join(reversed(flag)))