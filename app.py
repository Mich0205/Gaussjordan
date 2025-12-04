import streamlit as st
import time

st.set_page_config(page_title="Gauss-Jordan Animado", layout="wide")

# ================================
# MATRICES Y EXPLICACIONES
# ================================
steps = [
    (
        "Paso 1 — Matriz aumentada inicial",
        "Tomamos el sistema,escribimos su matriz aumentada.",
        r"""
        \left[
        \begin{array}{ccc|c}
        2 & 1 & -3 & 5 \\
        3 & -2 & 2 & 6 \\
        5 & -3 & -1 & 16
        \end{array}
        \right]
        """
    ),
    (
        "Paso 2 — F1 → (1/2)F1",
        "Normalizamos el primer pivote dividiendo la fila 1 entre 2.",
        r"""
        \left[
        \begin{array}{ccc|c}
        1 & 1/2 & -3/2 & 5/2 \\
        3 & -2 & 2 & 6 \\
        5 & -3 & -1 & 16
        \end{array}
        \right]
        """
    ),
    (
        "Paso 3 — Eliminamos abajo del pivote 1",
        r"Realizamos:\; F2 \rightarrow F2 - 3F1,\quad F3 \rightarrow F3 - 5F1",
        r"""
        \left[
        \begin{array}{ccc|c}
        1 & 1/2 & -3/2 & 5/2 \\
        0 & -7/2 & 13/2 & -3/2 \\
        0 & -11/2 & 13/2 & 7/2
        \end{array}
        \right]
        """
    ),
    (
        "Paso 4 — F2 → -(2/7)F2",
        "Normalizamos el pivote 2 dividiendo F2 entre -7/2.",
        r"""
        \left[
        \begin{array}{ccc|c}
        1 & 1/2 & -3/2 & 5/2 \\
        0 & 1 & -13/7 & 3/7 \\
        0 & -11/2 & 13/2 & 7/2
        \end{array}
        \right]
        """
    ),
    (
        "Paso 5 — F3 → F3 + (11/2)F2",
        "Eliminamos el elemento debajo del pivote 2.",
        r"""
        \left[
        \begin{array}{ccc|c}
        1 & 1/2 & -3/2 & 5/2 \\
        0 & 1 & -13/7 & 3/7 \\
        0 & 0 & -26/7 & 41/7
        \end{array}
        \right]
        """
    ),
    (
        "Paso 6 — F3 → -(7/26)F3",
        "Normalizamos el pivote 3.",
        r"""
        \left[
        \begin{array}{ccc|c}
        1 & 1/2 & -3/2 & 5/2 \\
        0 & 1 & -13/7 & 3/7 \\
        0 & 0 & 1 & -41/26
        \end{array}
        \right]
        """
    ),
    (
        "Paso 7 — Eliminación hacia arriba",
        r"Aplicamos:\; F2 \rightarrow F2 + \frac{13}{7}F3,\quad F1 \rightarrow F1 - \frac12 F2",
        r"""
        \left[
        \begin{array}{ccc|c}
        1 & 0 & 0 & 18/13 \\
        0 & 1 & 0 & -5/2 \\
        0 & 0 & 1 & -41/26
        \end{array}
        \right]
        """
    ),
]

# ================================
# ESTADO
# ================================
if "step" not in st.session_state:
    st.session_state.step = 0
if "playing" not in st.session_state:
    st.session_state.playing = False

st.title("📘 Método de Gauss–Jordan — Animación Paso a Paso")

# CONTENEDOR PARA ACTUALIZAR SIN RECARGAR
placeholder = st.empty()

# BOTONES
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅ Paso anterior"):
        st.session_state.playing = False
        if st.session_state.step > 0:
            st.session_state.step -= 1

with col2:
    if st.button("▶ Reproducir animación"):
        st.session_state.playing = True

with col3:
    if st.button("➡ Siguiente paso"):
        st.session_state.playing = False
        if st.session_state.step < len(steps) - 1:
            st.session_state.step += 1

# FUNCIÓN PARA MOSTRAR EL PASO
def display_step(i):
    title, explanation, matrix = steps[i]
    with placeholder.container():
        st.subheader(title)
        st.info(explanation)
        st.latex(matrix)

# MOSTRAR PASO ACTUAL
display_step(st.session_state.step)

# ANIMACIÓN (SIN RERUN)
if st.session_state.playing:
    for i in range(st.session_state.step, len(steps)):
        st.session_state.step = i
        display_step(i)
        time.sleep(1.8)
    st.session_state.playing = False

