class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = []

        for i in range(len(nums)):
            if nums[i] in one:
                one.remove(nums[i])
            else:
                one.append(nums[i])
        result = one[0]

        return (result)

