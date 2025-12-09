class Solution:
    def isValid(self, word: str) -> bool:
        check_1 =0
        check_2 =0
        vowel_set = set(["a","e","i","o","u","A","E","I","O","U"])
        if len(word) >=3:
            for i in word:
                if i in vowel_set:
                    check_1 = 1
                elif i.isalpha():
                    check_2 = 1
                elif i.isdigit():
                    pass
                else:
                    return False
        else:
            return False
        if check_1 and check_2:
            return True
        return False

