#等差数列
start = float(input("Input start\n"))
end = float(input("Input end\n"))
step = float(input("Input step\n"))
i = start
sum = 0.0
while i <= end:
    sum += i
    i += step
print(sum)