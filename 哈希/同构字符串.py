class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 定义两个字典，分别存正向和反向映射的内容
        forward = {}
        backward = {}
		
        for i in range(len(s)):
            a = s[i]
            b = t[i]
			# 判断是否满足正向检查
            # 如果a在forward字典中但是存的值不是b
            # 证明正向映射失败
            if a in forward and forward[a] != b:
                return False
           
			# 判断是否满足反向检查
            # 如果b在backward字典中但是存的值不是a
            # 证明反向映射失败
            if b in backward and backward[b] != a:
                return False
			# 如果上面两种都满足，建立双向映射关系
            # 并且返回True
            forward[a] = b
            backward[b] = a

        return True
