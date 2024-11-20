import bs4
import requests
raw_site= requests.get("https://www.empireonline.com/movies/features/best-movies-2/").text
movies = bs4.BeautifulSoup(raw_site, "html.parser")
movies_list = []
new_k = ""
for m in (movies.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")):
    movie_title = ""
    new_k = ""
    movie_data2 = m.text
    movie_data3 = movie_data2.split()
    movie_data4 = movie_data3[1:]
    for word in movie_data4:
        movie_title += word + " "
    movies_list.append(movie_title)


with open("processed_list.txt", "w") as text_file:
    for n in range(len(movies_list)):
        new_line_text = str(n + 1) + " - " + movies_list[-(n)] + "\n"
        text_file.write(new_line_text)

print(movies_list)