import matplotlib.pyplot as plt

t_log = 0
c = []
t = []
t_numvalue = []
f = open("OzonDaten.txt", "r")
count = True
counter = 0
platzhalter_t = 0
vari = 999


def integer_to_time_stamp(time_as_integer):
    hours = time_as_integer // 3600
    remaining_seconds = time_as_integer % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    time_stamp = f"{hours:02d}:{minutes:02d}:{seconds:02d}.000"
    return time_stamp


def time_as_integer(time_stamp):
    time_stamp_parts = time_stamp.split(":")
    hours = int(time_stamp_parts[0])
    minutes = int(time_stamp_parts[1])
    seconds_and_milliseconds = time_stamp_parts[2]
    seconds = seconds_and_milliseconds.split(".")
    seconds = int(seconds[0])
    return hours * 3600 + minutes * 60 + seconds


while count == True:
    line = f.readline()
    if line[0:4] == "Stop":
        count = False
        break
    platzhalter_t = int(line[0:2])
    platzhalter_tmin = line[2:8]
    if vari == 23 and vari != platzhalter_t:
        t_log += 1
    vari = platzhalter_t
    platzhalter_t += (24 * t_log)
    t.append(str(platzhalter_t) + platzhalter_tmin)
    t_numvalue.append(time_as_integer(t[counter]))
    c.append(float(line[35:40]))
    counter += 1
print(t_log)
t_labels = []
t_labelsnum = []
daysit = 0
for i in range(20):
    if daysit == 1:
        t_labels.append(integer_to_time_stamp(12 * 60 * 60)[0:5])
        daysit = 0
    else:
        t_labels.append(integer_to_time_stamp(24 * 60 * 60)[0:5])
        daysit = 1
    t_labelsnum.append(12 * 60 * 60 * i)
f.close()
plt.xlabel('Time')
plt.ylabel('Ozone concentration in ppb')
plt.title('Ozone concentration over time')
plt.plot(t_numvalue, c, marker=',', color='b')

plt.xticks(t_labelsnum, t_labels)
# plt.gcf().autofmt_xdate()
dayline = []
for i in range(10):
    dayline.append(24 * 60 * 60 * i)
    plt.axvline(x=dayline[i], color='r')
plt.xticks(fontsize=14)
plt.xticks(rotation=90)
#plt.savefig("Ozonplot.png") #Wenn jemand den Graph speichern möchte, bitte das "#" löschen
plt.show()
