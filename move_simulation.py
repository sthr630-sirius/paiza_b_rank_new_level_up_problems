n = int(input())
p = []
for i in range(n):
    t, y, x = map(int, input().split())
    p.append([t, y, x])

for i in range(n-1):
    t_s = p[i][0]
    y_s = p[i][1]
    x_s = p[i][2]
    t_e = p[i+1][0]
    y_e = p[i+1][1]
    x_e = p[i+1][2]
    t = t_s
    y = y_s
    x = x_s
    dt = 1
    #dy = round((y_e - y_s) / (t_e - t_s))
    #dx = round((x_e - x_s) / (t_e - t_s))
    while t < t_e:
        print(t, y, x)
        #print(y, x)
        t += dt
        y = y_s + int((y_e - y_s) / (t_e - t_s) * (t - t_s))
        x = x_s + int((x_e - x_s) / (t_e - t_s) * (t - t_s))
    print("--------------------")
print(p[n-1][1], p[n-1][2])