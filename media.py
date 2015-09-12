import webbrowser

class Movie():
    """"Movie class is a object of movie information.

        Attributes:
            title: String indicating the name of the movie.
            storyline: String indication the plot summary of the movie.
            poster_image_url: String url of image of movie poster.
            trailer_youtube_url: String url of YouTube movie trailer.
    """

    def __init__(self, title, storyline, poster, trailer):
        """"Initializes the Movie class.

            Parameters::
                title: String indicating the name of the movie.
                storyline: String indication the plot summary of the movie.
                poster: String url of image of movie poster.
                trailer: String url of YouTube movie trailer.
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """Opens a browser window to show a video of the movie trailer."""
        webbrowser.open(self.trailer_youtube_url)
