class Respondent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"


class AgeGroup:
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.respondents = []

    def add_respondent(self, respondent):
        self.respondents.append(respondent)

    def sort_respondents(self):
        self.respondents.sort(key = lambda x: (x.age, x.name))
        self.respondents = self.respondents[::-1]

    def __str__(self):
        if self.upper_bound == float('inf'):
            return f"{self.lower_bound}+: " + ", ".join(str(respondent) for respondent in self.respondents)
        else:
            return f"{self.lower_bound}-{self.upper_bound}: " + ", ".join(str(respondent) for respondent in self.respondents)


class SurveyModule:
    def __init__(self):
        pass

    def make_age_groups(self, age_boundaries):
        age_groups = []
        prev_bound = 0
        for boundary in age_boundaries:
            age_groups.append(AgeGroup(prev_bound, boundary))
            prev_bound = boundary + 1
        age_groups.append(AgeGroup(prev_bound, float('inf')))
        return age_groups

    def process_survey(self):
        respondents = self.read_respondents_file()
        age_boundaries = self.get_age_boundaries()
        age_groups = self.make_age_groups(age_boundaries)
        for respondent in respondents:
            for age_group in age_groups:
                if age_group.lower_bound <= respondent.age <= age_group.upper_bound:
                    age_group.add_respondent(respondent)

        for age_group in age_groups:
            if age_group.respondents:
                age_group.sort_respondents()
                print(age_group)

    def get_age_boundaries(self):
        while True:
            input_range = input("Введите возрастные рамки:").strip().split()
            try:
                age_boundaries = [int(x) for x in input_range]
            except ValueError:
                print("Ошибка ввода. Повторите ввод.")
                continue
            if not age_boundaries:
                print("Вы не ввели данные. Повторите ввод.")
                continue
            if age_boundaries[0] < 0 or age_boundaries[-1] > 123:
                print("Столько не живут. Повторите ввод.")
                continue
            break
        return age_boundaries

    def read_respondents_file(self):
        respondents = []
        with open("respondents.txt", 'r', encoding ='utf-8') as file:
            for line in file:
                line = line.strip()
                if line == "END":
                    break
                name, age = line.split(',')
                name = name.strip()
                age = int(age.strip())
                if age < 0 or age > 127:
                    print(f"Некорректный возраст у '{name}' ({age})")
                    continue
                respondents.append(Respondent(name, age))
        return respondents


if __name__ == "__main__":
    survey_module = SurveyModule()
    survey_module.process_survey()