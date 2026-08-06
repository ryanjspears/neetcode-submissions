from typing import List
from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        queue = deque([(0, 0)])
        visited = {0}

        while queue:
            current_amount, number_of_coins = queue.popleft()

            for coin in coins:
                next_amount = current_amount + coin

                if next_amount == amount:
                    return number_of_coins + 1

                if next_amount < amount and next_amount not in visited:
                    visited.add(next_amount)
                    queue.append(
                        (
                            next_amount,
                            number_of_coins + 1
                        )
                    )

        return -1