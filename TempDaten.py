import matplotlib.pyplot as plt


Temp = open("TempDaten.txt", "r")
temp = []
temp_time = []


for i in range(11):
    line = float(Temp.readline())
    temp.append(line)
Temp.close()
for i in range(11):
    if i != 10:
        plt.text((24 * 60 * 60 * i)+1000, 5.4, str(19 + i) + ".11.2022")
    temp_time.append((24 * 60 * 60 * i))
    plt.axvline(x=temp_time[i], color='g')
    print(temp[i])
    plt.hlines(y=temp[i], xmin=(24 * 60 * 60 * i), xmax=(24 * 60 * 60 * (i+1)), color='r')
plt.xlabel('Zeit')
plt.ylabel('Temperatur in °C')
plt.title('Durchschnittliche Temperatur zwischen 19.11.2022 und 28.11.2022')

plt.show()
