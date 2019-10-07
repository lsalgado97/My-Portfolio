# In this code, I'm defining classes to represent moving pictures in general, and two
# special classes which inherit properties from the general moving picture representation:
# films and TV series. After defining the classes, their properties and methods, I write
# a small code which prints a playlist of movies and TV series. For a little roleplaying,
# a number of people who liked each picture is introduced.

# This code was written in the context of a python learning course, and has the purpose of
# introducing the concepts of class inheritance, polymorphism, object string representation
# and duck typing


class Picture:

    # This is a parent class, it's properties will be inherited
    # by the two following daughter classes

    def __init__(self, title, year, likes=0):
        self._title = title.title()
        self.year = year
        self._likes = likes

    @property
    def likes(self):
        return self._likes

    def like(self):
        self._likes += 1

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

# the following classes, Film and Series, inherit properties from
# the Picture class. All properties of the Picture class will be
# accessible by any Film and Series objects. In both classes, a
# specific __str__ method is defined to give the classes an unique
# string representation (allows us to do print(film/series))

class Film(Picture):

    def __init__(self, title, year, runtime, likes=0):
        super().__init__(title, year, likes)
        self.runtime = runtime

    def __str__(self):
        return f'{self.title} - {self.year} - {self.runtime} min; # of likes: {self.likes}'

class Series(Picture):

    def __init__(self, title, year, seasons, likes=0):
        super().__init__(title, year, likes)
        self.seasons = seasons

    def __str__(self):
        return f'{self.title} - {self.year} - {self.seasons} season(s); # of likes: {self.likes}'

# I created the next class to emulate a list object, but with
# other desired characteristics. To do this, we must define
# specific __getitem__ (to make a Plylist object iterable)
# and __len__ (to make a Plylist object sized) methods.

class Playlist:

    def __init__(self, name, pictures):
        self.name = name
        self._pictures = pictures

    # making my playlist object an iterable
    def __getitem__(self, item):
        return self._pictures[item]

    # playlists are sized
    def __len__(self):
        return len(self._pictures)


avengers = Film('avengers: endgame', 2019, 182, int(1e9))
ad_astra = Film('ad astra', 2019, 124)
joker = Film('joker', 2019, 122)
the_boys = Series('the boys', 2019, 1, 7)
stranger = Series('Stranger things', 2016, 3, 10)

avengers.like()
avengers.like()
avengers.like()

ad_astra.like()
ad_astra.like()

joker.like()
joker.like()
joker.like()
joker.like()
joker.like()

pics = [avengers, ad_astra, joker, the_boys, stranger]
this_year_favs = Playlist('My favorite series and movies of 2019', pics)
for pic in this_year_favs:
    print(pic)
