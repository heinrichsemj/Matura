import matplotlib.pyplot as plt

##Variabeln und Listen
t_log = 0
c = []
t = []
t_numvalue = []
f = open("OzonDaten.txt", "r")
count = True
counter = 0
platzhalter_t = 0
vari = 999
t_labels = []
t_labelsnum = []
daysit = 0
dayline = []


def integer_to_time_stamp(time_as_integer): #eine Zahl zu Time stamp
    hours = time_as_integer // 3600
    remaining_seconds = time_as_integer % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    time_stamp = f"{hours:02d}:{minutes:02d}:{seconds:02d}.000"
    return time_stamp


def time_as_integer(time_stamp): #time stamp zu einer Zahl
    time_stamp_parts = time_stamp.split(":")
    hours = int(time_stamp_parts[0])
    minutes = int(time_stamp_parts[1])
    seconds_and_milliseconds = time_stamp_parts[2]
    seconds = seconds_and_milliseconds.split(".")
    seconds = int(seconds[0])
    return hours * 3600 + minutes * 60 + seconds


while count == True: #Daten aus 'OzonDaten.txt' lesen
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
   

for i in range(20): #Beschriftung der X-Achse (Zeit) verändern
    if daysit == 1:
        t_labels.append(integer_to_time_stamp(12 * 60 * 60)[0:5])
        daysit = 0
    else:
        t_labels.append(integer_to_time_stamp(24 * 60 * 60)[0:5])
        daysit = 1
    t_labelsnum.append(12 * 60 * 60 * i)
    
    
f.close()
plt.xlabel('Zeit')
plt.ylabel('Ozon Konzentration in parts per billion (ppb)')
plt.title('Ozon Konzentration zwischen 19.11.2022 und 28.11.2022')
plt.plot(t_numvalue, c, marker=',', color='b')
plt.xticks(t_labelsnum, t_labels)

for i in range(10): #Vertikale Linien und Datum einfügen
    plt.text((24 * 60 * 60 * i)+1000, 60, str(19 + i) + ".11.2022")
    dayline.append(24 * 60 * 60 * i)
    plt.axvline(x=dayline[i], color='r')
plt.xticks(fontsize=14)
plt.xticks(rotation=90)

#plt.savefig("Ozonplot.png") #Wenn jemand den Graph speichern möchte, bitte das "#" löschen
plt.show()
