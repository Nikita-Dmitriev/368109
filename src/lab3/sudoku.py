import pathlib
import random
from random import randint
import typing as tp

from pyparsing import col

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return [values[i:i+n] for i in range(0, len(values), n)]



def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """
    Возвращает все значения для номера строки, указанной в pos.

    :param grid: Нерешенный судоку.

    :param pos: Позиция элемента для проверки.

    :return: Список уже существующих значений в строке.
    """
    """
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    row = pos[0]
    return [grid[row][j] for j in range(0, (len(grid) + 1)//3)]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """
    Возвращает все значения для номера столбца, указанного в pos

    :param grid: Нерешенный судоку.

    :param pos: Позиция элемента для проверки

    :return: Список уже существующих элементов в столбце.
    """
    """
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    col = pos[1]
    return [grid[i][col] for i in range(len(grid))]


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """
    Возвращает все значения из квадрата, в который попадает позиция pos

    :param grid: Нерешенный судоку.

    :param pos: Позиция

    :return: Список существующих значений в блоке.
    """
    """
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    place_row = pos[0]
    place_col = pos[1]
    block_row = place_row // 3
    block_col = place_col // 3
    min_row = block_row * 3
    min_col = block_col * 3
    return [grid[i][j] for i in range(min_row, min_row + 3) for j in range(min_col, min_col + 3)]


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """
    Найти первую свободную позицию в пазле

    :param grid: Нерешенный судоку.

    :return: каорды пустой позиции.
    """
    """
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                return i, j     # возвращаем первое свободное место
    return None



def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """
    Вернуть множество возможных значения для указанной позиции!

    :param grid: Нерещенный судоку.

    :param pos: Позиция элемента для поиска значений.

    :return: Множество возможных значений.
    """
    """
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    row_nums = set(get_row(grid, pos))
    col_nums = set(get_col(grid, pos))
    block_nums = set(get_block(grid, pos))
    var = {str(i) for i in range(1,10)}

    possible_values = var - row_nums - col_nums - block_nums

    return possible_values


    return


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """
    Решение пазла, заданного в grid!

    :param grid: Нерешенное судоку

    :return: Решенный судоку!
    """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    free_pos = find_empty_positions(grid)
    if not free_pos:
        return grid # You win!

    row = free_pos[0]
    col = free_pos[1]
    possible_values = find_possible_values(grid, free_pos)
    for num in possible_values:
        grid[row][col] = num
        if solve(grid):
            return grid
        grid[row][col] = '.'
    return None

def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """
    Если решение solution верно, то вернуть True, в противном случае False.

    :param solution: Решеный судоку.

    :return: Булево значений, обозначает правильность решения.
    """


    check_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    for row in range(9):
        if set(get_row(solution, (row,1))) != check_set:
            return False

    for col in range(9):
        if set(get_col(solution, (1, col))) != check_set:
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if set(get_block(solution, (i, j))) != check_set:
                return False

    return True



def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """
    Генерация судоку заполненного на N элементов.

    :param N: Integer сколько должно быть заполненых значений.

    :return: Генерирует судоку с N заполнеными элементами.
    """
    """
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    grid = solve([['.' for _ in range(9)] for _ in range(9)])

    point_count = 81 - N

    for _ in range(point_count):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while grid[row][col] == '.':
            row, col = random.randint(0, 8), random.randint(0, 8)
        grid[row][col] = '.'

    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)