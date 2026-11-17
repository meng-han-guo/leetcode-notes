def length_of_longest_substring(s):
    # seen集合表示窗口，left表示左边界
    seen = set()
    left = 0
    # longest记录全局最长
    longest = 0
	
    for right in range(len(s)):
        # 如果窗口中有重复元素
        # 使用while循环让左边界+1
        # 直到窗口中没有重复元素
        while s[right] in seen:
            seen.remove(s[left])
            left = left + 1
		
        seen.add(s[right])
		# 计算当前窗口长度
        current_length = right - left + 1
        # 更新全局最长
        if current_length > longest:
            longest = current_length

    return longest
