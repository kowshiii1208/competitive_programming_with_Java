class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        res = []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                    row.append(matrix[j][i])
            res.append(row)
        return res