import streamlit as st
import numpy as np
import time

st.set_page_config(page_title="Gauss–Jordan Animado", layout="wide")

# -------------------------
# MATRIZ DEL EJERCICIO
# -------------------------
A = np.array([
    [2, 1, -3, 5],
    [3, -2, 2, 6],
    [5, -3, -1, 16]
], dtype=float)

explicaciones = [
    "Paso 1 — Hacemos pivote 1 en la fila 1 dividiendo toda la fila entre 2.",
    "Paso 2 — Eliminamos la columna 1 debajo del pivote usando F2 → F2 - 3F1.",
    "Paso 3 — Eliminamos en F3 la columna 1 usando F3 → F3 - 5F1.",
    "Paso 4 — Normalizamos el pivote 2 dividiendo F2 entre su elemento pivote.",
    "Paso 5 — Eliminamos arriba y abajo del pivote 2.",
    "Paso 6 — Normalizamos la fila 3.",
    "Paso 7 — Eliminamos arriba del pivote 3. Obtenemos la matriz identidad."
]

# Simulación de matrices en cada paso
matrices = []

# Paso 1
M1 = A.copy().astype(float)
M1[0] = M1[0] / 2
matrices.append(M1.copy())

# Paso 2
M2 = M1.copy()
M2[1] = M2[1] - 3*M2[0]
matrices.append(M2.copy())

# Paso 3
M3 = M2.copy()
M3[2] = M3[2] - 5*M2[0]
matrices.append(M3.copy())

# Paso 4
M4 = M3.copy()
M4[1] = M4[1] / M4[1,1]
matrices.append(M4.copy())

# Paso 5
M5 = M4.copy()
M5[0] = M5[0] - M5[0,1]*M5[1]
M5[2] = M5[2] - M5[2,1]*M5[1]
matrices.append(M5.copy())

# Paso 6
M6 = M5.copy()
M6[2] = M6[2] / M6[2,2]
matrices.append(M6.copy())

# Paso 7
M7 = M6.copy()
M7[0] = M7[0] - M7[0,2]*M7[2]
M7[1] = M7[1] - M7[1,2]*M7[2]
matrices.append(M7.copy())

# -------------------------
# CONTROL DE ESTADO
# -------------------------

if "paso" not in st.session_state:
    st.session_state.paso = 0

def siguiente():
    if st.session_state.paso < len(matrices) - 1:
        st.session_state.paso += 1

def anterior():
    if st.session_state.paso > 0:
        st.session_state.paso -= 1

def animar():
    for i in range(len(matrices)):
        st.session_state.paso = i
        time.sleep(1)
        st.experimental_get_query_params()  # este SÍ funciona y NO causa errores

# -------------------------
# UI
# -------------------------
st.title("📘 Método de Gauss–Jordan – Animación Paso a Paso")
st.write("Ejercicio tomado del PDF que mostraste. Incluye explicación detallada y animación automática.")

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.button("⏪ Paso anterior", on_click=anterior)

with col2:
    st.button("▶ Reproducir animación", on_click=animar)

with col3:
    st.button("⏩ Siguiente paso", on_click=siguiente)

# -------------------------
# MOSTRAR RESULTADOS
# -------------------------

st.subheader(f"Paso {st.session_state.paso+1} de {len(matrices)}")
st.info(explicaciones[st.session_state.paso])

st.latex(r"" + np.array2string(matrices[st.session_state.paso], separator=' & ').replace('[','\\left[').replace(']','\\right]'))

# Solución final
if st.session_state.paso == len(matrices) - 1:
    st.success("Solución final del sistema: \n\n"
               r"$x = \frac{18}{13},\quad y = -\frac{5}{2},\quad z = -\frac{41}{26}$")
