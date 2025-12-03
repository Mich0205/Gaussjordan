import streamlit as st
from fractions import Fraction

st.set_page_config(page_title="Gauss–Jordan Animado", layout="wide")

# ===============================
# MATRICES DEL EJERCICIO
# ===============================
steps = [
    {
        "title": "Paso 1 — Matriz aumentada inicial",
        "explanation": "Tomamos el sistema del PDF y escribimos su matriz aumentada.",
        "matrix": r"""
        \left[
        \begin{array}{ccc|c}
        2 & 1 & -3 & 5 \\
        3 & -2 & 2 & 6 \\
        5 & -3 & -1 & 16
        \end{array}
        \right]
        """
    },
    {
        "title": "Paso 2 — F1 → (1/2)F1",
        "explanation": "Normalizamos el primer pivote dividiendo la fila 1 entre 2.",
        "matrix": r"""
        \left[
        \begin{array}{ccc|c}
        1 & 1/2 & -3/2 & 5/2 \\
        3 & -2 & 2 & 6 \\
        5 & -3 & -1 & 16
        \end{array}
        \right]
        """
    },
    {
        "title": "Paso 3 — Eliminamos abajo del pivote 1",
        "explanation": r"Aplicamos: F2 → F2 - 3F1 \quad y \quad F3 → F3 - 5F1",
        "matrix": r"""
        \left[
        \begin{array}{ccc|c}
        1 & 1/2 & -3/2 & 5/2 \\
        0 & -7/2 & 13/2 & -3/2 \\
        0 & -11/2 & 13/2 & 7/2
        \end{array}
        \right]
        """
    },
    {
        "title": "Paso 4 — F2 → -(2/7)F2",
        "explanation": "Normalizamos el pivote 2 dividiendo F2 entre su entrada pivote (-7/2).",
        "matrix": r"""
        \left[
        \begin{array}{ccc|c}
        1 & 1/2 & -3/2 & 5/2 \\
        0 & 1 & -13/7 & 3/7 \\
        0 & -11/2 & 13/2 & 7/2
        \end{array}
        \right]
        """
    },
    {
        "title": "Paso 5 — F3 → F3 + (11/2)F2",
        "explanation": "Eliminamos el término debajo del pivote 2.",
        "matrix": r"""
        \left[
        \begin{array}{ccc|c}
        1 & 1/2 & -3/2 & 5/2 \\
        0 & 1 & -13/7 & 3/7 \\
        0 & 0 & -26/7 & 41/7
        \end{array}
        \right]
        """
    },
    {
        "title": "Paso 6 — F3 → (-7/26)F3",
        "explanation": "Normalizamos el pivote 3.",
        "matrix": r"""
        \left[
        \begin{array}{ccc|c}
        1 & 1/2 & -3/2 & 5/2 \\
        0 & 1 & -13/7 & 3/7 \\
        0 & 0 & 1 & -41/26
        \end{array}
        \right]
        """
    },
    {
        "title": "Paso 7 — Eliminación hacia arriba",
        "explanation": r"Aplicamos: F2 → F2 + (13/7)F3 \quad y \quad F1 → F1 - (1/2)F2",
        "matrix": r"""
        \left[
        \begin{array}{ccc|c}
        1 & 0 & 0 & 18/13 \\
        0 & 1 & 0 & -5/2 \\
        0 & 0 & 1 & -41/26
        \end{array}
        \right]
        """
    }
]

# ===============================
# INTERFAZ
# ===============================

st.title("📘 Método de Gauss–Jordan — Animación Paso a Paso")
st.write("Ejercicio tomado del PDF que mostraste (exactamente el mismo procedimiento).")

# Estado persistente
if "step" not in st.session_state:
    st.session_state.step = 0
if "auto" not in st.session_state:
    st.session_state.auto = False

# Botones
cols = st.columns(3)
with cols[0]:
    if st.button("⬅ Paso anterior"):
        if st.session_state.step > 0:
            st.session_state.step -= 1
with cols[1]:
    if st.button("▶ Reproducir animación"):
        st.session_state.auto = True
with cols[2]:
    if st.button("➡ Siguiente paso"):
        if st.session_state.step < len(steps)-1:
            st.session_state.step += 1

# Mostrar paso actual
cp = st.session_state.step
st.subheader(f"Paso {cp+1} de {len(steps)}: {steps[cp]['title']}")
st.info(steps[cp]["explanation"])
st.latex(steps[cp]["matrix"])

# Mostrar solución al final
if cp == len(steps)-1:
    st.success(r"Solución final: \quad x=\frac{18}{13},\; y=-\frac52,\; z=-\frac{41}{26}")

# Animación automática
if st.session_state.auto and st.session_state.step < len(steps)-1:
    import time
    time.sleep(1.5)  # Velocidad
    st.session_state.step += 1
    st.experimental_rerun()
