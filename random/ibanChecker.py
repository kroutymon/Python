'''
IBAN = input("DE54720501010030751705")

#DE54720501010030751705
#DE81500105174953777388




laendercode = IBAN[:2]
pruefziffer = IBAN[2:4]
blz = IBAN[4:12]
kontonummer = IBAN[12:].zfill(10)

check = str(98 - int(blz + kontonummer + "131400")%97).zfill(2)

if check == pruefziffer:
    print("korrekt")
else:
    print("falsch")
'''


iban = input("IBAN: DE")

#
laendercode = iban[:2]
pruefziffer = iban[2:4]
blz = iban[4:12]
konntonr = iban[12:].zfill(10)

check = str(98 - int(blz + konntonr + "131400") %97).zfill(2)

if check == pruefziffer:
    print("Die IBAN ist korekt!")
else:
    print("Die IBAN ist falsch!")