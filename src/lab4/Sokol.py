
class Film:
    def __init__(self, film_id, name : str):
        self.film_id = film_id
        self.name = name


class UserHistory:
    def __init__(self, watched_films):
        self.watched_films = watched_films


def read_films_file():
    films = []
    with open("films.txt", 'r', encoding ='utf-8') as file:
        for line in file:
            st = line.strip().split(',')
            try:                                # определяем номер и название каждого фильма в файле
                film_id = int(st.pop(0))
                name = st[0]
                films.append(Film(film_id, name))
            except ValueError:
                print('Ошибка обработки файла films.txt')

    return films            # получаем массив с названиями всех доступных фильмов


def read_user_history_file():
    user_histories = []
    with open("user_history.txt", 'r', encoding = 'utf-8') as file:
        for line in file:
            try:
                watched_films = list(map(int, line.strip().split(',')))
                user_histories.append(UserHistory(watched_films))
            except ValueError:
                print('Ошибка обработки файла user_history.txt')

    return user_histories   # получаем список историй просмора пользователей


def parse_user_input(user_input):
    user_watched_films = list(map(int, user_input.strip().split(',')))
    return user_watched_films


def recommend_film(films, user_histories, user_watched_films):
    candidates = []

    for user_history in user_histories:
        match = set(user_watched_films) & set(user_history.watched_films)
        if len(match) >= len(user_watched_films) // 2:
            candidates.append(user_history)

    candidate_films = [film for user in candidates for film in user.watched_films if film not in set(user_watched_films)]

    if not candidate_films:
        return None

    film_views_count = {}
    for film_id in candidate_films:
        film_views_count[film_id] = film_views_count.get(film_id, 0) + 1

    recommended_film_id = max(film_views_count, key=film_views_count.get)
    return next((film for film in films if film.film_id == recommended_film_id), None)


def main():
    films = read_films_file()
    user_histories = read_user_history_file()


    user_input = input('Введите номера просмотренных фильмов через запятую:')
    user_watched_films = parse_user_input(user_input)

    recommendation = recommend_film(films, user_histories, user_watched_films)

    if recommendation:
        print('Рекомендуем посмотреть:', recommendation.name)
    else:
        print('Нет рекомендаций')

if __name__ == '__main__':
    main()