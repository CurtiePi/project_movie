import media
import fresh_tomatoes


def launch_movie_site():
    # Create emtpy list to populate with Movie objects

    movie_list = []

    # Instantiate Movie objects and append to list of Movie objects

    movie_list.append(media.Movie("Being John Malkovich",
                                  "A puppeteer discovers a portal that leads \
                                   literally into the head of the movie star, \
                                   John Malkovich.",
                                  "http://sciblogs.co.nz/app/uploads/2010/10/Being-John-Malkovish-poster-2.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=Oxvc9KiLmzs"))  # noqa

    movie_list.append(media.Movie("Blade Runner",
                                  "A blade runner must pursue and terminate \
                                   four replicants who have returned to Earth \
                                   to find their creator.",
                                  "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=eogpIG53Cis"))  # noqa

    movie_list.append(media.Movie("Brazil",
                                  "A bureaucrat tries to correct an \
                                   administrative error and finds himself an \
                                   enemy of the state.",
                                  "http://www.iceposter.com/thumbs/MOV_fd1aed4c_b.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=EvBF3Lxla98"))  # noqa

    movie_list.append(media.Movie("Coming to America",
                                  "African prince goes to Queens, New York \
                                   to find a wife.",
                                  "https://upload.wikimedia.org/wikipedia/en/3/38/ComingtoAmerica1988MoviePoster.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=6l9pG_XL8yc"))  # noqa

    movie_list.append(media.Movie("Cool Runnings", 
                                   "Disqulified Jamaican sprinter enlists the \
                                    help of a dishonored coach to start the \
                                    first Jamaican Bobsled Team.",
                                   "http://cdn0.dailydot.com/uploaded/images/original/2014/4/16/coolrunnings.jpg",  # noqa
                                   "https://www.youtube.com/watch?v=Jpdg5XOZZDY"))  # noqa

    movie_list.append(media.Movie("The Dirty Dozen",
                                  "A US Army Major is assigned a dozen \
                                   convicted murderers to train and lead \
                                   on a mission in World War II.",
                                  "http://www.iceposter.com/thumbs/MOV_4d1d28d2_b.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=ff1V6ywnWcY"))  # noqa

    movie_list.append(media.Movie("Fallen",
                                  "Homicide detective investigates killings \
                                   that are very similar to executed killer's \
                                   style.",
                                  "http://www.impawards.com/1998/posters/fallen.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=bP-ey0cVs0M"))  # noqa

    movie_list.append(media.Movie("The Shawshank Redemption",
                                  "The story of an innocent man's stay and \
                                   eventual escape from prison despite all \
                                   obstacles in his way.",
                                  "http://4.bp.blogspot.com/_8_ENa7sVpug/S5emyO6WTsI/AAAAAAAALks/7AdQusg9DXY/s400/ShawshankRedemptionMoviePoster.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=NmzuHjWmXOc"))  # noqa

    movie_list.append(media.Movie("Sweet Sweetback's Baadasssss Song",
                                  "After saving a Black Panther from some \
                                   racist cops, a black male prostitute goes \
                                   on the run from 'the man' with the help of \
                                   the ghetto community and some \
                                   disillusioned Hells Angels.",
                                  "http://www.ugpulse.com/images/articles/daily/20060804_100_1.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=0rD1OzJVoWY"))  # noqa

    movie_list.append(media.Movie("The Thing",
                                  "Antarctic scientists confront \
                                   shape-shifting alien that assumes the \
                                   appearance of the people that it kills.",
                                  "http://blog.lefestinnu.com/wp-content/uploads/2013/12/421RMR3zL7TAb4oVNwTUNDj3nhk.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=F7t-919Ec9U"))  # noqa

    movie_list.append(media.Movie("Time Bandits",
                                  "A young boy accidentally joins a band of \
                                   dwarves as they jump from era to era \
                                   looking for treasure to steal.",
                                  "http://www.iceposter.com/thumbs/MOV_a6611c5d_b.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=ZUSLu5m9URE"))  # noqa

    movie_list.append(media.Movie("Unforgiven",
                                  "Retired gunslinger reluctantly takes on one \
                                   last job, with the help of his old partner \
                                   and a young man.",
                                  "http://www.bydewey.com/unforgiven.jpg",
                                  "https://www.youtube.com/watch?v=N-bNAXtCa_A"))  # noqa

    fresh_tomatoes.open_movies_page(movie_list)


launch_movie_site()

