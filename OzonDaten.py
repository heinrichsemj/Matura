import matplotlib.pyplot as plt


t_log = 0
c = []
time = []
time_numvalue = []
Ozon = open("OzonDaten.txt", "r")
count = True
counter = 0
platzhalter_t = 0
vari = 999
time_labels = []
time_labelsnum = []
daysit = 0
dayline = []

def integer_to_time_stamp(time_as_integer):
    hours = time_as_integer // 3600
    remaining_seconds = time_as_integer % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    time_stamp = f"{hours:02d}:{minutes:02d}:{seconds:02d}.000"
    return time_stamp


def time_stamp_to_integer(time_stamp):
    time_stamp_parts = time_stamp.split(":")
    hours = int(time_stamp_parts[0])
    minutes = int(time_stamp_parts[1])
    seconds_and_milliseconds = time_stamp_parts[2]
    seconds = seconds_and_milliseconds.split(".")
    seconds = int(seconds[0])
    return hours * 3600 + minutes * 60 + seconds


while count == True: #Ozon Daten lesen
    line = Ozon.readline()
    if line[0:4] == "Stop":
        count = False
        break
    platzhalter_t = int(line[0:2])
    platzhalter_tmin = line[2:8]
    if vari == 23 and vari != platzhalter_t:
        t_log += 1
    vari = platzhalter_t
    platzhalter_t += (24 * t_log)
    time.append(str(platzhalter_t) + platzhalter_tmin)
    time_numvalue.append(time_stamp_to_integer(time[counter]))
    c.append(float(line[35:40]))
    counter += 1



for i in range(20):
    if daysit == 1:
        time_labels.append(integer_to_time_stamp(12 * 60 * 60)[0:5])
        daysit = 0
    else:
        time_labels.append(integer_to_time_stamp(24 * 60 * 60)[0:5])
        daysit = 1
    time_labelsnum.append(12 * 60 * 60 * i)

Ozon.close()

## Graph Details


plt.xlabel('Zeit')
plt.ylabel('Ozon Konzentration in parts per billion (ppb)')
plt.title('Ozon Konzentration zwischen 19.11.2022 und 28.11.2022')
plt.plot(time_numvalue, c, marker=',', color='b')
plt.xticks(time_labelsnum, time_labels)
for i in range(11):
    if i != 10:
        plt.text((24 * 60 * 60 * i)+1000, 60, str(19 + i) + ".11.2022")
    dayline.append(24 * 60 * 60 * i)
    plt.axvline(x=dayline[i], color='g')
plt.xticks(fontsize=14)
plt.xticks(rotation=90)
plt.savefig("Ozonplot.png")
plt.show()
