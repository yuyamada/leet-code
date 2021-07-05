# https://leetcode.com/problems/contains-duplicate/

def solve(nums):
    m = set()
    for v in nums:
        if v in m:
            return True
        m.add(v)

    return False


def solve_otake(nums):
    m = set(nums)
    if len(m) < len(nums):
        return True
    return False


nums = [int(s) for s in input().strip().split()]
ans = solve(nums)
print(ans)
