import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.reshape(list,(3,3))
    
    calculations = dict()
    calculations["mean"] = __calculate_measure(matrix, np.mean)
    calculations["variance"] = __calculate_measure(matrix, np.var)
    calculations["standard deviation"] = __calculate_measure(matrix, np.std)
    calculations["max"] = __calculate_measure(matrix, np.amax)
    calculations["min"] = __calculate_measure(matrix, np.amin)
    calculations["sum"] = __calculate_measure(matrix, np.sum)
    return calculations

def __calculate_measure(matrix, fn):
    list = []
    list.append(fn(matrix, axis=0).tolist()) # axis1 / columns
    list.append(fn(matrix, axis=1).tolist()) # axis2 / rows
    list.append(fn(matrix).tolist()) # flattened
    return list