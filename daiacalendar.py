from dataclasses import dataclass
from datetime import datetime
import time

@dataclass
class DaiaDateTime:
    cycle:          int = 0     # currently 35th (so this should be 34 for positive Unix times)
    yearInCycle:    int = 0     # 1-143
    yearAbsolute:   int = 0
    dayAbsolute:    int = 0     # 1-549
    wheel1Count:    int = 0     # 1-33 (429 days)
    wheel1Name:     int = 0     # 1-13
    wheel2Count:    int = 0     # 1-61 (549 days)
    wheel2Name:     int = 0     # 1-9
    nata:           int = 0     # 0-15
    qaren:          int = 0     # 0-71
    dhagia:         float = 0.0 # 0.0-71.9

now = time.time()
nowReadable = time.ctime(now)

year = (now / 72000 // 549)
day = (now // 72000) % 549

d = DaiaDateTime(int(35 if now >= 0 else 34),
                 int(year),
                 int(((34 if now >= 0 else 33) * 143) + year),
                 int(day),
                 int(day % 33),
                 int(day % 13),
                 int(day % 61),
                 int(day % 9),
                 int((now // 4500) % 16),
                 int((now // 62.5) % 72),
                 (now * 69.12 / 60) % 72)

def DaiaPrint(d):
    print("year:", year)
    print("day", day)
    print(d.cycle, d.yearInCycle, d.yearAbsolute, d.dayAbsolute, d.wheel1Count, d.wheel1Name, d.wheel2Count, d.wheel2Name)
    gemNames = ['Mau', 'Lòđríř', 'Áradî', 'Nenálû', 'Rŷmňû', 'Řalídam', 'Kànâja', 'Térezî', 'Volánsikhai', 'Kuja', 'Còwì', 'Neital', 'Súvâri']
    colorNames = ['Sajúmas', 'Cavartûs', 'Âfełaris', 'Mátsunas', 'Basîres', 'Menaós', 'Ìtreus', 'Ávris', 'Îceilis']
    return " ".join(["On Daia, today is", str(d.wheel1Count + 1), gemNames[int(d.wheel1Name)], str(d.wheel2Count + 1), colorNames[int(d.wheel2Name)], "year", str(d.yearInCycle + 1), "of cycle", str(d.cycle), "(", str(d.yearAbsolute + 1), ")", "time", "{0:02d}".format(d.nata), ";", "{0:02d}".format(d.qaren), ";", "{0:02.1f}".format(d.dhagia)])

print(DaiaPrint(d))
print("On Earth, today is " + nowReadable)