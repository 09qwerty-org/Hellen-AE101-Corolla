import csv

bomName = "AE101Corolla-a-BOM-JLC.csv"
componentCount = []

with open(bomName, 'r', newline='') as BOM:
    rows = list(csv.reader(BOM))
    for col in rows:
        componentCount.append(col[1].count(",") + 1)

del componentCount[0]
max_cols = max(len(row) for row in rows)

for row in rows:
    while len(row) < max_cols:
        row.append("")

for row in rows:
    row.append("")

rows[0][-1] = "Count"

for i, count in enumerate(componentCount, start=1):
    if i >= len(rows):
        rows.append([""] * len(rows[0]))
    rows[i][-1] = count

with open(bomName, 'w', newline='') as BOM:
    writer = csv.writer(BOM)
    writer.writerows(rows)
