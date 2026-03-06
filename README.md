# Data Analyst Roadmap & Practice

Este repositorio posee conceptos y un laboratorio de prácticas basado en el [Data Analyst Roadmap de roadmap.sh](https://roadmap.sh/data-analyst). El objetivo es documentar la teoría fundamental y aplicar conceptos de análisis de datos utilizando el ecosistema de Python.

> [!TIP]
> **Propósito del Proyecto:** Este repositorio sirve como portafolio y guía de consulta rápida para dominar procesos de **ETL** (Extract, Transform, Load) y **EDA** (Exploratory Data Analysis).

## 🚀 Estructura del Repositorio

El proyecto está organizado de forma modular para seguir una progresión lógica, desde los conceptos teóricos hasta la implementación de librerías especializadas.

* **`01-Introduction/`**: Conceptos básicos, el rol del analista, tipos de análisis y ciclo de vida del dato.
* **`02-Numpy/`**: Fundamentos de computación numérica, manejo de arrays y álgebra lineal básica.
* **`03-Pandas/`**: Manipulación de DataFrames, limpieza de datos, filtrado y agregaciones.
* **`04-Visualization/`**: Creación de historias visuales con Matplotlib y Seaborn.
* **`05-Statistics/`**: Aplicación de estadística descriptiva e inferencial con Python.
* **`06-Projects/`**: Casos de estudio reales integrando todas las herramientas anteriores.

> [!NOTE]
> Cada carpeta de librerías (`02` al `04`) contiene archivos `.md` para la teoría y archivos `.ipynb` o `.py` para la ejecución de código práctico.

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.x
* **Gestor de Entorno:** Pipenv
* **Librerías Principales:**
  * `numpy`: Procesamiento de vectores y matrices.
  * `pandas`: Análisis y manipulación de estructuras de datos.
  * `matplotlib` / `seaborn`: Visualización de datos.
  * `jupyter`: Entorno interactivo para experimentación.

## 📦 Configuración del Entorno

Este proyecto utiliza **Pipenv** para la gestión de dependencias y el entorno virtual.

1. **Instalar Pipenv** (si no lo tienes):
    ```bash
    pip install pipenv
    ```

2. **Instalar dependencias**
    ```bash
    pipenv install --dev
    ```

3. **Activar el entorno**
    ```bash
    pipenv shell
    ```

> [!IMPORTANT]
> Si planeas visualizar los gráficos de Matplotlib dentro de VS Code, asegúrate de tener instalada la extensión de **Jupyter** y seleccionar el kernel del entorno creado por Pipenv.

> [!WARNING]
> Los datasets de gran tamaño (.csv, .xlsx) no se suben al repositorio. Consulta el archivo `.gitignore` para más detalles.