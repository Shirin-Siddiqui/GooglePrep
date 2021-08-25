def maxThreeSals(array):
    higestSal1 = higestSal2 = higestSal3 = 0
    for i in range(len(array)):
        if array[i] > higestSal1:
            higestSal3 = higestSal2
            higestSal2 = higestSal1
            higestSal1 = array[i]
        elif array[i] > higestSal2:
            higestSal3 = higestSal2
            higestSal2 = array[i]
        elif array[i] > higestSal3:
            higestSal3 = array[i]
    
    return [higestSal1,higestSal2,higestSal3]


array = [4,20,30,25,15,21]
print(maxThreeSals(array))
