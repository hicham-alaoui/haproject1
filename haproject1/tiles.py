#import the main python file that will help generate the index.html file.
import tiles_page

#import the media file with the main class and variable information.
import media

# Add the movies details to match the constructor data; in other words the class variables.
hideous_kinky = media.Trailers("Hideous Kinky", "http://img.moviepostershop.com/hideous-kinky-movie-poster-1999-1010349794.jpg", "https://youtu.be/Db68gSckUU0")

up = media.Trailers("Up", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtzUBKeCoz5G5bS48g-bAUG_AorBExMGHNgYlQvEMUVUTQU2beFw", "https://youtu.be/qas5lWp7_R0")

indigenes = media.Trailers("Indigenes", "http://www.impawards.com/2007/posters/days_of_glory.jpg", "https://youtu.be/6_EuwDYfA-M")

#Define the list of movies/tarilers you wull be using by creating an array.
tiles = [hideous_kinky, up, indigenes]

#Use the function trailers_page in the main python page to fire the generated html file to the the local server. 

tiles_page.trailers_page(tiles)

