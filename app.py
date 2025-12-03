import streamlit as st
from fractions import Fraction

st.set_page_config(page_title="Gauss-Jordan Animado", layout="centered")

st.title("📘 Método de Gauss–Jordan – Animación Paso a Paso")
st.write("Ejercicio tomado del PDF que mostraste.")

# ==== MATRIZ INICIAL ====
matrices = [
    ("**Matriz aumentada inicial:**", 
     r"""
\[
\left[
\begin{array}{ccc|c}
2 & 1 & -3 & 5\\
3 & -2 & 2 & 6\\
5 & -3 & -1 & 16
\end{array}
\right]
\]
"""),

    ("**1. Hacemos 1 el pivote de la fila 1:**  \n\(F_1 \rightarrow \frac{1}{2}F_1\)",
     r"""
\[
\left[
\begin{array}{ccc|c}
1 & \tfrac12 & -\tfrac32 & \tfrac52\\
3 & -2 & 2 & 6\\
5 & -3 & -1 & 16
\end{array}
\right]
\]
"""),

    ("**2. Hacemos ceros debajo del pivote 1:**  \n\(F_2 \rightarrow F_2 - 3F_1\)\n\(F_3 \rightarrow F_3 - 5F_1\)",
     r"""
\[
\left[
\begin{array}{ccc|c}
1 & \tfrac12 & -\tfrac32 & \tfrac52\\
0 & -7/2 & 13/2 & -3/2\\
0 & -11/2 & 13/2 & 7/2
\end{array}
\right]
\]
"""),

    ("**3. Convertimos pivote de fila 2 en 1:**  \n\(F_2 \rightarrow -\tfrac{2}{7} F_2\)",
     r"""
\[
\left[
\begin{array}{ccc|c}
1 & \tfrac12 & -\tfrac32 & \tfrac52\\
0 & 1 & -13/7 & 3/7\\
0 & -11/2 & 13/2 & 7/2
\end{array}
\right]
\]
"""),

    ("**4. Hacemos cero debajo del pivote de fila 2:**  \n\(F_3 \rightarrow F_3 + \tfrac{11}{2}F_2\)",
     r"""
\[
\left[
\begin{array}{ccc|c}
1 & \tfrac12 & -\tfrac32 & \tfrac52\\
0 & 1 & -13/7 & 3/7\\
0 & 0 & -26/7 & 41/7
\end{array}
\right]
\]
"""),

    ("**5. Convertimos pivote de fila 3 en 1:**  \n\(F_3 \rightarrow -\tfrac{7}{26} F_3\)",
     r"""
\[
\left[
\begin{array}{ccc|c}
1 & \tfrac12 & -\tfrac32 & \tfrac52\\
0 & 1 & -13/7 & 3/7\\
0 & 0 & 1 & -41/26
\end{array}
\right]
\]
"""),

    ("**6. Hacemos ceros arriba del pivote de fila 3:**  \n\(F_2 \rightarrow F_2 + \tfrac{13}{7} F_3\)",
     r"""
\[
\left[
\begin{array}{ccc|c}
1 & \tfrac12 & -\tfrac32 & \tfrac52\\
0 & 1 & 0 & -5/2\\
0 & 0 & 1 & -41/26
\end{array}
\right]
\]
"""),

    ("**7. Hacemos ceros arriba del pivote de fila 2:**  \n\(F_1 \rightarrow F_1 + \tfrac32 F_3\)\n\(F_1 \rightarrow F_1 - \tfrac12 F_2\)",
     r"""
\[
\left[
\begin{array}{ccc|c}
1 & 0 & 0 & 18/13\\
0 & 1 & 0 & -5/2\\
0 & 0 & 1 & -41/26
\end{array}
\right]
\]
"""),

    ("**SOLUCIÓN FINAL:**",
     r"""
\[
x = \frac{18}{13}, 
\qquad 
y = -\frac{5}{2}, 
\qquad 
z = -\frac{41}{26}
\]
""")
]

# ======= ANIMACIÓN =========
step = st.slider("Paso", 1, len(matrices), 1)

st.subheader(matrices[step-1][0])
st.markdown(matrices[step-1][1])
