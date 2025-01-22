from typing import List, Dict


def rod_cutting_memo(length: int, prices: List[int], memo: dict = None) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через мемоізацію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """

    if memo is None:
        memo = {}
        memo[0] = {"max_profit": 0,
                   "cuts": [],
                   "number_of_cuts": 0}
        memo[1] = {"max_profit": prices[0],
                   "cuts": [1],
                   "number_of_cuts": 0}
    if length in memo:
        return memo[length]

    cuts = []
    max_profit = 0
    for i in range(1, length + 1):
        if i <= len(prices):
            next_cut = rod_cutting_memo(length - i, prices, memo)
            profit = prices[i - 1] + next_cut["max_profit"]
            if profit > max_profit:
                max_profit = profit
                cuts = [i] + next_cut["cuts"]
                cuts_quantity = len(cuts) - 1
    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": cuts_quantity
    }



def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через табуляцію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    res = [0] * (length + 1)
    cut_choices = [0] * (length + 1)

    for i in range(1, length + 1):
        for j in range(1, i + 1):
            if j <= len(prices) and res[i] < res[i - j] + prices[j - 1]:
                res[i] = res[i - j] + prices[j - 1]
                cut_choices[i] = j

    cuts = []
    n = length
    while n > 0:
        cuts.insert(0, cut_choices[n])
        n -= cut_choices[n]

    max_profit = res[length]
    cuts_quantity = len(cuts) - 1 if cuts else 0
    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": cuts_quantity,
    }


def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        # Тест 2: Оптимально не різати
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        # Тест 3: Всі розрізи по 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")


if __name__ == "__main__":
    run_tests()