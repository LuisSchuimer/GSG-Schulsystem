__autor__ = "Luis Schuimer"
from time import sleep
import socket
import keyboard
# Imports

def menu(username):

    print(f"""
     _____________________
    |🅶🆂🅶-🆂🅲🅷🆄🅻-🆂🆈🆂🆃🅴🄼 |
     ---------------------
    school and education
    Simply better!

    Übersichtsseite:
    Konto:
    {username}

    """)
    if fail_c == False:
        print(f"""
    ----------------Corona---Deutschland----
    Fälle: {cases}
    Tode: {deaths}
    Wöchendliche Insidenz: {weekIncidence}
    Fälle pro 100k: {casesPer100k}
    Letztes Update: {lastUpdate}

    Quelle: Robert Koch Institut
    ----------------------------------------
        """)
    else:
        print(f"""
    ----------------Corona---Error!----
    Dateien konnten nicht geladen werden!
    {error}
    {details}
    -----------------------------------
        """)

    print("""
    Alle deine Fächer:
    --------------------
    A. Deutsch
    B. ITG (Informatik)
    C. Mathe
    D. LZD
    E. Wirdschaft und Politik
    F. Erdkunde
    G. Geschichte
    H. AG
    I. Französich
    J. Englisch

    -----------------
    Anwendungen:
    L. Timer 

    (K). Alle Anwendungen

     _________________________! Wichtig !_____________________
    |Weitere Fächer werden mit weiteren Updates nachgereicht! |
     ---------------------------------------------------------
    --------------------
    """)

    action = input("AKTION] ")
    if action == "L":
        import time
        import datetime

        # Create class that acts as a countdown
        def countdown(h, m, s):
            cls()
            total_seconds = h * 3600 + m * 60 + s
            print(f"""
            |----------------| 
            |Timer           |
            | GSG-SYSTEM     |
            |----------------|


            """)

            # Calculate the total number of seconds

            # While loop that checks if total_seconds reaches zero
            # If not zero, decrement total time by one second
            while total_seconds > 0:
                timer = datetime.timedelta(seconds=total_seconds)
                # Timer represents time left on countdown

                # Prints the time left on the timer
                print(timer, end="\r")

                # Delays the program one second
                time.sleep(1)

                # Reduces total time by one second
                total_seconds -= 1

            print("Hey, der Timer ist abgelaufen!")
            sleep(2)
            menu(username)


        # Inputs for hours, minutes, seconds on timer
        h = input("Gebe die Stunden des Timers ein: ")
        m = input("Gebe die Minuten des Timers ein: ")
        s = input("Gebe die Sekunden des Timers ein: ")
        countdown(int(h), int(m), int(s))

def login():
    if keyboard.is_pressed("S"):
        print("")
    username = os.getlogin()
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        h_name = socket.gethostname()
        IP_addres = socket.gethostbyname(h_name)
        print(f"Logging in with {os.getlogin()}...")
        sleep(1)
        client_socket.connect(("192.168.178.31", 10))
        client_socket.send(bytes(username, "utf8"))
        sleep(1)
        client_socket.send(bytes(h_name, "utf8"))
        sleep(1)
        client_socket.send(bytes(IP_addres, "utf8"))
        cls()
    except:
        print("Server is not avariable at that time!")
        sleep(1)
        cls()
        menu(username)
import os
import requests
# Variables
Version = 0.5
url = "https://api.corona-zahlen.org/germany"
fail_c = False
# Start-functions
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Intro

print("           ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
cls()
print("          ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
cls()
print("         ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
cls()
print("        ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
cls()
print("       ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
cls()
print("      ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
cls()
print("     ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
cls()
print("    ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
cls()
print("   ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
cls()
print("  ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
cls()
print(" ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
cls()
print("▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
cls()
import datetime

x = datetime.datetime.now().strftime("%Y")


print(f"""
 _____________________
|🅶🆂🅶-🆂🅲🅷🆄🅻-🆂🆈🆂🆃🅴🄼 |
 ---------------------
school and education
Simply better!

©2020-{x} LUIS SCHUIMER (GSG-VELBERT)
All rights reserved
Version: {Version}
""")
sleep(3)
# Startup begins here:
print("Startup...")
for i in range(101):
    print("Loading data...")
    if i == 20:
        print("Getting Corona-Information from Robert Koch Institut...")
        data = requests.get(url).json()
        sleep(3)
        print("Writing Informations...")
        try:
            cases = data["cases"]
            deaths = data["deaths"]
            weekIncidence = data["weekIncidence"]
            source = data["meta"]["source"]
            casesPerWeek = data["casesPerWeek"]
            casesPer100k = data["casesPer100k"]
            newcases = data["delta"]["cases"]
            newdeaths = data["delta"]["deaths"]
            recovered = data["delta"]["recovered"]
            lastUpdate = data["meta"]["lastUpdate"]
            contact = data["meta"]["contact"]
            info = data["meta"]["info"]
            casesPer100k = round(casesPer100k, 0)
        except:
            error = data["error"]["message"]
            details = data["error"]["stack"]
            fail_c = True

    cls()
    print(f"{i}%")
    if i > 80:
        print("Clean up!...")
sleep(2)


print("Startup finished...")
sleep(1)
cls()

# Startup ends here!

login()







