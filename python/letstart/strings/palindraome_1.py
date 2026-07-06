def longest_palindrome(s):
    if not s:
        return ""

    start = 0
    max_len = 1

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        # 1️⃣ Odd length palindrome (aba)
        l1, r1 = expand(i, i)
        if r1 - l1 + 1 > max_len:
            start = l1
            max_len = r1 - l1 + 1

        # 2️⃣ Even length palindrome (abba)
        l2, r2 = expand(i, i + 1)
        if r2 - l2 + 1 > max_len:
            start = l2
            max_len = r2 - l2 + 1

    return s[start:start + max_len]



print(longest_palindrome("babad"))   # bab or aba
print(longest_palindrome("cbbd"))    # bb
print(longest_palindrome("a"))       # a
print(longest_palindrome("aa"))      # aa
print(longest_palindrome("forgeeksskeegfor"))  # geeksskeeg
