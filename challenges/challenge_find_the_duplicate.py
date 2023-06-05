def find_duplicate(nums):
    if not nums or isinstance(nums, str):
        return False

    n = len(nums) - 1
    count = [0] * (n + 1)

    for num in nums:
        if not isinstance(num, int) or num < 1 or num > n:
            return False
        count[num] += 1
        if count[num] > 1:
            return num

    return False
