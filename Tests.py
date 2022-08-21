import numpy as np
import Math as m

# Función para probar el método para calcular el inverso de la matriz
def pruebaInverso(matrix):
    '''
    PRUEBA COMPLETADA

    '''
    print(m.getMatrixInverse(matrix))
    print(np.linalg.inv(np.array(matrix)))


def pruebaRestaMatrices(matrix1,matrix2):
    print(m.matrix_substract(matrix1,matrix2))
    print(np.subtract(np.array(matrix1),np.array(matrix2)))

# pruebaInverso([[1, 2, 3, 4],[0,5,7,9],[-2,4,-8,5],[10,6,6,7]])
# pruebaRestaMatrices([[0,1],[0,2]] ,[[0,1,2],[3,4,5],[6,7,8]])
# print('\n')
pruebaRestaMatrices([[0,1,1],[0,2,9],[5,6,7]] ,[[0,1,2],[3,4,5],[6,7,8]])