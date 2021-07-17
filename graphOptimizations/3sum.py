class Solution:
	def threeSum(self, nums):
		res = []
		found, dups = set(), set()
		seen = {}
		for i, val1 in enumerate(nums):
			if val1 not in dups:
				dups.add(val1)
				for j, val2 in enumerate(nums[i+1:]):
					complement = -val1 - val2
					if complement in seen and seen[complement] == i:
						min_val = min(val1, val2, complement)
						max_val = max(val1, val2, complement)
						if (min_val, max_val) not in found:
							found.add((min_val, max_val))
							res.append([val1, val2, complement])
					seen[val2] = i
		return res
s=Solution()
arr=[-1,0,1,2,-1,4]
print(s.threeSum(arr))
