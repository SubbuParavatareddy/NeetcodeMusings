class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = dict()
        t_dict = dict()
        for ch in s:
            s_dict[ch] = s_dict.get(ch, 0) + 1

        for ch in t:
            t_dict[ch] = t_dict.get(ch, 0) + 1

        for val in s_dict:
            t_value = t_dict.get(val, 0)
            s_value = s_dict.get(val, 0)
            if (t_value!=s_value):
                return False

        return True