from PIL import Image
import numpy as np

if __name__ == '__main__':
    array = np.loadtxt("2.csv", delimiter=",")
    array *= 2.55
    array = array.astype('uint8')
    i = Image.fromarray(array, mode='L')
    i.save('2.png')