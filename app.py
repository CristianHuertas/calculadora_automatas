import streamlit as st
import itertools
from typing import Set, List, Union

# Configuración de la página
st.set_page_config(
    page_title="Calculadora de Lenguajes Formales",
    page_icon="🔤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Funciones auxiliares para operaciones con conjuntos
def parse_set(input_str: str) -> set:
    """Convierte una cadena en un conjunto de Python."""
    if not input_str.strip():
        return set()
    
    # Limpieza básica de entrada
    input_str = input_str.strip()
    if input_str.startswith('{') and input_str.endswith('}'):
        input_str = input_str[1:-1]
    
    # Separar elementos por coma y limpiar espacios
    elements = [elem.strip() for elem in input_str.split(',') if elem.strip()]
    return set(elements)

def format_set(s: set) -> str:
    """Formatea un conjunto para mostrar en pantalla."""
    if not s:
        return "∅"
    return "{" + ", ".join(sorted(s)) + "}"

# Operaciones con conjuntos/alfabetos
def union(A: set, B: set) -> set:
    """Unión de dos conjuntos."""
    return A | B

def intersection(A: set, B: set) -> set:
    """Intersección de dos conjuntos."""
    return A & B

def difference(A: set, B: set) -> set:
    """Diferencia de dos conjuntos A - B."""
    return A - B

def symmetric_difference(A: set, B: set) -> set:
    """Diferencia simétrica de dos conjuntos."""
    return A ^ B

def complement(A: set, universe: set) -> set:
    """Complemento de A respecto al universo."""
    return universe - A

# Operaciones con palabras/cadenas
def concatenate_words(w1: str, w2: str) -> str:
    """Concatena dos palabras."""
    return w1 + w2

def word_power(word: str, n: int) -> str:
    """Calcula la potencia n de una palabra."""
    if n == 0:
        return ""  # Palabra vacía (epsilon)
    return word * n

def word_reverse(word: str) -> str:
    """Calcula la reflexión (inversa) de una palabra."""
    return word[::-1]

def word_length(word: str) -> int:
    """Calcula la longitud de una palabra."""
    return len(word)

# Operaciones con lenguajes
def language_concatenation(L1: set, L2: set) -> set:
    """Concatenación de dos lenguajes."""
    if not L1 or not L2:
        return set()
    
    result = set()
    for w1 in L1:
        for w2 in L2:
            result.add(w1 + w2)
    return result

def language_power(L: set, n: int) -> set:
    """Calcula la potencia n de un lenguaje."""
    if n == 0:
        return {""}  # Lenguaje que contiene solo la palabra vacía
    
    if not L:
        return set()
    
    result = L.copy()
    for i in range(1, n):
        result = language_concatenation(result, L)
    
    return result

def language_reverse(L: set) -> set:
    """Calcula la reflexión de un lenguaje."""
    return {word_reverse(w) for w in L}

def kleene_closure(L: set, max_iterations: int = 5) -> set:
    """Calcula la clausura de Kleene de un lenguaje."""
    if not L:
        return {""}  # L* = {ε} cuando L = ∅
    
    result = {""}  # Siempre incluye la palabra vacía
    current_power = L.copy()
    
    for i in range(1, max_iterations + 1):
        result.update(current_power)
        if i < max_iterations:
            current_power = language_concatenation(current_power, L)
    
    return result

def positive_closure(L: set, max_iterations: int = 5) -> set:
    """Calcula la clausura positiva de un lenguaje."""
    if not L:
        return set()
    
    result = set()
    current_power = L.copy()
    
    for i in range(1, max_iterations + 1):
        result.update(current_power)
        if i < max_iterations:
            current_power = language_concatenation(current_power, L)
    
    return result

# Interfaz principal de Streamlit
def main():
    st.title("🔤 Calculadora de Lenguajes Formales")
    st.markdown("---")
    
    # Sidebar para seleccionar tipo de operación
    st.sidebar.title("Seleccionar Operación")
    
    operation_type = st.sidebar.radio(
        "Tipo de operación:",
        ["Operaciones con Conjuntos/Alfabetos",
         "Operaciones con Palabras/Cadenas",
         "Operaciones con Lenguajes"]
    )
    
    if operation_type == "Operaciones con Conjuntos/Alfabetos":
        handle_set_operations()
    elif operation_type == "Operaciones con Palabras/Cadenas":
        handle_word_operations()
    else:
        handle_language_operations()

def handle_set_operations():
    """Maneja las operaciones con conjuntos/alfabetos."""
    st.header("📊 Operaciones con Conjuntos/Alfabetos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Conjunto A")
        set_A_input = st.text_input(
            "Ingresa el conjunto A (separado por comas):",
            value="a,b,c",
            key="set_A"
        )
        set_A = parse_set(set_A_input)
        st.write(f"A = {format_set(set_A)}")
    
    with col2:
        st.subheader("Conjunto B")
        set_B_input = st.text_input(
            "Ingresa el conjunto B (separado por comas):",
            value="b,c,d",
            key="set_B"
        )
        set_B = parse_set(set_B_input)
        st.write(f"B = {format_set(set_B)}")
    
    # Operación seleccionada
    operation = st.selectbox(
        "Selecciona la operación:",
        ["Unión (A ∪ B)",
         "Intersección (A ∩ B)", 
         "Diferencia (A - B)",
         "Diferencia Simétrica (A Δ B)",
         "Complemento de A"]
    )
    
    # Calcular resultado
    if operation == "Unión (A ∪ B)":
        result = union(set_A, set_B)
        st.success(f"A ∪ B = {format_set(result)}")
        
    elif operation == "Intersección (A ∩ B)":
        result = intersection(set_A, set_B)
        st.success(f"A ∩ B = {format_set(result)}")
        
    elif operation == "Diferencia (A - B)":
        result = difference(set_A, set_B)
        st.success(f"A - B = {format_set(result)}")
        
    elif operation == "Diferencia Simétrica (A Δ B)":
        result = symmetric_difference(set_A, set_B)
        st.success(f"A Δ B = {format_set(result)}")
        
    elif operation == "Complemento de A":
        universe_input = st.text_input(
            "Ingresa el conjunto universo U:",
            value="a,b,c,d,e,f",
            key="universe"
        )
        universe = parse_set(universe_input)
        st.write(f"U = {format_set(universe)}")
        
        result = complement(set_A, universe)
        st.success(f"A' = {format_set(result)}")

def handle_word_operations():
    """Maneja las operaciones con palabras/cadenas."""
    st.header("📝 Operaciones con Palabras/Cadenas")
    
    operation = st.selectbox(
        "Selecciona la operación:",
        ["Concatenación de dos palabras",
         "Potencia de una palabra",
         "Reflexión (palabra inversa)",
         "Longitud de una palabra"]
    )
    
    if operation == "Concatenación de dos palabras":
        col1, col2 = st.columns(2)
        
        with col1:
            word1 = st.text_input("Palabra 1:", value="abc", key="word1_concat")
            
        with col2:
            word2 = st.text_input("Palabra 2:", value="def", key="word2_concat")
        
        result = concatenate_words(word1, word2)
        st.success(f"'{word1}' · '{word2}' = '{result}'")
        
    elif operation == "Potencia de una palabra":
        word = st.text_input("Palabra:", value="ab", key="word_power")
        power = st.number_input("Potencia (n):", min_value=0, max_value=10, value=3, key="power_n")
        
        result = word_power(word, power)
        if power == 0:
            st.success(f"'{word}'^{power} = 'ε' (palabra vacía)")
        else:
            st.success(f"'{word}'^{power} = '{result}'")
        
    elif operation == "Reflexión (palabra inversa)":
        word = st.text_input("Palabra:", value="abcd", key="word_reverse")
        result = word_reverse(word)
        st.success(f"Reflexión de '{word}' = '{result}'")
        
    elif operation == "Longitud de una palabra":
        word = st.text_input("Palabra:", value="hello", key="word_length")
        length = word_length(word)
        st.success(f"|'{word}'| = {length}")

def handle_language_operations():
    """Maneja las operaciones con lenguajes."""
    st.header("🔤 Operaciones con Lenguajes")
    
    operation = st.selectbox(
        "Selecciona la operación:",
        ["Concatenación de lenguajes (L₁ · L₂)",
         "Potencia de un lenguaje (L^n)",
         "Reflexión de un lenguaje",
         "Unión de lenguajes (L₁ ∪ L₂)",
         "Intersección de lenguajes (L₁ ∩ L₂)",
         "Diferencia de lenguajes (L₁ - L₂)",
         "Clausura de Kleene (L*)",
         "Clausura Positiva (L⁺)"]
    )
    
    if operation in ["Concatenación de lenguajes (L₁ · L₂)", 
                     "Unión de lenguajes (L₁ ∪ L₂)",
                     "Intersección de lenguajes (L₁ ∩ L₂)",
                     "Diferencia de lenguajes (L₁ - L₂)"]:
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Lenguaje L₁")
            L1_input = st.text_input(
                "Ingresa L₁ (palabras separadas por comas):",
                value="a,aa,aba",
                key="L1"
            )
            L1 = parse_set(L1_input)
            st.write(f"L₁ = {format_set(L1)}")
        
        with col2:
            st.subheader("Lenguaje L₂")
            L2_input = st.text_input(
                "Ingresa L₂ (palabras separadas por comas):",
                value="b,ab",
                key="L2"
            )
            L2 = parse_set(L2_input)
            st.write(f"L₂ = {format_set(L2)}")
        
        if operation == "Concatenación de lenguajes (L₁ · L₂)":
            result = language_concatenation(L1, L2)
            st.success(f"L₁ · L₂ = {format_set(result)}")
            
        elif operation == "Unión de lenguajes (L₁ ∪ L₂)":
            result = union(L1, L2)
            st.success(f"L₁ ∪ L₂ = {format_set(result)}")
            
        elif operation == "Intersección de lenguajes (L₁ ∩ L₂)":
            result = intersection(L1, L2)
            st.success(f"L₁ ∩ L₂ = {format_set(result)}")
            
        elif operation == "Diferencia de lenguajes (L₁ - L₂)":
            result = difference(L1, L2)
            st.success(f"L₁ - L₂ = {format_set(result)}")
    
    else:
        # Operaciones que requieren un solo lenguaje
        L_input = st.text_input(
            "Ingresa el lenguaje L (palabras separadas por comas):",
            value="a,b",
            key="L_single"
        )
        L = parse_set(L_input)
        st.write(f"L = {format_set(L)}")
        
        if operation == "Potencia de un lenguaje (L^n)":
            power = st.number_input("Potencia (n):", min_value=0, max_value=5, value=2, key="lang_power")
            result = language_power(L, power)
            st.success(f"L^{power} = {format_set(result)}")
            
        elif operation == "Reflexión de un lenguaje":
            result = language_reverse(L)
            st.success(f"L^R = {format_set(result)}")
            
        elif operation == "Clausura de Kleene (L*)":
            max_iter = st.number_input(
                "Número máximo de iteraciones:", 
                min_value=1, max_value=8, value=4, 
                key="kleene_iter"
            )
            result = kleene_closure(L, max_iter)
            st.success(f"L* (hasta {max_iter} iteraciones) = {format_set(result)}")
            st.info("Nota: L* es infinito, se muestran solo las primeras iteraciones.")
            
        elif operation == "Clausura Positiva (L⁺)":
            max_iter = st.number_input(
                "Número máximo de iteraciones:", 
                min_value=1, max_value=8, value=4, 
                key="positive_iter"
            )
            result = positive_closure(L, max_iter)
            st.success(f"L⁺ (hasta {max_iter} iteraciones) = {format_set(result)}")
            st.info("Nota: L⁺ es infinito, se muestran solo las primeras iteraciones.")

    # Ejemplos y ayuda
    with st.expander("💡 Ejemplos y Ayuda"):
        st.markdown("""
        ### Ejemplos de entrada:
        
        **Conjuntos/Alfabetos:**
        - `a,b,c` → {a, b, c}
        - `0,1` → {0, 1}
        
        **Palabras:**
        - `abc` → cadena "abc"
        - ` ` (vacío) → palabra vacía (ε)
        
        **Lenguajes:**
        - `a,aa,aaa` → {a, aa, aaa}
        - `ab,ba` → {ab, ba}
        - ` ` (vacío) → lenguaje vacío ∅
        
        ### Notación:
        - ∅: conjunto/lenguaje vacío
        - ε: palabra vacía (cadena de longitud 0)
        - L*: clausura de Kleene (incluye ε)
        - L⁺: clausura positiva (no incluye ε)
        """)

if __name__ == "__main__":
    main()
