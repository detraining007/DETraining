def find_index(matrix, target):
    for i, row in enumerate(matrix):  # Loop through each row
        for j, value in enumerate(row):  # Loop through each column (inside the row)
            if value == target:  # If we find the target value
                return (i, j)  # Return its (row, column) index
    return "Element not found"  # If the element is not found, return None

def swap_elements(matrix, index1, index2):

    if index1 and index2:
        i1 , j1 = index1
        i2 , j2 = index2
        if (i1 == i2 or i1+1 == i2 or i2+1 == i1) and (j1 == j2 or j1+1 == j2 or j2+1 == j1):
          matrix[i1][j1] , matrix[i2][j2] = matrix[i2][j2] , matrix[i1][j1]
          return matrix
        else:
            return "Only adjacent elements will be swapped"
    else:
        return "One or both elements not found"

matrix = [[7, 4, 8,10], [1, 5, 3,11], [6, 9,12, 2]]

if __name__ == "__main__":
    opinion = "yes"
    print("Before swapping")
    for row in matrix:
        print(row)

    #To swap multiple times based on your requirements
    while opinion=='yes':
        try:
           target1 = int(input("Please select 1st element which you need to swap"))
           target2 = int(input("Please select 2nd element which you need to swap"))
        except Exception:
            raise "Value should be Number"


        index1 = find_index(matrix, target1)
        index2 = find_index(matrix, target2)

        if type(index1) == tuple and type(index2) == tuple:
            result = swap_elements(matrix, index1, index2)
            if isinstance(result, list):
                print("Swapped list")
                for row in result:
                    print(row)
                # opinion=input("Do you swap again ? Type yes/no").lower
            else:
                print(result)
        else:
            print("Cannot find elements")
            print("Do you want still swap as per your requirements ? if so")
            opinion = input("Enter yes/no").lower()
            while opinion not in ["yes", "no"]:
                opinion = input("Enter yes/no: ").lower()
