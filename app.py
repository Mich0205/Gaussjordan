import streamlit as st
from time import sleep

st.set_page_config(page_title="Gauss–Jordan Animado", layout="centered")

st.title("📘 Método de Gauss–Jordan — Animación Completa")

st.write("Incluye animación, pasos detallados y explicación clara del procedimiento del PDF.")

# Cargar GIF
st.image("gaussjordanim.gif", caption="Animación del método Gauss–Jordan", use_column_width=True)

st.divider()

# ==========================
# PASOS DETALLADOS
# ==========================

steps = [

("Paso 1 — Matriz inicial",
"""
Tomamos la matriz aumentada del sistema del PDF:
""",
r"""
\[
\left[
\begin{array}{ccc|c}
2 & 1 & -3 & 5 \\
3 & -2 & 2 & 6 \\
5 & -3 & -1 & 16
\end{array}
\right]
\]
"""),

("Paso 2 — Normalización del pivote 1",
"""
Aplicamos:

\[
F_1 \rightarrow \tfrac12 F_1
\]
""",
r"""
\[
\left[
\begin{array}{ccc|c}
1 & 1/2 & -3/2 & 5/2 \\
3 & -2 & 2 & 6 \\
5 & -3 & -1 & 16
\end{array}
\right]
\]
"""),

("Paso 3 — Eliminación debajo del pivote",
"""
Aplicamos:

\[
F_2 \rightarrow F_2 - 3F_1,
\qquad
F_3 \rightarrow F_3 - 5F_1
\]
""",
r"""
\[
\left[
\begin{array}{ccc|c}
1 & 1/2 & -3/2 & 5/2 \\
0 & -7/2 & 13/2 & -3/2 \\
0 & -11/2 & 13/2 & 7/2
\end{array}
\right]
\]
"""),

("Paso 4 — Normalización del pivote 2",
"""
Aplicamos:

\[
F_2 \rightarrow -\tfrac{2}{7}F_2
\]
""",
r"""
\[
\left[
\begin{array}{ccc|c}
1 & 1/2 & -3/2 & 5/2 \\
0 & 1 & -13/7 & 3/7 \\
0 & -11/2 & 13/2 & 7/2
\end{array}
\right]
\]
"""),

("Paso 5 — Eliminación debajo de F2",
"""
Aplicamos:

\[
F_3 \rightarrow F_3 + \tfrac{11}{2}F_2
\]
""",
r"""
\[
\left[
\begin{array}{ccc|c}
1 & 1/2 & -3/2 & 5/2 \\
0 & 1 & -13/7 & 3/7 \\
0 & 0 & -26/7 & 41/7
\end{array}
\right]
\]
"""),

("Paso 6 — Normalización del pivote 3",
"""
Aplicamos:

\[
F_3 \rightarrow -\tfrac{7}{26}F_3
\]
""",
r"""
\[
\left[
\begin{array}{ccc|c}
1 & 1/2 & -3/2 & 5/2 \\
0 & 1 & -13/7 & 3/7 \\
0 & 0 & 1 & -41/26
\end{array}
\right]
\]
"""),

("Paso 7 — Eliminación hacia arriba (forma reducida)",
"""
Aplicamos:

\[
F_2 \rightarrow F_2 + \tfrac{13}{7}F_3,
\qquad
F_1 \rightarrow F_1 - \tfrac12 F_2
\]
""",
r"""
\[
\left[
\begin{array}{ccc|c}
1 & 0 & 0 & 18/13 \\
0 & 1 & 0 & -5/2 \\
0 & 0 & 1 & -41/26
\end{array}
\right]
\]
"""),

]

# Mostrar pasos
if "step" not in st.session_state:
    st.session_state.step = 0

title, explanation, matrix = steps[st.session_state.step]

st.subheader(title)
st.info(explanation)
st.markdown(matrix)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅ Anterior"):
        if st.session_state.step > 0:
            st.session_state.step -= 1

with col3:
    if st.button("➡ Siguiente"):
        if st.session_state.step < len(steps)-1:
            st.session_state.step += 1

with col2:
    if st.button("▶ Reproducir animación paso a paso"):
        for i in range(len(steps)):
            st.session_state.step = i
            sleep(1.2)
            st.experimental_update()
