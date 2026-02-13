import csv
bomName = "AE101Corolla-a-BOM-JLC.csv"
componentCount = []

with open(bomName, 'r', newline='') as BOM:
    for col in (csv.reader(BOM)):
        componentCount.append(col[1].count(",")+1)
        
print(componentCount)

with open(bomName, 'w', newline='') as BOM:
    csv.writer(BOM).writerow(["","","","","test"])
    
