
def fs_quick(arr, num):
    indexes = {}
    for e in arr:
        if e < num:
            target = num-e
            if target in indexes:
                return [target, e]
            elif e not in indexes:
                indexes.update({e: 1})
    return []


def fs_left_to_right(arr, num):
    indexes = {}
    for e in arr:
        if e < num and e not in indexes:
            indexes.update({e: 1})
    for n in arr:
        rest = num-n
        if rest in indexes:
            return [n, rest]

    return []


if __name__ == "__main__":

    # Ejemplo de muestra ofrecido en el PDF.
    x = [1, 5, 8, 2, 9]

    # Valor de ejemplo de muestra
    y = 10

    # Primer metodo, busqueda rapida (fs_quick)
    # Este metodo evaluara todas las combinaciones anteriores durante la iteracion, lo que hace que el algoritmo se
    # detenga justo cuando consiga algun valor que coincida con el valor solicitado, por ejemplo en el caso planteado
    # en el pdf de muestra:
    # [1, 5, 8, 2, 9]
    # Al realizar este metodo de busqueda encontrara primero la coincidencia de 8 y 2, ya que es la primera coincidencia
    # que el algoritmo puede encontrar durante la iteracion ya que aun no ha llegado a leer el 9 y ya encontro una
    # coincidencia para el numeor solicitado
    # En las pruebas realizadas (con un poder de procesamieto alto) el resultado fue de 0.000 segundos para el ejemplo
    # del pdf, en una lista de 100.000 elementos en el array se obtuvo EN EL PEOR CASO (que no exista coincidencia), se
    # obtuvo un tiempo de 0.031 segundos, si lo que se necesita es comprobar que el numero exista y obtener los valores
    # que concuerden este es el metodo optimo incluso si se quiere modificar para obtener todas las variantes posibles.

    print(fs_quick(x, y))

    # Segundo metodo, busqueda ordenada de izquierda a derecha (fs_left_to_right)
    # Este metodo indexara y evaluara todos los valores que puedan ser utiles para la operacion deseada y luego
    # recorrera cada uno de los elementos de izquierda a derecha y comparara si el valor que necesito ha sido indexado
    # lo que hace tener un resultado dando prioridad al primer valor que pueda coincidir con la sumatoria solicitada
    # Tomando de ejemplo de muestra:,
    # [1, 5, 8, 2, 9]
    # Va a indexar cada uno de los valores y luego iniciara una nueva iteracion para consultar si existe indexado el
    # valor que concuerde con el valor solicitado en la sumatoria por lo que si tendria en cuenta el valor de 1 y 9 como
    # primera coincidencia correcta de izquierda a derecha.
    # En las pruebas realizadas (con un poder de procesamieto alto) el resultado fue de 0.000 segundos para el ejemplo
    # del pdf, en una lista de 100.000 elementos en el array se obtuvo EN EL PEOR CASO (que no exista coincidencia), se
    # obtuvo un tiempo de 0.062 segundos (hubo dos iteraciones) y se devolvio como resultado [] (sin coincidencias) por
    # lo que siendo un metodo ordenado no es el mas optimo pero es la forma correcta en caso de necesitar obtener el
    # resultado especificamente en el orden leido de izquierda a derecha.

    print(fs_left_to_right(x, y))

    # Optimizacion: La optimizacion del algoritmo tiene un rendimiento excelente de manera lineal sin dejar de lado la
    # posiblidad de mejora, pero es posible que en caso de necesitar procesar millones de numeros se podria partir de
    # la idea de crear esto en N hilos segun la cantidad de datos y dividir en varios bloques la indexacion de los
    # valores e incluso se podria garantizar un tiempo de respuesta maximo utilizando procesamiento paralelo lo que
    # reduciria el tiempo pero aumentaria el uso de recursos para la tarea.

    # NOTA: Para realizar las pruebas de tiempo y optimizacion de utilizo el modulo profile de python que ofrece un
    # reporte detallado de la ejecucion y donde se consume la mayor parte del tiempo para poder optimizarlo.

    # NOTA 2: Estos algoritmos son facilmente aplicables a cualquier lenguaje, ya que no se utiliza ninguna libreria
    # adicional ni helpers, unicamente arreglos, hashmaps(dict) y ciclos.
