import sys
from calendar import leapdays, monthrange
from datetime import datetime
from math import ceil


def format_number(n, sep=",", f=""):
    """Returns a number string, properly formatted with commas."""
    n, l = f"{n}", -len(f"{n}")
    for i in range(-1, l - 1, -1):
        f += n[i] + sep if i % 3 == 0 and i - l else n[i]

    def reverse_string(xyz, rev=""):
        for i in range(len(xyz) - 1, -1, -1):
            rev += xyz[i]
        return rev

    return reverse_string(f)


def generation(born):
    if born > 2012:
        return "Generation Alpha"
    if born > 1996:
        return "Generation Z"
    if born > 1980:
        return "Generation X"
    if born > 1964:
        return "Boomers II"
    if born > 1954:
        return "Boomers I"
    if born > 1945:
        return "Post War"
    if born > 1927:
        return "WWII"


def lpn(n):
    return n if n < 10 or n in (11, 22, 33) else lpn(n // 10 + n % 10)


def suffix(n):
    if n % 10 not in (1, 2, 3) or n % 100 in (11, 12, 13):
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}[n % 10]


def zodiac_sign(day, month):
    # checks month and date within the valid range
    # of a specified zodiac
    if month == "December":
        astro_sign = (
            ("Sagittarius", "Jupiter") if (day < 22) else ("Capricorn", "Saturn"),
            "Holly",
            "Turquoise, Tanzanite and Zircon",
        )

    elif month == "January":
        astro_sign = (
            ("Capricorn", "Saturn") if (day < 20) else ("Aquarius", "Uranus"),
            "Carnation",
            "Garnet",
        )

    elif month == "February":
        astro_sign = (
            ("Aquarius", "Uranus") if (day < 19) else ("Pisces", "Neptune"),
            "Violet",
            "Amethyst",
        )

    elif month == "March":
        astro_sign = (
            ("Pisces", "Neptune") if (day < 21) else ("Aries", "Mars"),
            "Daffodil",
            "Aquamarine and Bloodstone",
        )

    elif month == "April":
        astro_sign = (
            ("Aries", "Mars") if (day < 20) else ("Taurus", "Venus"),
            "Daisy",
            "Diamond",
        )

    elif month == "May":
        astro_sign = (
            ("Taurus", "Venus") if (day < 21) else ("Gemini", "Mercury"),
            "Lily of the Valley",
            "Emerald",
        )

    elif month == "June":
        astro_sign = (
            ("Gemini", "Mercury") if (day < 21) else ("Cancer", "The Moon"),
            "Rose",
            "Pearl, Moonstone and Alexandrite",
        )

    elif month == "July":
        astro_sign = (
            ("Cancer", "The Moon") if (day < 23) else ("Leo", "The Sun"),
            "Delphinium",
            "Ruby",
        )

    elif month == "August":
        astro_sign = (
            ("Leo", "The Sun") if (day < 23) else ("Virgo", "Mercury"),
            "Gladiolus",
            "Peridot, Spinel and Sardonyx",
        )

    elif month == "September":
        astro_sign = (
            ("Virgo", "Mercury") if (day < 23) else ("Libra", "Venus"),
            "Aster",
            "Sapphire",
        )

    elif month == "October":
        astro_sign = (
            ("Libra", "Venus") if (day < 23) else ("Scorpio", "Pluto"),
            "Marigold",
            "Opal and Tourmaline",
        )

    elif month == "November":
        astro_sign = (
            ("Scorpio", "Pluto") if (day < 22) else ("Sagittarius", "Jupiter"),
            "Chrysanthemum",
            "Topaz and Citrine",
        )

    return astro_sign[0] + astro_sign[1:]


print("This program prints some top facts about you from your date of birth.")
dmy = input("Enter Your Date of Birth (DD/MM/YYYY) :\t")
DOB = datetime.strptime(dmy, "%d/%m/%Y")
now = datetime.now()
date = now - DOB
days = date.days
secs = date.seconds
byear = DOB.year + 32
bmonth = DOB.month - 4
if bmonth < 1:
    bmonth += 12
    byear -= 1
