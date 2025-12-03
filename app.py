import streamlit as st
from animacion import gauss_jordan_steps, gauss_jordan_animation

st.set_page_config(page_title="Animación Gauss-Jordan", layout="centered")

st.title("📘 Método de Gauss-Jordan paso a paso")
st.write("Este programa muestra la reducción por filas con animación.")

A = [[2, 1, -3, 5],
     [3, -2, 2, 6],
     [5, -3, -1, 16]]

st.subheader("Matriz aumentada inicial")
st.write(A)

if st.button("Ejecutar animación"):
    gif_bytes = gauss_jordan_animation()
    st.image(gif_bytes, caption="Animación del método", use_column_width=True)

st.subheader("Pasos detallados")
steps = gauss_jordan_steps()

for step in steps:
    st.markdown(step)
