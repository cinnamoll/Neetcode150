class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def total_hour(speed) -> bool:
            return sum(math.ceil(pile / speed) for pile in piles) <= h
        
        l, r = 1, max(piles)
        while l < r:
            mid = l + (r - l) // 2
            if total_hour(mid):
                r = mid 
            else:
                l = mid + 1
        return l