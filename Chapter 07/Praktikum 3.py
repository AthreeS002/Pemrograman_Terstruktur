file = open("data1.txt", "r")

sum = 0
for data in file:
       try:
          sum = sum + int(data)
       except ValueError:
          continue
print(sum)
