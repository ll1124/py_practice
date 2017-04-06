fo = open("/home/jinkyu/Desktop/coding/py/sess03_data.txt", "r")

# print(fo.tell())
# data_byte = fo.readline()
# print(data_byte)
#
# print(fo.tell())
# data_byte = fo.readline()
# print(data_byte)
#
# print(fo.tell())
# data_byte = fo.readline()
# print(data_byte)
#
# fo.seek(0)
#
# print(fo.tell())
# data_byte = fo.readline()
# print(data_byte)

line1 = fo.readline()
line2 = fo.readline()

# line1 = line1.decode("utf-8")

# line1 = line1[0:-1]

line1_split = line1.split(',')
line1_ls = []

for i in line1_split:
    line1_ls.append(int(i))

print(line1_ls)

line2_split = line2.split(',')
line2_ls = []

for i in line2_split:
    line2_ls.append(int(i))

print(line2_ls)
import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot
print(matplotlib.pyplot)


matplotlib.pyplot.plot(line1_ls, line2_ls)
matplotlib.pyplot.show()
