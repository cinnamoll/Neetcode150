def trap(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    maxL, maxR = height[l], height[r]
    res = 0
    while l < r:
        if maxL <= maxR:
            l+=1
            maxL = max(maxL, height[l])
            res += max(0, maxL - height[l])
        else:
            r-=1
            maxR = max(maxR, height[r])
            res += max(0, maxR - height[r])
    return res

test = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height=test))