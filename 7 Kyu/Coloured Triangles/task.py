def triangle(row):
    while len(row) > 1:
        new_row = ""
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                new_row += row[i]
            else:
                new_row += list(set("RGB").difference(row[i] + row[i + 1]))[0]
        row = new_row
    return row


# ----------------------------------------------------------------------------------------------------------------------

print(triangle('RGBG') == 'B')
print(triangle('RGBG'))
print(triangle('RBRGBRB') == 'G')
print(triangle('RBRGBRB'))
