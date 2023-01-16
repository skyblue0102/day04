#input 2 numbers

# start_end = input("start and end number : ").split()
# print(start_end)
# print(int(start_end[0]), int(start_end[1]))

#prime_number
start = int(input("start number : "))
end = int(input("end number : "))
print(start, end)

if end < start:
    start, end = end, start

for i in range(start, end+1):
    # is_prime = True

    if i <= 1:
        continue
    for k in range(2, i):
        if  i % k ==0:
        # is_prime = False
            break
    else:
        print(i, end=' ')