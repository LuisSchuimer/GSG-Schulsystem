__autor__ = "Luis Schuimer"
# Imports

import os
from time import sleep
from bs4 import BeautifulSoup
import requests
# Variables
Version = 0.1
url = "https://api.corona-zahlen.org/germany"
fail_c = False
# Start-functions
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Intro

print("           ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
sleep(0.01)
cls()
print("          ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
sleep(0.01)
cls()
print("         ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
sleep(0.01)
cls()
print("        ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
sleep(0.01)
cls()
print("       ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
sleep(0.01)
cls()
print("      ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
sleep(0.01)
cls()
print("     ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
sleep(0.01)
cls()
print("    ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
sleep(0.01)
cls()
print("   ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
sleep(0.01)
cls()
print("  ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
sleep(0.01)
cls()
print(" ▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
sleep(0.01)
cls()
print("▟▛▜▟▛▜▟▛ 🄶🅂🄶-🅂🄲🄷🅄🄻-🅂🅈🅂🅃🄴🄼 ▟▛▜▟▛▜▟▛")
sleep(0.01)
cls()
print(f"""
 _____________________
|🅶🆂🅶-🆂🅲🅷🆄🅻-🆂🆈🆂🆃🅴🄼 |
 ---------------------
school and education
Simply better!

©2020-2021 LUIS SCHUIMER (GSG-VELBERT)
All rights reserved
Version: {Version}
""")
sleep(3)
# Startup begins here:
print("Startup...")
sleep(2)
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

print("Startup finished...")
sleep(1)
cls()
# Startup ends here!
# Main (Menu)
print(f"""
 _____________________
|🅶🆂🅶-🆂🅲🅷🆄🅻-🆂🆈🆂🆃🅴🄼 |
 ---------------------
school and education
Simply better!

Übersichtsseite:

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

(K). Alle Anwendungen

 _________________________! Wichtig !_____________________
|Weitere Fächer werden mit weiteren Updates nachgereicht! |
 ---------------------------------------------------------
--------------------
""")

sleep(200)

