import streamlit as st
from fractions import Fraction

st.set_page_config(page_title="Gauss–Jordan Paso a Paso", layout="wide")

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
    return r"\left[\begin{array}{ccc|c}" + cuerpo + r"\end{array}\right]"


pasos = [
    {
        "texto": "Paso 1 — Matriz aumentada inicial.",
        "matriz": [
            [2, 1, -3, 5],
            [3, -2, 2, 6],
            [5, -3, -1, 16]
        ]
    },
    {
        "texto": "Paso 2 — Normalizamos F1 → ½F1.",
        "matriz": [
            [1, 1/2, -3/2, 5/2],
            [3, -2, 2, 6],
            [5, -3, -1, 16]
        ]
    },
    {
        "texto": "Paso 3 — Eliminamos abajo del pivote 1.",
        "matriz": [
            [1, 1/2, -3/2, 5/2],
            [0, -7/2, 13/2, -3/2],
            [0, -11/2, 13/2, 7/2]
        ]
    },
    {
        "texto": "Paso 4 — Normalizamos F2 → (-2/7)F2.",
        "matriz": [
            [1, 1/2, -3/2, 5/2],
            [0, 1, -13/7, 3/7],
            [0, -11/2, 13/2, 7/2]
        ]
    },
    {
        "texto": "Paso 5 — Eliminamos entrada de F3.",
        "matriz": [
            [1, 1/2, -3/2, 5/2],
            [0, 1, -13/7, 3/7],
            [0, 0, -26/7, 41/7]
        ]
    },
    {
        "texto": "Paso 6 — Normalizamos F3 → (-7/26)F3.",
        "matriz": [
            [1, 1/2, -3/2, 5/2],
            [0, 1, -13/7, 3/7],
            [0, 0, 1, -41/26]
        ]
    },
    {
        "texto": "Paso 7 — Eliminamos hacia arriba.",
        "matriz": [
            [1, 0, 0, 18/13],
            [0, 1, 0, -5/2],
            [0, 0, 1, -41/26]
        ]
    }
]

if "i" not in st.session_state:
    st.session_state.i = 0

st.title("📘 Método de Gauss–Jordan — Animación Paso a Paso")

col1, col2, col3 = st.columns([1,1,1])

with col1:
    if st.button("⏮ Paso anterior"):
        if st.session_state.i > 0:
            st.session_state.i -= 1
            st.rerun()

with col2:
    if st.button("▶ Reproducir animación"):
        for k in range(len(pasos)):
            st.session_state.i = k
            st.rerun()

with col3:
    if st.button("⏭ Siguiente paso"):
        if st.session_state.i < len(pasos)-1:
            st.session_state.i += 1
            st.rerun()

paso = pasos[st.session_state.i]

st.subheader(f"Paso {st.session_state.i + 1} de {len(pasos)}")
st.info(paso["texto"])

st.latex(matriz_a_latex(paso["matriz"]))

if st.session_state.i == len(pasos)-1:
    st.success(
        r"""
        \textbf{Solución final del sistema: } \\
        x = \frac{18}{13}, \qquad
        y = -\frac{5}{2}, \qquad
        z = -\frac{41}{26}
        """
    )
