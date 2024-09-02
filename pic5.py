query = f'insert into {filename} ({titles[0]}, {titles[1]}, {titles[2]}, {titles[3]}, {titles[4]}, {titles[5]}, {titles[6]}, {titles[7]}) values (%s, %s, %s, %s, %s, %s, %s, %s)'

for row in sheet.iter_rows(min_row=2, values_only=True):

    values = []
    for cell in row:
        values.append(cell)

    cur.execute(query, values)

    connection.commit()

    cur.close()

    connection.close()

path = ".\excel\"

files = os.listdir(path)

for file in files:
    if not (".~lock" in file or "_data" not in file):
        print("Processing file: " + file)
        filename = file.replace(".xlsx", "")
        exToTable(filename)