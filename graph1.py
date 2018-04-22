from PIL import Image
import numpy as np

if __name__ == '__main__':
    array = np.loadtxt("1.csv", delimiter=",")
    array = array.astype('uint8')
    array[array > 0] = 255
    i = Image.fromarray(array, mode='L')
    i.save('1.png')