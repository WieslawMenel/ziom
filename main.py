import csv
import random


file = open("zlom_dane.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print("wczytano:")
print(header)
data = []
for row in csvreader:
    data.append(row)
print(data)
file.close()


with open('zlom.csv', 'w') as file:
    writer = csv.writer(file)
    for i in range(100):

        numer=random.randint(0, len(data)-1)
        datai = [data[numer][0],
                 random.randint(int(data[numer][1]), int(data[numer][2])),
                 random.randint(int(data[numer][3]), int(data[numer][4]))]
        writer.writerow(datai)
file.close()

