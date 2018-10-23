import fresh_tomatoes
import media

#Dangal movie instance of class Movie
dangal=media.Movie("Dangal",
                   "Dangal is an extraordinary true story based on the life of Mahavir Singh and his two daughters, Geeta and Babita Phogat.",
                   "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
                   "https://www.youtube.com/watch?v=x_7YlGv9u1g")

#Munthirivallikal Thalirkkumbol movie instance of class Movie
munthirivallikal_thalirkkumbol=media.Movie("Munthirivallikal Thalirkkumbol",
                                           "Munthirivallikal_Thalirkkumbol is an upcoming Indian Malayalam domestic drama film directed by Jibu Jacob and written by M. Sindhuraj, loosely based on the Malayalam short story Pranayopanishath by V. J. James. Produced and distributed by Weekend Blockbusters of Sophia Paul, the film stars Mohanlal and Meena, respectively as Panchayat secretary Ulahannan and his wife Annyamma.",
                                           "https://upload.wikimedia.org/wikipedia/en/e/e4/Munthirivallikal_Thalirkkumbol_poster.jpg",
                                           "https://www.youtube.com/watch?v=8qHITluVfX8")

#Kattappanayile Rithwik Roshan movie instance of class Movie
kattappanayile_rithwik_roshan=media.Movie("Kattappanayile Rithwik Roshan",
                                          "Kattappanayile Rithwik Roshan (English: Rithwik Roshan of Kattappana) is a 2016 Indian Malayalam-language comedy film directed by Nadirshah. It stars Vishnu Unnikrishnan in the lead role.",
                                          "https://upload.wikimedia.org/wikipedia/en/7/7f/Kattappanayile_Rithwik_Roshan_film_poster.jpg",
                                          "https://www.youtube.com/watch?v=Ui4GDleZSRQ")

#Ezra movie instance of class Movie
ezra=media.Movie("Ezra",
                 "Ezra is an upcoming 2017 Indian Malayalam horror thriller film written and directed by Jay K, starring Prithviraj Sukumaran.[1] Major filming locations were Fort Kochi and Sri Lanka.",
                 "https://upload.wikimedia.org/wikipedia/en/7/74/Ezra_movie_poster.jpg",
                 "https://www.youtube.com/watch?v=4ecn22XHqHc")

#The Shawshank Redemption movie instance of class Movie
the_shawshank_redemption=media.Movie("The Shawshank Redemption",
                                     "The Shawshank Redemption is a 1994 American drama film written and directed by Frank Darabont, and starring Tim Robbins and Morgan Freeman. Adapted from the Stephen King novella Rita Hayworth and Shawshank Redemption, the film tells the story of Andy Dufresne, a banker who is sentenced to life in Shawshank State Penitentiary for the murder of his wife and her lover, despite his claims of innocence.",
                                     "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                     "https://www.youtube.com/watch?v=6hB3S9bIaco")

#Pulimurugan movie instance of class Movie
pulimurugan=media.Movie("Pulimurugan",
                        "Pulimurugan (English: Leopard-Murugan) is a 2016 Indian Malayalam-language action adventure film directed by Vysakh, starring Mohanlal in the titular role,[7] and co-stars Kamalini Mukherjee, Jagapati Babu, Bala, Lal, and Vinu Mohan.",
                        "https://upload.wikimedia.org/wikipedia/en/e/e1/Pulimurugan_film_poster.jpg",
                        "https://www.youtube.com/watch?v=blQUlD8g4Pk")

#List for movies
movies=[dangal,munthirivallikal_thalirkkumbol,
        kattappanayile_rithwik_roshan,
        ezra,
        the_shawshank_redemption,
        pulimurugan]

fresh_tomatoes.open_movies_page(movies)



