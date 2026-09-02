class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)

        max = 0
        start_nums = set()
        for i in nums:
            pre_num = i - 1
            if pre_num not in set_nums:
                start_nums.add(i)

        for s in start_nums:
            count = 1
            next_num = s + 1
            while next_num in set_nums:
                count += 1
                next_num += 1

            if max < count:
                max = count

        return max