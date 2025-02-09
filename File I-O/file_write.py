import csv
name = input("What's your name? ")
house = input("What house are you in? ")

with open("file_write.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow((name, house))