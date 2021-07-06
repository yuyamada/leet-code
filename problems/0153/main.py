# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def solve(nums):
    return f(nums, 0, len(nums) - 1)


def f(nums, l, r):
    if r <= l:
        return nums[l]

    n = len(nums)
    m = (l + r) // 2
    m_prev, m_next = (m - 1 + n) % n, (m + 1) % n
    if nums[m] < nums[m_prev] and nums[m] < nums[m_next]:
        return nums[m]
    elif nums[m] < nums[r]:
        return f(nums, l, m - 1)
    else:
        return f(nums, m + 1, r)


nums = [int(s) for s in input().strip().split()]
ans = solve(nums)
print(ans)
