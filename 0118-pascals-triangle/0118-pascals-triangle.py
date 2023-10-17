class Solution:
    solution = []
    def generate(self, numRows: int) -> List[List[int]]:

        # For Loop Solution
        # solution = []
        # for i in range(1, numRows+1):
        #     if i == 1 or i == 2:
        #         solution.append(([1] * i))
        #     else:
        #         tmp = [1]
        #         for j in range(1, i-1): # range: 1, 1
        #             tmp.append(solution[i-2][j-1] + solution[i-2][j])
        #         tmp.append(1)
        #         solution.append(tmp)

        # return solution


        # Dynamic solution
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        prev_rows = self.generate(numRows - 1)
        prev_row = prev_rows[-1]
        current_row = [1]

        for i in range(1, numRows - 1):
            current_row.append(prev_row[i-1] + prev_row[i])

        current_row.append(1)
        prev_rows.append(current_row)

        return prev_rows

