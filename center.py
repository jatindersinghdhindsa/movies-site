import fresh_tomatoes
import media

nj = media.Movie("Nikka Zaildar","ammy","https://upload.wikimedia.org/wikipedia/en/0/03/Nikka_Zaildar_First_Look_Poster.jpg","https://www.youtube.com/watch?v=AlpSxOWN9HU") 


dangal = media.Movie("Dangal"," awesome ","https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg","https://www.youtube.com/watch?v=x_7YlGv9u1g")


rangon= media.Movie("Rangoon","saif ali","https://upload.wikimedia.org/wikipedia/en/b/b3/RangoonPoster.jpg","https://www.youtube.com/watch?v=B-tC0wcIu24")


jagga = media.Movie("Jagga Jassos ","ranbit","https://upload.wikimedia.org/wikipedia/en/9/94/JaggaJasoosPoster.jpg","https://www.youtube.com/watch?v=zBobLhXFBio") 

llb = media.Movie("Jolly LLB 2s","akshay kumar ","https://upload.wikimedia.org/wikipedia/en/4/4b/Jolly_LLB_2_first_look.jpg","https://www.youtube.com/watch?v=kvjxoBG5euo")

movies=[nj,dangal,rangon,jagga,llb]

fresh_tomatoes.open_movies_page(movies)

