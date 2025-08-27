# 🔤 Calculadora de Lenguajes Formales

Una aplicación web interactiva desarrollada con Streamlit para realizar operaciones con lenguajes formales, conjuntos, alfabetos y palabras.

## 🌐 Repositorio GitHub
📂 **Repositorio oficial**: https://github.com/CristianHuertas/calculadora_automatas.git

## ⚡ Inicio Rápido

1. 📎 **Descargar**: Clona o descarga este repositorio
2. 🔄 **Ejecutar**: Haz doble clic en `ejecutar.bat`
3. 🌐 **Usar**: Se abre automáticamente en tu navegador
4. 🎉 **¡Listo!**: Ya puedes usar la calculadora

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
- **Python 3.8 o superior** (descarga desde https://python.org)
- Asegúrate de marcar **"Add to PATH"** durante la instalación de Python

### Instalación

1. **Descargar el proyecto**
   ```bash
   # Clonar desde GitHub
   git clone https://github.com/CristianHuertas/calculadora_automatas.git
   cd calculadora_automatas
   
   # O descargar directamente desde GitHub como ZIP
   ```

2. **🎯 MÉTODO MÁS FÁCIL: Ejecutar directamente**
   - **Hacer doble clic en `ejecutar.bat`** ✨
   - El script instalará automáticamente las dependencias si es necesario
   - La aplicación se abrirá automáticamente en tu navegador

3. **Métodos alternativos**
   ```bash
   # Opción 1: PowerShell
   .\ejecutar.ps1
   
   # Opción 2: Instalación manual
   pip install -r requirements.txt
   streamlit run app.py
   ```

4. **Acceder a la aplicación**
   - 🌐 La aplicación se abrirá automáticamente en `http://localhost:8501`
   - Si no se abre automáticamente, copia esa URL en tu navegador
   - ⛔ Para cerrar: presiona `Ctrl+C` en la ventana de comandos

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
