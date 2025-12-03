import streamlit as st
from fractions import Fraction

st.set_page_config(page_title="Gauss–Jordan Paso a Paso", layout="wide")

# ============================================================
# FUNCIÓN: convierte matriz numérica a LaTeX con fracciones
# ============================================================
def matriz_a_latex(M):
    filas = []
    for fila in M:
        celdas = []
        for v in fila:
            frac = Fraction(v).limit_denominator()
            if frac.denominator == 1:
                celdas.append(str(frac.numerator))
            else:
                celdas.append(rf"\frac{{{frac.numerator}}}{{{frac.denominator}}}")
        filas.append(" & ".join(celdas))
    cuerpo = r" \\".join(filas)
    return r"\left[\begin{array}{cccc|c}" + cuerpo + r"\end{array}\right]"


# ============================================================
# MATRICES DEL EJERCICIO PASO A PASO (las del PDF EXACTAS)
# ============================================================

pasos = [
    # --- Paso 1: Matriz original ---
    {
        "texto": "Paso 1 — Matriz aumentada inicial del sistema.",
        "matriz": [
            [2, 1, -3, 5],
            [3, -2, 2, 6],
            [5, -3, -1, 16]
        ]
    },

    # --- Paso 2: F1 → 1/2 F1 ---
    {
        "texto": "Paso 2 — Normalizamos el pivote 1. Operación:  F1 → ½ F1.",
        "matriz": [
            [1, 1/2, -3/2, 5/2],
            [3, -2, 2, 6],
            [5, -3, -1, 16]
        ]
    },

    # --- Paso 3: Eliminación debajo del pivote 1 ---
    {
        "texto": "Paso 3 — Eliminamos entradas debajo del pivote 1. Operaciones: F2 → F2 - 3F1,  F3 → F3 - 5F1.",
        "matriz": [
            [1, 1/2, -3/2, 5/2],
            [0, -7/2, 13/2, -3/2],
            [0, -11/2, 13/2, 7/2]
        ]
    },

    # --- Paso 4: Normalizamos pivote 2 ---
    {
        "texto": "Paso 4 — Normalizamos el pivote 2. Operación: F2 → (-2/7) F2.",
        "matriz": [
            [1, 1/2, -3/2, 5/2],
            [0, 1, -13/7, 3/7],
            [0, -11/2, 13/2, 7/2]
        ]
    },

    # --- Paso 5: Eliminación debajo del pivote 2 ---
    {
        "texto": "Paso 5 — Eliminamos entrada debajo del pivote 2. Operación: F3 → F3 + (11/2)F2.",
        "matriz": [
            [1, 1/2, -3/2, 5/2],
            [0, 1, -13/7, 3/7],
            [0, 0, -26/7, 41/7]
        ]
    },

    # --- Paso 6: Normalizamos pivote 3 ---
    {
        "texto": "Paso 6 — Normalizamos pivote 3. Operación: F3 → (-7/26) F3.",
        "matriz": [
            [1, 1/2, -3/2, 5/2],
            [0, 1, -13/7, 3/7],
            [0, 0, 1, -41/26]
        ]
    },

    # --- Paso 7: Eliminamos arriba del pivote 3 ---
    {
        "texto": "Paso 7 — Eliminamos entradas arriba del pivote 3. Operaciones: F2 → F2 + (13/7)F3,  F1 → F1 + (3/2)F3.",
        "matriz": [
            [1, 0, 0, 18/13],
            [0, 1, 0, -5/2],
            [0, 0, 1, -41/26]
        ]
    }
]


# ============================================================
# CONTROL DE ESTADO
# ============================================================
if "i" not in st.session_state:
    st.session_state.i = 0


# ============================================================
# TÍTULO
# ============================================================
st.title("📘 Método de Gauss–Jordan — Animación Paso a Paso")


# ============================================================
# BOTONES DE CONTROL
# ============================================================
col1, col2, col3 = st.columns([1,1,1])

with col1:
    if st.button("⏮ Paso anterior"):
        if st.session_state.i > 0:
            st.session_state.i -= 1

with col2:
    if st.button("▶ Reproducir animación"):
        for k in range(len(pasos)):
            st.session_state.i = k
            st.experimental_rerun()

with col3:
    if st.button("⏭ Siguiente paso"):
        if st.session_state.i < len(pasos)-1:
            st.session_state.i += 1


# ============================================================
# MOSTRAR PASO ACTUAL
# ============================================================
paso = pasos[st.session_state.i]

st.subheader(f"Paso {st.session_state.i + 1} de {len(pasos)}")
st.info(paso["texto"])

st.latex(matriz_a_latex(paso["matriz"]))


# ============================================================
# SI ES EL ÚLTIMO PASO, MOSTRAR SOLUCIÓN
# ============================================================
if st.session_state.i == len(pasos)-1:

    st.success(
        r"""
        \textbf{Solución final del sistema: } \\
        x = \frac{18}{13}, \qquad
        y = -\frac{5}{2}, \qquad
        z = -\frac{41}{26}
        """
    )
