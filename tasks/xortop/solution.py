out = "189 164 172 178 240 183 159 244 164 159 174 241 159 178 243 168 176 241 163 159 240 180 176 185 178 163 159 180 245 243 162 159 243 168 148 187 140 136 147 139 140"
out = list(map(int, out.split()))
for key in range(0, 256):
    for num in reversed(out):
        print(chr(num ^ key), end="")
    print()