j = byear % 4 == 0 and byear % 100 != 0 or byear % 400 == 0
n = (31, 28 + j, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[bmonth - 1]
bday = DOB.day + 7
if bday > n:
    bday -= n
    bmonth += 1
    if bmonth > 12:
        bmonth = 1
        byear += 1
bdate = datetime.strptime(f"{bday}/{bmonth}/{byear}", "%d/%m/%Y")
on = "was on" if bdate < now else "will happen sometime on"
bmonth = bdate.strftime("%B")
month = DOB.strftime("%B")
zodiac, planet, flower, stone = zodiac_sign(DOB.day, month)
weekday = DOB.strftime("%A")
yearday = (DOB - datetime.strptime(f"31/12/{DOB.year - 1}", "%d/%m/%Y")).days
weekdays = ceil(yearday / 7)
dayyear = 365.242
fage = days / dayyear
age = int(fage)
mage = int(days % dayyear / 30)
dage = int(days % dayyear % 30)
nextbyear = now.year
nextbdate = datetime.strptime(f"{DOB.day}/{DOB.month}/{nextbyear}", "%d/%m/%Y")
if nextbdate <= now:
    nextbyear += 1
    nextbdate = datetime.strptime(f"{DOB.day}/{DOB.month}/{nextbyear}", "%d/%m/%Y")
nextnextbdate = datetime.strptime(f"{DOB.day}/{DOB.month}/{nextbyear + 1}", "%d/%m/%Y")
nextbweekday = nextbdate.strftime("%A")
nextnextbweekday = nextnextbdate.strftime("%A")
nextbdaterem = nextbdate - now
nextbday = nextbdaterem.days
nextbsec = nextbdaterem.seconds
log = f"""

Date: {month} {DOB.day}, {DOB.year}

It was the {weekdays}{suffix(weekdays)} {weekday} of {DOB.year}. If you were born on this date your birthday numbers {DOB.month}, {DOB.day} and {DOB.year} reveal that your life path number is {lpn(int(dmy.replace('/', '')))}. Your zodiac sign is {zodiac} with a ruling planet {planet}, your birthstone is the {stone}, and your birth flower is the {flower}. You are {age} years old, and were born in {DOB.year // 10 * 10}s, in the middle of {generation(DOB.year)}. The generation you are born into makes an impact on your life. Swipe up to find out what it all means.



→ {month} {DOB.day}, {DOB.year} was a {weekday}

→ Zodiac sign for this date is {zodiac}

→ This date was {format_number(days)} days ago

→ In {nextbyear}, {month} {DOB.day} is on {nextbweekday}







View snazzy {month} {DOB.day}, {DOB.year} birthday facts that no one tells you about, such as your life path number, birthstone, ruling planet, zodiac sign and birth flower.



You have been alive for:



{age} Years {mage} Months {dage} Days {secs // 3600} Hours {secs % 3600 // 60} Minutes

People born on this day will turn {age + 1} in exactly {nextbday + 1} days.

If you were born on this date:

You have been alive for {format_number(days)} days. Your birth sign is {zodiac} with a ruling planet {planet}. There were precisely {format_number(int(days / 29.5))} full moons after you were born up to this day. Your billionth second {on} {bmonth} {bdate.day}, {bdate.year}.



→ You’ve slept {format_number(days // 3)} days or {round(fage / 3, 2)} years.

→ Your next birthday is {nextbday} days away

→ You’ve been alive {format_number(days // 30)} months

→ You have been alive {format_number(days * 24)} hours

→ You are {format_number(days * 1440)} minutes old

→ Age on next birthday: {age + 1} years old







You were born on a {weekday}

{month} {DOB.day}, {DOB.year} was the {weekdays}{suffix(weekdays)} {weekday} of that year. It was also the {yearday}{suffix(yearday)} day and {DOB.month}{suffix(DOB.month)} month of {DOB.year} in the Gregorian calendar. The next time you can reuse {DOB.year} calendar will be in {now.year + 14 - now.year % 14 + DOB.year % 14}. Both calendars will be exactly the same.



There are {nextbday + 1} days left before your next birthday. Your {age + 1}{suffix(age + 1)} birthday will be on a {nextbweekday} and a birthday after that will be on a {nextnextbweekday}. The timer below is a countdown clock to your next birthday.



Your next birthday is in:

{nextbday // 30} Months {nextbday % 30} Days {nextbsec // 3600} Hours {nextbsec % 3600 // 60} Minutes {nextbsec % 60} Seconds

Your next birthday is on a {nextbweekday}





You’ve slept 33% of your life!

Assuming you’ve been sleeping 8 hours daily since birth. Here is how much time you’ve spent sleeping so far:



You’ve slept {round(fage / 3, 2)} years of your life.

You’ve slept {days // 90} month of your life.

You’ve slept {format_number(days // 21)} week of your life.

You’ve slept {format_number(days // 3)} days of your life.
"""
print(log)
if sys.argv[1:2] in (["-l"], ["--log"]):
    with open(
        (sys.argv[2:3] or [f"{DOB.day} {month} {DOB.year} - Top 25 Facts.txt"])[0], "w"
    ) as f:
        f.write(log)
