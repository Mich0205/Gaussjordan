import streamlit as st

st.set_page_config(page_title="Método de Gauss–Jordan", layout="wide")

st.title("📘 Método de Gauss–Jordan – Animación Paso a Paso")
st.write("Ejercicio tomado del PDF que mostraste.")

# -----------------------
# MATRICES EN LATEX
# -----------------------

matrices = [
r"""
\left[
\begin{array}{ccc|c}
2 & 1 & -3 & 5 \\
3 & -2 & 2 & 6 \\
5 & -3 & -1 & 16
\end{array}
\right]
""",

r"""
F_1 \rightarrow \frac{1}{2} F_1
\qquad
\left[
\begin{array}{ccc|c}
1 & 1/2 & -3/2 & 5/2 \\
3 & -2 & 2 & 6 \\
5 & -3 & -1 & 16
\end{array}
\right]
""",

r"""
F_2 \rightarrow F_2 - 3F_1
\qquad
F_3 \rightarrow F_3 - 5F_1
\qquad
\left[
\begin{array}{ccc|c}
1 & 1/2 & -3/2 & 5/2 \\
0 & -7/2 & 13/2 & -3/2 \\
0 & -11/2 & 13/2 & 7/2
\end{array}
\right]
""",

r"""
F_2 \rightarrow -\frac{2}{7} F_2
\qquad
F_3 \rightarrow F_3 + \frac{11}{2}F_2
\qquad
\left[
\begin{array}{ccc|c}
1 & 1/2 & -3/2 & 5/2 \\
0 & 1 & -13/7 & 3/7 \\
0 & 0 & -26/7 & 41/7
\end{array}
\right]
""",

r"""
F_3 \rightarrow -\frac{7}{26}F_3
\qquad
\left[
\begin{array}{ccc|c}
1 & 1/2 & -3/2 & 5/2 \\
0 & 1 & -13/7 & 3/7 \\
0 & 0 & 1 & -41/26
\end{array}
\right]
""",

r"""
F_2 \rightarrow F_2 + \frac{13}{7}F_3
\qquad
F_1 \rightarrow F_1 + \frac{3}{2}F_3
\qquad
\left[
\begin{array}{ccc|c}
1 & 1/2 & 0 & 7/52 \\
0 & 1 & 0 & -5/2 \\
0 & 0 & 1 & -41/26
\end{array}
\right]
""",

r"""
F_1 \rightarrow F_1 - \frac{1}{2}F_2
\qquad
\left[
\begin{array}{ccc|c}
1 & 0 & 0 & 18/13 \\
0 & 1 & 0 & -5/2 \\
0 & 0 & 1 & -41/26
\end{array}
\right]
"""
]

# Slider
paso = st.slider("Paso", 1, len(matrices), 1)

st.latex(matrices[paso - 1])
