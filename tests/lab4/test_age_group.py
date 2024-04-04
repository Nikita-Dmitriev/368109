import unittest
from src.lab4.age_group import Respondent, AgeGroup


class TestRespondent(unittest.TestCase):
    def test_str_representation(self):
        respondent = Respondent("Джонидеп Леонтьев", 52)
        self.assertEqual(str(respondent), "Джонидеп Леонтьев (52)")


class TestAgeGroup(unittest.TestCase):
    def test_str_representation(self):
        age_group = AgeGroup(0, 18)
        age_group.add_respondent(Respondent("Сидоров Сережа", 16))
        age_group.add_respondent(Respondent("Иванов Иван", 17))
        self.assertEqual(str(age_group), "0-18: Сидоров Сережа (16), Иванов Иван (17)")

    def test_str_representation_infinity(self):
        age_group = AgeGroup(101, float('inf'))
        age_group.add_respondent(Respondent("Кошельков Захар Брониславович", 105))
        self.assertEqual(str(age_group), "101+: Кошельков Захар Брониславович (105)")



if __name__ == '__main__':
    unittest.main()