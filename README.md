# Estructuras de Datos (Python)

Implementación formal de TDAs en Python con clases genéricas y pruebas de rendimiento, reportando tiempos en **milisegundos** y **ticks** (1 tick = 100 ns).

## Estructura del Proyecto

```text
├── Arreglos/
│   ├── TDA_Array.py            # Arreglo dinámico/básico (múltiples tipos)
│   ├── TDA_Array_Generica.py   # Arreglo con tipado genérico formal (Generic[T])
│   └── operaciones_arreglos.py # Medición de rendimiento (5, 10, 15 y 20 datos)
├── Pilas/
│   ├── TDA_Pila.py             # Implementación del TDA Pila (LIFO)
│   ├── TDA_Pila_Generica.py
│   └── operaciones_pilas.py    # Medición de rendimiento en Pila
├── .gitignore
└── README.md
```
# Ejecución de Pruebas
### Punto de Entrada Principal 
```bash
python main.py
```
### Para correr las mediciones de rendimiento de forma independiente:
```bash
# Probar Arreglos
python Arreglos/operaciones_arreglos.py

# Probar Pilas
python Pilas/operaciones_pilas.py
```