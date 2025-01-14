from collections import defaultdict
from typing import List


class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        maxUnique = -1
        numbers = defaultdict()

        for number in A:
            if number in numbers:
                numbers[number] += 1
            else:
                numbers[number] = 1

        for key, value in numbers.items():
            if value == 1:
                maxUnique = max(maxUnique, key)
        # ToDo: Write Your Code Here.
        return maxUnique


# version 2


class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        freq = defaultdict(int)

        # Populate the dictionary with number frequencies
        for num in A:
            freq[num] += 1

        maxUnique = -1
        # Traverse the dictionary to find the largest unique number
        for key, value in freq.items():
            if value == 1:
                maxUnique = max(maxUnique, key)

        return maxUnique


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestUniqueNumber([5, 7, 3, 7, 5, 8]))  # Expected: 8
    print(sol.largestUniqueNumber([1, 2, 3, 2, 1, 4, 4]))  # Expected: 3
    print(sol.largestUniqueNumber([9, 9, 8, 8, 7, 7]))   # Expected: -1
