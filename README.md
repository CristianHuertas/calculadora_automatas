# 🔤 Calculadora de Lenguajes Formales

Una aplicación web interactiva desarrollada con Streamlit para realizar operaciones con lenguajes formales, conjuntos, alfabetos y palabras.

## ✨ Funcionalidades

### 📊 Operaciones con Conjuntos/Alfabetos
- **Unión** (A ∪ B)
- **Intersección** (A ∩ B)
- **Diferencia** (A - B)
- **Diferencia Simétrica** (A Δ B)
- **Complemento** (A' respecto a un conjunto universal)

### 📝 Operaciones con Palabras/Cadenas
- **Concatenación** de dos palabras
- **Potencia** de una palabra (x⁰, x¹, x², ...)
- **Reflexión** (palabra inversa)
- **Longitud** de una palabra

### 🔤 Operaciones con Lenguajes
- **Concatenación** de lenguajes (L₁ · L₂)
- **Potencia** de un lenguaje (L², L³, ...)
- **Reflexión** de un lenguaje
- **Unión** de lenguajes (L₁ ∪ L₂)
- **Intersección** de lenguajes (L₁ ∩ L₂)
- **Diferencia** de lenguajes (L₁ - L₂)
- **Clausura de Kleene** (L*)
- **Clausura Positiva** (L⁺)

## 🚀 Instalación y Uso

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   # Si tienes el proyecto en un directorio
   cd calculadora_automatas
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación**
   ```bash
   streamlit run app.py
   ```

4. **Abrir en el navegador**
   - La aplicación se abrirá automáticamente en `http://localhost:8501`
   - Si no se abre automáticamente, copia esa URL en tu navegador

## 📖 Guía de Uso

### Formato de Entrada

#### Conjuntos y Alfabetos
- Separar elementos por comas: `a,b,c`
- Opcional usar llaves: `{a,b,c}`
- Ejemplo: `0,1` para el alfabeto binario

#### Palabras
- Ingresar directamente: `abc`
- Dejar vacío para la palabra vacía (ε)

#### Lenguajes
- Palabras separadas por comas: `a,aa,aba`
- Ejemplo: `ab,ba,abb` para un lenguaje de 3 palabras
- Dejar vacío para el lenguaje vacío (∅)

### Ejemplos de Operaciones

#### 🔍 Ejemplo: Concatenación de Lenguajes
- **L₁**: `a,aa,aba`
- **L₂**: `b,ab`
- **Resultado L₁ · L₂**: `{ab, aab, abab, aaab, abaab}`

#### 🔍 Ejemplo: Clausura de Kleene
- **L**: `a,b`
- **L*** (3 iteraciones): `{ε, a, b, aa, ab, ba, bb, aaa, aab, aba, abb, baa, bab, bba, bbb}`

#### 🔍 Ejemplo: Operaciones con Conjuntos
- **A**: `a,b,c`
- **B**: `b,c,d`
- **A ∪ B**: `{a, b, c, d}`
- **A ∩ B**: `{b, c}`
- **A - B**: `{a}`

## 🎯 Características Especiales

- **Interfaz Intuitiva**: Navegación fácil con pestañas y sidebar
- **Resultados en Tiempo Real**: Los cálculos se actualizan automáticamente
- **Límite Configurable**: Para clausuras infinitas (Kleene y Positiva)
- **Notación Matemática**: Uso de símbolos matemáticos correctos
- **Ejemplos Integrados**: Ayuda contextual con ejemplos de uso
- **Validación Robusta**: Manejo de entradas vacías y casos especiales

## 📚 Notación Utilizada

- **∅**: Conjunto o lenguaje vacío
- **ε**: Palabra vacía (cadena de longitud 0)
- **∪**: Unión
- **∩**: Intersección
- **-**: Diferencia
- **Δ**: Diferencia simétrica
- **'**: Complemento
- **·**: Concatenación
- **^n**: Potencia
- **^R**: Reflexión/Inversa
- **L***: Clausura de Kleene
- **L⁺**: Clausura positiva

## 🛠️ Tecnologías Utilizadas

- **Python 3.8+**
- **Streamlit**: Framework web para aplicaciones interactivas
- **Pandas**: Manipulación de datos
- **NumPy**: Operaciones numéricas

## 📝 Notas Técnicas

- Las clausuras de Kleene y positiva son infinitas por naturaleza, por lo que se limitan a un número configurable de iteraciones
- Todos los conjuntos se manejan internamente como `set` de Python para garantizar unicidad
- La aplicación maneja casos especiales como lenguajes vacíos y palabras vacías correctamente

---
**Desarrollado para el curso de Autómatas y Lenguajes Formales**
