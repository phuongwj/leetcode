class Solution:
    def compress(self, chars: list[str]) -> int:

        n = len(chars)
        newChars = []

        i = 0
        while i < n:
            count = 1
            ptr = i+1

            while ptr < len(chars) and chars[ptr] == chars[i]:
                count += 1
                ptr += 1


            newChars.append(chars[i])
            if count != 1:
                newChars.extend(list(str(count)))

            i = ptr

        chars.clear()

        for elem in newChars:
            chars.append(elem)

        return len(chars)