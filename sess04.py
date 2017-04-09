def coin(value=0):

    coin1 = 500
    coin2 = 300
    coin3 = 100

    five = value // coin1

    value -= coin1 * five

    three = value // coin2
    value -= coin2 * three

    one = value // coin3

    return f"{five}, {three}, {one}"


value = 2500

print(coin(value))

c = [1,2,3,[1,2,3,[5]]]
ls_index = c[3][3][0]
print(ls_index)


for value in range(20): print("*")

b = [4,5,4,5,6,3]
result = 0

for value in b: result += value
print(result)


h = 5
a = " "
b = "*"
for value in range(h+1):
    if value == 0:
        pass
    else:
        space = a * (h - value)
        star = (value * 2 - 1) * b
        print(space + star)
