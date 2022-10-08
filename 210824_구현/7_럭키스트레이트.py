n=input()
print("LUCKY" if sum(list(map(int, n[:int(len(n)/2)])))==sum(list(map(int,n[int(len(n)/2):]))) else "READY")