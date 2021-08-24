class Show:

    def __init__(self, name: str, year: int) -> None:
        super().__init__()
        self.__name = name.title()  # All first letter capitalized
        self.year = year
        self.__likes = 0

    def __str__(self):
        return f'{self.__name} - {self.year} - {self.__likes}'

    def like(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value.capitalize()


class Filme(Show):

    def __init__(self, name: str, year: int, duration: int) -> None:
        super().__init__(name, year)
        self.duration = duration


class Serie(Show):

    def __init__(self, name: str, year: int, seasons: int) -> None:
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self) -> str:
        return super().__str__() + ' Serie'


class Playlist:

    def __init__(self, name, shows: [Show]) -> None:
        self.name = name
        self._shows = shows

    # Make this class possible to be
    # used with len() method
    def __len__(self):
        return len(self._shows)

    @property
    def shows(self) -> [Show]:
        return self._shows

    # Make this class iterable
    # so I can use in for loops for example
    # or use method in to validate if an item
    # is inside my list
    def __getitem__(self, item):
        return self._shows[item]


avengers = Filme('Avenger infinite war', 2018, 160)
friends = Serie(name='friends', year=2000, seasons=10)

shows: [Show] = [avengers, friends]

weekendPlaylist = Playlist('final de semana python', shows)

for show in weekendPlaylist:
    show.like()
    print(show)

print(f'Avenger está presente na lista? {avengers in weekendPlaylist}')
print(f'Quantidade de items na lista {len(weekendPlaylist)}')