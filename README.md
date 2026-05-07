# Valoración de Inversión con Riesgo de Truncamiento (Modelo Damodaran)

Este repositorio contiene un modelo de valoración dinámica que integra **Finanzas Corporativas** y **Simulación de Montecarlo** para capturar el riesgo de supervivencia en proyectos de inversión, basado en el marco teórico de **Aswath Damodaran** (*"The Cost of Distress: Survival, Truncation Risk and Valuation"*).

## 📈 Contexto Financiero
El modelo tradicional de Flujo de Caja Descontado (DCF) suele sufrir de un "punto ciego": el sesgo de continuidad (*Going Concern*). Este proyecto rompe con ese sesgo al modelar la posibilidad de que un proyecto no alcance su valor terminal debido a crisis de liquidez.

### Conceptos Clave Implementados:
* **Riesgo de Truncamiento:** Si el proyecto se queda sin caja, los flujos futuros se anulan irreversibilmente.
* **Valor de Liquidación ("Fire Sale"):** En caso de quiebra, se asume la venta de activos a precio de remate en lugar de su valor contable.
* **Autosustento:** El trigger de quiebra se activa si la liquidez acumulada es negativa, evaluando la capacidad del proyecto de sobrevivir sin inyecciones externas de capital.

## 🛠️ Herramientas Utilizadas
* **Python (Numpy):** Para el motor estadístico de 10,000 iteraciones.
* **Excel:** Como interfaz de flujos de caja y reportes.
* **Xlwings:** Para la integración en tiempo real entre el motor de Python y el modelo financiero en Excel.

## 📊 Resultados de la Simulación
Tras estresar el modelo con 10,000 escenarios, se obtuvieron los siguientes resultados:

| Métrica | Valor |
| :--- | :--- |
| **Probabilidad de Supervivencia** | 97.0% |
| **Probabilidad de Quiebra (Distress)** | 3.0% |
| **VAN Esperado (Escenarios Supervivencia)** | $15,866.90 |
| **VAN Esperado (Escenarios Quiebra)** | -$20,878.98 |
| **VAN Esperado Final (Ponderado)** | **$14,838.02** |

## 📁 Estructura del Repositorio
* `main.py`: Script de Python con la lógica de simulación y conexión a Excel.
* `Proyectos de inversion.xlsx`: Modelo financiero con el Flujo de Caja Libre y cálculos de liquidación.

## 🚀 Instrucciones
1. Clonar el repositorio.
2. Abrir el archivo `Proyectos de inversion.xlsx`.
3. Ejecutar `main.py`. El script actualizará automáticamente las celdas de Excel, recalculará el modelo para cada iteración y almacenará los resultados en memoria para el análisis final.

---
**Autor:** Pablo Fernando Ortiz Pinell  
**Inspiración:** Marco teórico de Aswath Damodaran sobre el costo del distrés financiero.
