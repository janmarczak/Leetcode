class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                return digits
        return [1] + digits 


        # if digits[-1] != 9:
        #     digits[-1] += 1
        #     return digits
        # else:
        #     mod_10 = True
        #     for i in range(len(digits)-1, -1, -1):
        #         if digits[i] == 9 and mod_10:
        #             digits[i] = 0
        #             mod_10 = True
        #             if i == 0:
        #                 return [1] + (len(digits) * [0])
        #         elif mod_10:
        #             digits[i] += 1
        #             mod_10 = False
        #         else:
        #             return digits

        #     return digits
