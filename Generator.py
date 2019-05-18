def reverse(data):
    for index in range(len(data) - 1, 0, -1):
        yield data[index]

for char in reverse('shenchen pan'):
    print(char)


print(sum(i*i for i in range(10)))
xvec = [10, 20, 30]
yvec = [7, 5, 3]
total = sum(x*y for x,y in zip(xvec, yvec))         # dot product
print(total)

from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
print(sine_table)

unique_words = set(word  for line in ["12 3123", "dfs ads"]  for word in line.split())
print(unique_words)

# valedictorian = max((student.gpa, student.name) for student in graduates)
# print(valedictorian)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
