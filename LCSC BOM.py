import csv
from pathlib import Path

filename = Path('boards/AE101Corolla-a/board') / 'AE101Corolla-a-BOM-JLC.csv'
with open(filename, 'r', newline='') as f:
    rows = list(csv.reader(f))
for row in rows:
    while len(row) < 5:
        row.append("")
rows[0][4] = "Quantity"

#count quantity via commas
for i in range(1, len(rows)):
    col2_value = rows[i][1] if len(rows[i]) > 1 else ""
    comma_count = col2_value.count(",")
    quantity = comma_count + 1
    rows[i][4] = quantity

#write quantities moving down
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
