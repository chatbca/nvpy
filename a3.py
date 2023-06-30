t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)


half_len = len(t1) // 2
print(t1[:half_len])
print(t1[half_len:])

t2=()
for i in t1:
    if i%2==0:
        t2+=(i,)
print("tuple with even number",t2)


t2 = (11, 13, 15)
t3 = t1 + t2
print("t1+t2:",t3)


max_val = max(t1)
min_val = min(t1)
print(f"Max value: {max_val}")
print(f"Min value: {min_val}")
