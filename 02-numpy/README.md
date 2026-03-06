# Computación Numérica con Numpy

**NumPy** (Numerical Python) es la librería fundamental para el cómputo científico en Python. Proporciona estructuras de datos de arreglos de alto rendimiento y herramientas para trabajar con ellos.

> [!TIP]
> **¿Por qué usar Numpy y no listas de Python?** Las listas de Python son flexibles pero lentas. Los arreglos de Numpy (`ndarrays`) son hasta **50 veces más rápidos** porque almacenan los datos de forma contigua en memoria y están escritos en C.

---

## 1. El Concepto de `ndarray`

El objeto principal es el arreglo multidimensional (N-dimensional array).

* **1D (Vector):** Una sola fila o columna.
* **2D (Matriz):** Filas y columnas (como una tabla).
* **3D o más (Tensor):** Arreglos anidados (como imágenes en color RGB).

### Atributos clave de un array:
* `.shape`: Dimensiones del arreglo (ej: `(3, 4)` para 3 filas y 4 columnas).
* `.dtype`: Tipo de dato (int64, float64, etc.). Todos los elementos de un array de Numpy **deben ser del mismo tipo**.
* `.size`: Cantidad total de elementos.

---

## 2. Creación de Arreglos

Numpy ofrece métodos rápidos para generar datos:

* `np.array([1, 2, 3])`: Crea un array desde una lista.
* `np.zeros((3, 3))`: Crea una matriz llena de ceros.
* `np.ones((2, 2))`: Crea una matriz llena de unos.
* `np.arange(0, 10, 2)`: Crea una secuencia (0, 2, 4, 6, 8).
* `np.linspace(0, 1, 5)`: Crea 5 números equitativamente espaciados entre 0 y 1.

---

## 3. Operaciones Vectorizadas (Broadcasting)

A diferencia de las listas, puedes hacer operaciones matemáticas directamente sobre el objeto sin usar bucles `for`.

* **Suma:** `arr + 10` (Suma 10 a cada elemento).
* **Multiplicación:** `arr * 2`.
* **Producto Matricial:** `np.dot(A, B)` o el operador `@`.

> [!IMPORTANT]
> **Broadcasting:** Es la capacidad de Numpy de realizar operaciones entre arreglos de diferentes formas (shapes), siempre que sean compatibles.

---

## 4. Indexación y Slicing (Rebanado)

Funciona de forma similar a las listas pero en múltiples dimensiones:

* `arr[0, 1]`: Accede a la fila 0, columna 1.
* `arr[:, 1]`: Accede a **todas** las filas de la columna 1.
* `arr[arr > 5]`: **Indexación Booleana**. Devuelve solo los elementos que cumplen la condición.

---

## 5. Funciones Estadísticas Integradas

Numpy permite realizar cálculos sobre ejes (`axis`):
* `axis=0`: Operaciones hacia abajo (columnas).
* `axis=1`: Operaciones hacia los lados (filas).

| Función | Descripción |
| :--- | :--- |
| `np.mean()` | Media aritmética. |
| `np.median()` | Mediana. |
| `np.std()` | Desviación estándar. |
| `np.sum()` | Suma total. |

---

> [!WARNING]
> Numpy está optimizado para números. Si intentas meter un string en un array de números, Numpy convertirá todo a strings (Upcasting), perdiendo la capacidad de hacer cálculos matemáticos.
