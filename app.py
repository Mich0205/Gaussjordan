import streamlit as st
from time import sleep

st.set_page_config(page_title="Método de Gauss–Jordan", layout="centered")

st.title("📘 Método de Gauss–Jordan — Animación Paso a Paso")
st.write("Ejercicio tomado del PDF que mostraste. Incluye explicación detallada y animación automática.")

# Guardar paso
if "paso" not in st.session_state:
    st.session_state.paso = 0

# ============================
#  PASOS CORREGIDOS
# ============================

steps = [

    # Paso 1
    (
        "Paso 1 — Matriz aumentada inicial",
        """
        Tomamos el sistema del PDF y escribimos su matriz aumentada.
        """,
        """
        \[
        \left[
        \begin{array}{ccc|c}
        2 & 1 & -3 & 5 \\
        3 & -2 & 2 & 6 \\
        5 & -3 & -1 & 16
        \end{array}
        \right]
        \]
        """
    ),

    # Paso 2
    (
        "Paso 2 — Normalización del pivote 1",
        """
        Aplicamos:

        \[
        F_1 \rightarrow \tfrac12 F_1
        \]
        """,
        """
        \[
        \left[
        \begin{array}{ccc|c}
        1 & 1/2 & -3/2 & 5/2 \\
        3 & -2 & 2 & 6 \\
        5 & -3 & -1 & 16
        \end{array}
        \right]
        \]
        """
    ),

    # Paso 3
    (
        "Paso 3 — Eliminación abajo del pivote 1",
        """
        Aplicamos:

        \[
        F_2 \rightarrow F_2 - 3F_1, \qquad
        F_3 \rightarrow F_3 - 5F_1
        \]
        """,
        """
        \[
        \left[
        \begin{array}{ccc|c}
        1 & 1/2 & -3/2 & 5/2 \\
        0 & -7/2 & 13/2 & -3/2 \\
        0 & -11/2 & 13/2 & 7/2
        \end{array}
        \right]
        \]
        """
    ),

    # Paso 4
    (
        "Paso 4 — Normalización del pivote 2",
        """
        Aplicamos:

        \[
        F_2 \rightarrow -\frac{2}{7} F_2
        \]
        """,
        """
        \[
        \left[
        \begin{array}{ccc|c}
        1 & 1/2 & -3/2 & 5/2 \\
        0 & 1 & -13/7 & 3/7 \\
        0 & -11/2 & 13/2 & 7/2
        \end{array}
        \right]
        \]
        """
    ),

    # Paso 5
    (
        "Paso 5 — Eliminación abajo del pivote 2",
        """
        Aplicamos:

        \[
        F_3 \rightarrow F_3 + \frac{11}{2} F_2
        \]
        """,
        """
        \[
        \left[
        \begin{array}{ccc|c}
        1 & 1/2 & -3/2 & 5/2 \\
        0 & 1 & -13/7 & 3/7 \\
        0 & 0 & -26/7 & 41/7
        \end{array}
        \right]
        \]
        """
    ),

    # Paso 6
    (
        "Paso 6 — Normalización del pivote 3",
        """
        Aplicamos:

        \[
        F_3 \rightarrow -\frac{7}{26} F_3
        \]
        """,
        """
        \[
        \left[
        \begin{array}{ccc|c}
        1 & 1/2 & -3/2 & 5/2 \\
        0 & 1 & -13/7 & 3/7 \\
        0 & 0 & 1 & -41/26
        \end{array}
        \right]
        \]
        """
    ),

    # Paso 7
    (
        "Paso 7 — Eliminación hacia arriba",
        """
        Aplicamos:

        \[
        F_2 \rightarrow F_2 + \frac{13}{7} F_3,
        \qquad
        F_1 \rightarrow F_1 - \frac12 F_2
        \]
        """,
        """
        \[
        \left[
        \begin{array}{ccc|c}
        1 & 0 & 0 & 18/13 \\
        0 & 1 & 0 & -5/2 \\
        0 & 0 & 1 & -41/26
        \end{array}
        \right]
        \]
        """
    ),
]

total = len(steps)

# =============================
#  MOSTRAR EL PASO
# =============================

titulo, explicacion, matriz = steps[st.session_state.paso]

st.subheader(titulo)
st.info(explicacion)
st.markdown(matriz)

# =============================
#  BOTONES
# =============================

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅ Paso anterior"):
        if st.session_state.paso > 0:
            st.session_state.paso -= 1

with col3:
    if st.button("➡ Siguiente paso"):
        if st.session_state.paso < total - 1:
            st.session_state.paso += 1

with col2:
    if st.button("▶ Reproducir animación"):
        for i in range(total):
            st.session_state.paso = i
            sleep(1.2)
            st.experimental_update()
