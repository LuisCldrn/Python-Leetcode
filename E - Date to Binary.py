def convertdate(date: str):
    date = date.split("-")
    return f'{bin(int(date[0]))[2:]}-{bin(int(date[1]))[2:]}-{bin(int(date[2]))[2:]}'

print(convertdate('1900-01-01'))