class Solution:
    solution = []
    def generate(self, numRows: int) -> List[List[int]]:

        solution = []
        for i in range(1, numRows+1):
            if i == 1 or i == 2:
                solution.append(([1] * i))
            else:
                tmp = [1]
                for j in range(1, i-1): # range: 1, 1
                    tmp.append(solution[i-2][j-1] + solution[i-2][j])
                tmp.append(1)
                solution.append(tmp)

        return solution



        # if numRows == 1:
        #     return [[1]]
        # elif numRows == 2:
        #     return [[1, 1]]
        # else:

        #     # 4
        #     [1,3,3,1]

        #     # 5
        #     [1,4,6,4,1]


        #     return solution + generate()

            # 5 -> 5 integer array
            # 1
            # 1+3
            # 3+3
            # 3+1
            # 1

        