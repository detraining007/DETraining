class Sort_Matrix(object):
    def single_list(self, matrix):
        flat = []
        for row in matrix:
            for i in row:
              flat.append(i)
        flat.sort()
        return flat

    # def sort_list(self, flat):
    #     flat.sort()
    #     return flat

    def create_sorted_matrix(self, flat, rows, cols):
        matrix = []
        idx = 0
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(flat[idx])
                idx += 1
            matrix.append(row)
        return matrix

obj = Sort_Matrix()
matrix = [[1, 8], [-1, 4]]
flat = obj.single_list(matrix)
# sorted_flat = obj.sort_list(flat)
res = obj.create_sorted_matrix(flat, len(matrix), len(matrix[0]))

for r in res:
 print(r)