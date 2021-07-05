# https://leetcode.com/problems/product-of-array-except-self/

def solve(nums):
    results = [0] * len(nums)
    product = 1
    for i in range(len(nums)):
        results[i] = product
        product *= nums[i]

    product = nums[len(nums) - 1]
    for i in range(len(nums) - 2, -1, -1):
        results[i] *= product
        product *= nums[i]


nums = [int(s) for s in input().strip().split()]
ans = solve(nums)
print(ans)
