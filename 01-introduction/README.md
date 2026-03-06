# Introducción al Análisis de Datos

En esta sección se exploran los fundamentos teóricos que definen el rol del Analista de Datos y el flujo de trabajo estándar en la industria.

> [!TIP]
> El análisis de datos no se trata de usar herramientas, sino de **responder preguntas de negocio** usando evidencia numérica.

---

## 1. ¿Qué es un Analista de Datos?

Es el profesional encargado de recolectar, procesar y realizar estudios estadísticos de datos para obtener insights (visiones o conocimientos) que ayuden a la toma de decisiones.

### 🛠️ Responsabilidades Principales
* **Limpieza de datos:** Transformar datos "sucios" en formatos utilizables.
* **Exploración (EDA):** Identificar patrones, tendencias y valores atípicos (outliers).
* **Comunicación:** Traducir hallazgos técnicos a un lenguaje que cualquier stakeholder pueda entender.

---

## 2. Tipos de Análisis de Datos

Existen cuatro niveles de análisis, cada uno con un mayor grado de complejidad y valor:

| Tipo | Pregunta que responde | Ejemplo Práctico |
| :--- | :--- | :--- |
| **Descriptivo** | ¿Qué pasó? | Informe de ventas mensuales. |
| **Diagnóstico** | ¿Por qué pasó? | Analizar por qué bajó el tráfico en la web. |
| **Predictivo** | ¿Qué es probable que pase? | Pronóstico de demanda para el próximo año. |
| **Prescriptivo** | ¿Cómo podemos hacer que pase? | Recomendación de precios para maximizar margen. |

> [!NOTE]
> Como Analista de Datos Junior, te enfocarás principalmente en el análisis **Descriptivo** y **Diagnóstico**.

---

## 3. El Ciclo de Vida del Dato (Workflow)

Para que un análisis sea profesional y reproducible, seguimos estos pasos:

1. **Definición del Problema:** Entender qué queremos resolver.
2. **Ingesta de Datos:** Extraer datos de SQL, CSV, APIs o Excel.
3. **Limpieza (Wrangling):** Manejar valores nulos, duplicados y errores de formato.
4. **Análisis Exploratorio (EDA):** Aplicar estadística descriptiva y visualización.
5. **Conclusión y Reporte:** Presentar los resultados finales.

---

## 4. Conceptos Estadísticos Clave

Para usar librerías como `Numpy` o `Pandas`, debemos entender:

### Medidas de Tendencia Central
* **Media:** El promedio aritmético.
* **Mediana:** El valor central (resistente a valores extremos).
* **Moda:** El valor que más se repite.

### Medidas de Dispersión
* **Desviación Estándar:** Qué tan alejados están los datos respecto a la media.
* **Varianza:** La variabilidad de los datos.

> [!IMPORTANT]
> **Correlación no implica Causalidad.** Que dos variables se muevan juntas no significa que una cause la otra.

---

## 5. Glosario Rápido del Sector

* **Dataset:** Conjunto de datos organizado (usualmente una tabla).
* **Feature (Característica):** Una columna en tu tabla (variable).
* **Observation (Observación):** Una fila en tu tabla (registro).
* **Outlier:** Un valor que se aleja drásticamente del resto (un error o una anomalía).

---
> [!WARNING]
> Nunca empieces a limpiar datos sin antes entender el contexto del negocio. Los números sin contexto son solo ruido.