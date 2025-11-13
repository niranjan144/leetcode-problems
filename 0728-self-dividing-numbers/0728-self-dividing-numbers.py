class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num: int) -> bool:
            for d in str(num):
                if d == '0' or num % int(d) != 0:
                    return 0
            return 1

        return [n for n in range(left, right + 1) if is_self_dividing(n)]
