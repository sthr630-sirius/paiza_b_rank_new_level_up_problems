n = int(input())
t_list = []
y_list = []
x_list = []
for _ in range(n):
    t, y, x = map(int, input().split())
    t_list.append(t)
    y_list.append(y)
    x_list.append(x)
print(t_list)

for i in range(n):
    print(t_list[i])

