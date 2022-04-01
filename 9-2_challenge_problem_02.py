answer = input("What is your favorite movie?:")

with open("fav_movie.txt", "w", encoding="utf-8") as f:
    f.write(answer)

