class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        lastIndex = len(s) - 1
        ptr1 = lastIndex - 1

        while ptr1 >= 0:
            s.append(s[ptr1])
            s.pop(ptr1)

            ptr1 -= 1