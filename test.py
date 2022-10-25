
number = [1, 2, 3 ,4]
print("Without using range")
for i in number:
  print(i)

print()

# start from 0
for i in range(len(number)):
  print("index is ", i)
  print("value is ", number[i])