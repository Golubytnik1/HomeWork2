#dz - 16.11.2022

data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []

for i in data:
    if i[0] == "0":
        codes.append(i)
    else:
        designations.append(i)

x = 0
operators = {}
while len(operators) != len(designations):
    operators[designations[x]] = {codes[x]}
    x += 1

deleted = operators.pop('Katel')
deleted = operators.pop('Fonex')
operators["O!"].add("0700")
operators["O!"].add("0500")
operators["Megacom"].add("0999")
operators["Megacom"].add("0555")
operators["Beeline"].add("0222")
operators["Beeline"].add("0777")

for k, v in operators.items():
    print(f'{k} - {v}')

