import unittest
from src.lab4.Sokol import *

class TestFilmRecommendationSystem(unittest.TestCase):
    def test_parse_user_input(self):
        user_input = "1,4,6"
        expected_output = [1, 4, 6]
        self.assertEqual(parse_user_input(user_input), expected_output)

    def test_recommend_film(self):
        films = [
            Film(1, "Манхеттен"),
            Film(2, "Энни Холл"),
            Film(3, "Банкир"),
            Film(4, "Сияние"),
            Film(5, "Зеленая миля"),
            Film(6, "Остров проклятых"),
        ]
        user_histories = [
            UserHistory([2, 1, 3, 6]),
            UserHistory([1, 3, 4]),
            UserHistory([5, 5, 2, 3]),
            UserHistory([1, 5, 6, 2, 4]),
            UserHistory([2, 3, 3, 1]),
            UserHistory([4, 4, 4, 2]),
            UserHistory([1, 2, 3, 4, 6])
        ]
        user_watched_films = [1, 4, 6]

        recommendation = recommend_film(films, user_histories, user_watched_films)
        self.assertIsNotNone(recommendation)
        self.assertEqual(recommendation.film_id, 2)

if __name__ == "__main__":
    unittest.main()