string = "1,2,3,4,2,3"

numbers = string.split(",")
print(numbers)

unice = []
for i in numbers:
    if numbers.count(i)==1:
        unice.append(i)

print(unice)