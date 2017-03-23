# import the main python file that will help generate the index.html file.
import tiles_page

# import the media file with the main class and variable information.
import media

# Add the movies details to match the constructor class variables.
hideous_kinky = media.Trailers("Hideous Kinky", "https://goo.gl/lKsHKE",
                               "https://youtu.be/Db68gSckUU0")

up = media.Trailers("Up", "https://goo.gl/L3ndLp",
                    "https://youtu.be/qas5lWp7_R0")

indigenes = media.Trailers("Indigenes", "https://goo.gl/E987Ei",
                           "https://youtu.be/6_EuwDYfA-M")

# Define the list of movies/tarilers you wull be using by creating an array.
tiles = [hideous_kinky, up, indigenes]

# Use the function trailers_page to fire the generated html file.

tiles_page.trailers_page(tiles)
