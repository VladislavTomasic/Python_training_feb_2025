string = "11,22,33,44,22,33"

numbers = string.split(",")

print(sum([int(i) for i in numbers if numbers.count(i) == 1]))