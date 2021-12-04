import numpy as np

def count_increase(measurements):
    print(len(np.where(np.diff(measurements) > 0)[0]))
    
if __name__ == '__main__':
    with open('input1.txt', 'r') as f:
        lines = f.readlines()

    measurements = []
    for line in lines:
        measurements.append(int(line.strip()))

    measurements = np.array(measurements)

    count_increase(measurements)

    sliding_window = np.array([])
    for i in range(1,len(measurements)-1):
        sliding_window = np.append(sliding_window, np.sum(measurements[i-1:i+2]))

    count_increase(sliding_window)

    

