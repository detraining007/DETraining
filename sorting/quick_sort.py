class Quick_Sort:
    def __init__(self,array,Pivot):
        self.array = array
        self.Pivot = Pivot
    def sorting(self):
        array = self.array
        Pivot = self.Pivot
        
        for val in array:
            left = 0
            right = -1
            left_ele = array[left]
            right_ele = array[right]
            for val2 in range(val+1):
             if array[val2]<Pivot:
                left += 1
             elif array[val2]>Pivot:
                right -= 1
            if array[left] >= Pivot and array[right] <= Pivot:
                array[left]= right_ele
                array[right]= left_ele
            print(array)


        









if __name__ == "__main__":
    elements = input("Please enter the elements as numbers: ")  
    array = list(map(int,elements.split()))
    print("Unsorted array:",array)
    Pivot = int(input("Enter the element from the array u want to choose as pivot: "))
    sorted = Quick_Sort(array,Pivot)
    sorted.sorting()