import streamlit as st
import time

st.set_page_config(page_title="Método de Gauss–Jordan", layout="wide")

st.title("Método de Gauss–Jordan")


# -------------------------
# MATRICES + EXPLICACIONES
# -------------------------

steps = [
(
r"""
\left[
\begin{array}{ccc|c}
2 & 1 & -3 & 5 \\
3 & -2 & 2 & 6 \\
5 & -3 & -1 & 16
\end{array}
\right]
""",
"**Paso 1 — Matriz aumentada inicial.**\nTomamos el sistema original y formamos la matriz aumentada."
),

(
r"""
F_1 \rightarrow \frac{1}{2}F_1
\quad\Rightarrow\quad
\left[
\begin{array}{ccc|c}
1 & 1/2 & -3/2 & 5/2 \\
3 & -2 & 2 & 6 \\
5 & -3 & -1 & 16
\end{array}
\right]
""",
"**Paso 2 — Hacemos 1 el pivote de la primera fila.** Dividimos toda la fila 1 entre 2."
),

(
r"""
F_2 \rightarrow F_2 - 3F_1
\qquad
F_3 \rightarrow F_3 - 5F_1
\quad\Rightarrow\quad
\left[
\begin{array}{ccc|c}
1 & 1/2 & -3/2 & 5/2 \\
0 & -7/2 & 13/2 & -3/2 \\
0 & -11/2 & 13/2 & 7/2
\end{array}
\right]
""",
"**Paso 3 — Eliminamos los valores debajo del pivote 1.** Aplicamos F₂ = F₂ − 3F₁ y F₃ = F₃ − 5F₁."
),

(
r"""
F_2 \rightarrow -\frac{2}{7}F_2
\qquad
F_3 \rightarrow F_3 + \frac{11}{2}F_2
\quad\Rightarrow\quad
\left[
\begin{array}{ccc|c}
1 & 1/2 & -3/2 & 5/2 \\
0 & 1 & -13/7 & 3/7 \\
0 & 0 & -26/7 & 41/7
\end{array}
\right]
""",
"**Paso 4 — Normalizamos la segunda fila.** Multiplicamos F₂ por -2/7 para obtener un pivote igual a 1."
),

(
r"""
F_3 \rightarrow -\frac{7}{26}F_3
\quad\Rightarrow\quad
\left[
\begin{array}{ccc|c}
1 & 1/2 & -3/2 & 5/2 \\
0 & 1 & -13/7 & 3/7 \\
0 & 0 & 1 & -41/26
\end{array}
\right]
""",
"**Paso 5 — Normalizamos la tercera fila.** Multiplicamos F₃ para obtener un pivote 1."
),

(
r"""
F_2 \rightarrow F_2 + \frac{13}{7}F_3
\qquad
F_1 \rightarrow F_1 + \frac{3}{2}F_3
\quad\Rightarrow\quad
\left[
\begin{array}{ccc|c}
1 & 1/2 & 0 & 7/52 \\
0 & 1 & 0 & -5/2 \\
0 & 0 & 1 & -41/26
\end{array}
\right]
""",
"**Paso 6 — Eliminamos los valores arriba del pivote 3.**"
),

(
r"""
F_1 \rightarrow F_1 - \frac{1}{2}F_2
\quad\Rightarrow\quad
\left[
\begin{array}{ccc|c}
1 & 0 & 0 & 18/13 \\
0 & 1 & 0 & -5/2 \\
0 & 0 & 1 & -41/26
\end{array}
\right]
""",
"**Paso 7 — Eliminación final arriba del pivote 2.** Con esto llegamos a la matriz identidad."
),
]

# -------------------------
# CONTROL DE PASOS
# -------------------------

if "step" not in st.session_state:
    st.session_state.step = 0
if "auto" not in st.session_state:
    st.session_state.auto = False

# Botones
col1, col2, col3 = st.columns([1,1,1])

with col1:
    if st.button("⏮ Paso anterior"):
        st.session_state.auto = False
        st.session_state.step = max(0, st.session_state.step - 1)

with col2:
    if st.button("▶ Reproducir animación"):
        st.session_state.auto = True

with col3:
    if st.button("⏭ Siguiente paso"):
        st.session_state.auto = False
        st.session_state.step = min(len(steps)-1, st.session_state.step + 1)

# Animación automática SIN rerun
if st.session_state.auto:
    for i in range(st.session_state.step, len(steps)):
        st.session_state.step = i
        time.sleep(1.4)
        st.write("")  # fuerza refresco visual pequeño
        st.experimental_update()  # ESTE SÍ FUNCIONA EN STREAMLIT CLOUD

# Mostrar paso
matrix, explanation = steps[st.session_state.step]

st.subheader(f"Paso {st.session_state.step + 1} de {len(steps)}")
st.latex(matrix)
st.info(explanation)

# Solución final
if st.session_state.step == len(steps)-1:
    st.success(
        r"""
        **Solución final del sistema:**
        \[
        x = \frac{18}{13},\quad
        y = -\frac{5}{2},\quad
        z = -\frac{41}{26}
        \]
        """
    )
