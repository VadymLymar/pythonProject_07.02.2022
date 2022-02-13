x = 123456
y = 0
print('Дані:', x)
while x > 0:
    digit = x % 10
    x = x // 10
    y = y * 10
    y = y + digit

print('Результат:',  y)
