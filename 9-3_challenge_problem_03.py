import csv

title01 = ["Top Gun", "Risky Business", "Minority Report"]
title02 = ["Titanic", "The Revenant", "Inception"]
title03 = ["Training Day", "Man on Fire", "Flight"]

with open("movie_list.csv", "w", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(title01)
    w.writerow(title02)
    w.writerow(title03)

