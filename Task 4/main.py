# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 


class Movie:
    """class Movie
    Required arguments are title, director and budget.
    Title and director arguments must be string type.
    Budget argument must be integer type.
    """

    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def was_expensive(self):
        """Returns true if budget was above 100M USD, false otherwise."""
        if self.budget <= 10 ** 8:
            return False
        return True


movie1 = Movie("The Shawshank Redemption", "Frank Darabont", 25_000_000)

movie2 = Movie("Dune", "Denis Villeneuve", 165_000_000)

movie3 = Movie("Avatar", "James Cameron", 237_000_000)
