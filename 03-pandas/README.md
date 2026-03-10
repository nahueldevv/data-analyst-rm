
# Manipulación de Datos con Pandas

**Pandas** es la librería estándar de la industria para el análisis, limpieza y manipulación de datos en Python. Introduce estructuras de datos de alto nivel que permiten manejar tablas de forma similar a SQL o Excel, pero con la potencia de un lenguaje de programación.

> [!TIP]
> Mientras que **Numpy** se enfoca en el cálculo numérico puro, **Pandas** se enfoca en la estructuración y el etiquetado de datos (tablas con nombres de columnas y filas).

## 1. Estructuras de Datos Principales

1. **Series**: Un arreglo unidimensional (1D) etiquetado. Es como una sola columna de una tabla.
2. **DataFrame**: Una estructura de datos bidimensional (2D) similar a una tabla. Es una colección de Series que comparten el mismo índice.

## 2. Ingesta de Datos (Data Ingestion)

Pandas puede conectarse a múltiples fuentes de datos.

```python
import pandas as pd

# Leer desde un CSV
df = pd.read_csv('dataset.csv')

# Leer desde Excel (requiere openpyxl)
df_excel = pd.read_excel('reporte.xlsx')

# Leer desde un JSON o API
df_json = pd.read_json('datos.json')

```

## 3. Exploración Inicial (Inspección)

Antes de operar, debemos entender qué contienen nuestros datos.

| Metodo | Descripción |
| --- | --- |
| `df.head(n)` | Muestra las primeras `n` filas (por defecto 5). |
| `df.tail()` | Muestra las últimas filas. |
| `df.info()` | Muestra tipos de datos, memoria usada y valores no-nulos. |
| `df.describe()` | Genera estadísticas (media, min, max, cuartiles). |
| `df.shape` | Retorna una tupla con `(filas, columnas)`. |

## 4. Selección y Filtrado (Indexing)

Pandas ofrece formas potentes de acceder a la información:

### Selección de columnas

```python
columna = df['NombreColumna']          # Devuelve una Series
sub_tabla = df[['Col1', 'Col2']]       # Devuelve un DataFrame

```

### Selección por etiquetas vs posición

* **`df.loc[]`**: Acceso mediante **nombres** de etiquetas.
* **`df.iloc[]`**: Acceso mediante **índices numéricos** (como en Numpy).

---

## 5. Limpieza de Datos (Data Wrangling)

> [!IMPORTANT]
> El análisis de datos real es 80% limpieza. Los datos suelen venir con valores faltantes (`NaN`) o duplicados.

* **Valores Nulos:**
* `df.isnull().sum()`: Identifica cuántos nulos hay por columna.
* `df.dropna()`: Elimina filas con nulos.
* `df.fillna(valor)`: Rellena los huecos con un valor específico.


* **Duplicados:**
* `df.duplicated().any()`: Verifica si hay filas idénticas.
* `df.drop_duplicates()`: Limpia el dataset de repeticiones.


## 6. Operaciones y Filtrado Condicional

Puedes filtrar datos usando lógica booleana, como en Numpy:

```python
# Filtrar filas donde la columna 'Edad' sea mayor a 18
adultos = df[df['Edad'] > 18]

# Filtrar con múltiples condiciones (& para AND, | para OR)
filtro = df[(df['Salario'] > 2000) & (df['Departamento'] == 'IT')]

```

> [!WARNING]
> Ten cuidado con las copias: Muchos métodos en Pandas devuelven un nuevo objeto. Si quieres modificar el original, asegúrate de reasignarlo: `df = df.dropna()`.

