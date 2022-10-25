
number = [1, 2, 3 ,4]
print("Without using range")
for i in number:
  print(i)

print()
income = [["Salary", "gig", "commission"], [1000, 200, 300]]
income = [[["Salary", "gig", "commission"], [1000, 200, 300]], [["Salary", "gig", "commission"], [2000, 200, 300]], [["Salary", "gig", "commission"], [3000, 200, 300]]]

# ez method
income_list = []
print("Ez method")
for i in income:
  income_list.append(i[1][0])
print(income_list)

# one line method
print("One line method")
one_income = [i[1][0] for i in income]
print(one_income)

# start from 0
for i in range(len(number)):
  print("index is ", i)
  print("value is ", number[i])

# data analytics

# 1. data import >
# 2. data cleaning >
# 3. data transformation >
# 4. data exploration > find relationship
# 5. data visualization >> graph
