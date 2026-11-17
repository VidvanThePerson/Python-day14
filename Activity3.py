l = [4,2,5,7,9,8,10]
print("Original List = ",l)
count = 0
for i in l:
    count += 1
avg = count/len(l)
print("Amount =",count)
print("Average =",avg)
l.sort()
print("Smallest element is:",l[0])
print("Largest element is:",l[-1])