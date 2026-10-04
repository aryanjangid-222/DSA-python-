class Solution(object):
    def searchMatrix(self, matrix, target):
        len_row = len(matrix[0])
        len_mat = len(matrix)
        left_mat = 0
        right_mat = len_mat-1
        while left_mat <= right_mat:
            mid_mat = (left_mat + right_mat)//2
            el = matrix[mid_mat]
            if target >= el[0] and target <= el[len_row - 1]:
                left = 0
                right = len_row
                while left <= right:
                    mid = (left + right)//2
                    if el[mid] == target:
                        return True
                    elif target > el[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
                return target == el[left]
            elif target > el[len_row-1]:
                left_mat = mid_mat + 1
            elif target < el[0]:
                right_mat = mid_mat - 1
        return False