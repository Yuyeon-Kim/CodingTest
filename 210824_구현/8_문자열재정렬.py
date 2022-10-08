s=sorted(input())
sum=0
for idx, c in enumerate(s):
  if c.isdigit():
    sum+=int(c)
  else:
    print("".join(s[idx:])+str(sum))
    break