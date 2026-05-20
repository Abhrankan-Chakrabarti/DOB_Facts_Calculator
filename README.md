# DOB_Facts_Calculator

DOB_Facts_Calculator is a Python script that generates a detailed, personalised fact sheet from your date of birth — covering everything from numerology and astrology to sleep stats and birthday countdowns.

## Features

- **Life path number** — reduces your full birth date digits to a single digit (or master numbers 11, 22, 33) using numerology
- **Zodiac sign, ruling planet, birthstone & birth flower** — determined from your birth month and day
- **Generation label** — classifies your birth year (e.g. Gen Z, Gen Alpha, Boomers I/II, Post War, WWII)
- **Exact age** — broken down into years, months, days, hours, and minutes
- **Days, hours & minutes lived** — total counts since birth, formatted with commas
- **Full moon count** — estimated number of full moons since your birth date
- **Billionth second milestone** — the exact date you hit (or will hit) 1,000,000,000 seconds old
- **Next birthday countdown** — days remaining, and the weekday of your next two birthdays
- **Calendar reuse year** — the next year whose calendar is identical to your birth year
- **Sleep statistics** — estimated time spent sleeping (assuming 8 hours/day), in years, months, weeks, and days
- **Log file output** — optionally saves the full output to a `.txt` file via a command-line flag

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/Abhrankan-Chakrabarti/DOB_Facts_Calculator.git
    ```
2. Navigate to the repository directory:
    ```bash
    cd DOB_Facts_Calculator
    ```
3. Run the script:
    ```bash
    python DOB.py
    ```
4. Optionally, save the output to a log file:
    ```bash
    python DOB.py -l
    # or specify a custom filename:
    python DOB.py -l my_facts.txt
    ```

## Example

When you run the script, you will be prompted to enter your date of birth:

```
Enter Your Date of Birth (DD/MM/YYYY):
```

The script then prints a full fact sheet including your zodiac sign, life path number, exact age, billionth second date, next birthday countdown, sleep statistics, and more.

## Requirements

- Python 3.x (no third-party dependencies — uses only the standard library)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

This script was created by [Abhrankan Chakrabarti](https://github.com/Abhrankan-Chakrabarti).
