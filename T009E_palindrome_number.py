class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        nums = list()

        while x != 0:
            x, m = divmod(x, 10)
            nums.append(m)

        for i in range(len(nums) // 2):
            if nums[i] != nums[-(i + 1)]:
                return False

        return True
