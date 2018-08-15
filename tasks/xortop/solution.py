out = input()
out = list(map(int, out.split()))
for key in range(0, 256):
    s = ""
    for num in reversed(out):
        s+=chr(num ^ key)
    if(all([0x21 <= ord(a) <= 0x7e for a in s])):
        print(s)
