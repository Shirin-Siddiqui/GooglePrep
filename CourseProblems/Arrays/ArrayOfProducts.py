def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]

    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i != j:
                runningProduct *= array[j]
        products[i]= runningProduct
    
    return products


def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    lProd = [1 for _ in range(len(array))]
    rProd = [1 for _ in range(len(array))]

    runningProduct = 1
    for i in range(len(array)):
        lProd[i] = runningProduct
        runningProduct *= array[i]

    runningProduct = 1
    for i in reversed(range(len(array))):
        rProd[i] = runningProduct
        runningProduct *= array[i]
    
    for i in range(len(array)):
        products[i] = lProd[i] * rProd[i]
    
    return products


def arrayOfProducts(array):    
    products = [1 for _ in range(len(array))]
    lProd = [1 for _ in range(len(array))]

    runningProduct = 1
    for i in range(len(array)):
        lProd[i] = runningProduct
        runningProduct *= array[i]
    
    runningProduct = 1
    for i in reversed(range(len(array))):
        products[i] = runningProduct * lProd[i]
        runningProduct *= array[i]
    
    return products