class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:


        # Example: 4 2 2 9 9 -> 4 2 3 0 0

        # 9 9 
        # 9 0 
        # 0 0
        # 9 8 9 -> 9 9 0

        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            mod_10 = True
            for i in range(len(digits)-1, -1, -1):
                if digits[i] == 9 and mod_10:
                    digits[i] = 0
                    mod_10 = True
                    if i == 0:
                        print(i)
                        return [1] + (len(digits) * [0])
                elif mod_10:
                    digits[i] += 1
                    mod_10 = False
                else:
                    return digits

            return digits



                


        # add_one = False
        # for i in range(len(digits), 0):

        #     if add_one:

        #     if digits[i] == 9:
        #         digits[i] = 0
        #         add_one = True
        #     else:
        #         digirs[i] += 1
        #         add_one = False

                
                    


            

        # 9

        # % 10 operations
        