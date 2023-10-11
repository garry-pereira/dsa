# Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer
# limit, return a boolean array that represents the answer to each query. A query is true if the sum 
# of the subarray from x to y is less than limit, or false otherwise.

# For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13,
# the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].

def main(nums: list[int], queries: list[list[int]], limit: int) -> list[bool]:

    # make the prefix sum
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(prefix[i-1] + nums[i])

    # main
    ans = []
    for x, y in queries:
        ans.append(prefix[y] - prefix[x] + nums[x] < limit)

    return ans

nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13

print(main(nums, queries, limit))
