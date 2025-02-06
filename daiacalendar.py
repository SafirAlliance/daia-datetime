from dataclasses import dataclass
from datetime import datetime, timezone
import time

CONST_SECS_PER_YEAR = CONST_DAYS_PER_YEAR * CONST_SECS_PER_DAY
CONST_YEARS_PER_CYCLE = 143
CONST_SECS_PER_DAY = 72000
CONST_DAYS_PER_YEAR = 549
CONST_SECS_PER_NATA = 4500
CONST_SECS_PER_QAREN = 62.5
CONST_DHAGIAI_PER_SECOND = 69.12 / 60

@dataclass
class DaiaDateTime:
    def __init__(self, secs):
        self.secs = secs
        self.years, r = divmod(secs, CONST_SECS_PER_YEAR)
        self.cycles = 34 if secs >= 0 else 33
        self.yearsAbsolute = (self.cycles * CONST_YEARS_PER_CYCLE) + self.years
        self.days, r = divmod(r, CONST_SECS_PER_DAY)
        self.daysAbsolute = (self.years * CONST_DAYS_PER_YEAR) + self.days
        self.natai, r = divmod(r, CONST_SECS_PER_NATA)
        self.qarenaw, r = divmod(r, CONST_SECS_PER_QAREN)
        self.dhagiai = r * CONST_DHAGIAI_PER_SECOND
    def __str__(self):
        gemNames = ['Mau', 'Lòđríř', 'Áradî', 'Nenálû', 'Rŷmňû', 'Řalídam', 'Kànâja', 'Térezî', 'Volánsikhai', 'Kuja', 'Còwì', 'Neital', 'Súvâri']
        colorNames = ['Sajúmas', 'Cavartûs', 'Âfełaris', 'Mátsunas', 'Basîres', 'Menaós', 'Ìtreus', 'Ávris', 'Îceilis']
        wheel1Count = d.daysAbsolute % 33
        wheel1Name = gemNames[int(d.daysAbsolute % 13)]
        wheel2Count = d.days % 61
        wheel2Name = colorNames[int(d.days % 9)]
        wheels = " ".join([str(int(wheel1Count + 1)), wheel1Name, str(int(wheel2Count + 1)), wheel2Name])
        yearList = " ".join(["year", str(int(d.years + 1)), "of the", ordinal(d.cycles + 1), "cycle"])
        time = ";".join(["{0:02d}".format(int(d.natai)), "{0:02d}".format(int(d.qarenaw)), "{0:02.1f}".format(d.dhagiai)])
        return " ".join(["On Daia, today is", wheels, yearList, "and Aran Mean Time is", time])

now = time.time()
nowReadable = time.ctime(now)
nowUniversal = datetime.now(timezone.utc)

year = (now / CONST_SECS_PER_DAY // CONST_DAYS_PER_YEAR)
day = (now // CONST_SECS_PER_DAY) % CONST_DAYS_PER_YEAR

d = DaiaDateTime(time.time())

def ordinal(n):
    suffix = {1:'st', 2:'nd', 3:'rd', 11:'th', 12:'th', 13:'th' }
    return str(n)+(suffix.get(n%100) or suffix.get(n%10,'th'))

print(d)
print("Your local time: " + nowReadable)
print("UTC: " + str(nowUniversal))