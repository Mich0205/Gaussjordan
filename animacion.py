import numpy as np
import matplotlib.pyplot as plt
import imageio
from PIL import Image
import os

# ==========================
# SISTEMA INICIAL DEL PDF
# ==========================

matrices = []

def add_frame(M, title, explanation, pivot=None, rows=None):
    """
    Genera una imagen (frame) de la matriz con:
    - pivot en rojo
    - filas modificadas en gris
    - explicación arriba
    - estilo matemático simple (tipo escolar)
    """

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.axis("off")

    # Texto del título
    plt.text(0.5, 1.05, title, ha="center", fontsize=16, color="black", transform=ax.transAxes)

    # Texto de explicación
    plt.text(0.5, 0.95, explanation, ha="center", fontsize=12, color="black", transform=ax.transAxes)

    # Convertir matriz a tabla
    table = ax.table(cellText=M, loc="center", cellLoc="center")

    # Estilos de todas las celdas
    for (i, j), cell in table.get_celld().items():
        cell.set_edgecolor("black")
        cell.set_linewidth(1.5)
        cell.set_fontsize(12)

        # Colorear pivote
        if pivot is not None and (i, j) == pivot:
            cell.set_facecolor("#ff5959")  # rojo suave

        # Colorear filas afectadas
        if rows is not None and i in rows:
            cell.set_facecolor("#d9d9d9")  # gris claro

    fig.tight_layout()

    # Guardar frame temporal
    plt.savefig("frame.png", dpi=120)
    plt.close()

    matrices.append(imageio.imread("frame.png"))


# ==========
# PASO 1
# ==========
M1 = [
    [2, 1, -3, 5],
    [3, -2, 2, 6],
    [5, -3, -1, 16]
]
add_frame(M1, "Paso 1 — Matriz inicial",
          "Escribimos la matriz aumentada del sistema.",
          pivot=None, rows=None)

# ==========
# PASO 2 — Normalización pivote 1
# ==========
M2 = [
    [1, 1/2, -3/2, 5/2],
    [3, -2, 2, 6],
    [5, -3, -1, 16]
]
add_frame(M2, "Paso 2 — Normalización de F1",
          r"Aplicamos:  F1 → ½ F1",
          pivot=(0, 0), rows=[0])

# ==========
# PASO 3 — Eliminación bajo pivote 1
# ==========
M3 = [
    [1, 1/2, -3/2, 5/2],
    [0, -7/2, 13/2, -3/2],
    [0, -11/2, 13/2, 7/2]
]
add_frame(M3, "Paso 3 — Eliminamos debajo del pivote",
          r"Aplicamos: F2 → F2 − 3F1,  F3 → F3 − 5F1",
          pivot=(0, 0), rows=[1, 2])

# ==========
# PASO 4 — Normalizar pivote 2
# ==========
M4 = [
    [1, 1/2, -3/2, 5/2],
    [0, 1, -13/7, 3/7],
    [0, -11/2, 13/2, 7/2]
]
add_frame(M4, "Paso 4 — Normalización de F2",
          r"Aplicamos: F2 → -(2/7) F2",
          pivot=(1, 1), rows=[1])

# ==========
# PASO 5 — Eliminación bajo pivote 2
# ==========
M5 = [
    [1, 1/2, -3/2, 5/2],
    [0, 1, -13/7, 3/7],
    [0, 0, -26/7, 41/7]
]
add_frame(M5, "Paso 5 — Eliminación bajo F2",
          r"Aplicamos: F3 → F3 + (11/2)F2",
          pivot=(1, 1), rows=[2])

# ==========
# PASO 6 — Normalizar pivote 3
# ==========
M6 = [
    [1, 1/2, -3/2, 5/2],
    [0, 1, -13/7, 3/7],
    [0, 0, 1, -41/26]
]
add_frame(M6, "Paso 6 — Normalización de F3",
          r"Aplicamos: F3 → -(7/26)F3",
          pivot=(2, 2), rows=[2])

# ==========
# PASO 7 — Eliminación hacia arriba
# ==========
M7 = [
    [1, 0, 0, 18/13],
    [0, 1, 0, -5/2],
    [0, 0, 1, -41/26]
]
add_frame(M7, "Paso 7 — Eliminación hacia arriba",
          r"Aplicamos: F2 → F2 + (13/7)F3,  F1 → F1 − ½ F2",
          pivot=(2, 2), rows=[0, 1])

# ======================
# GENERAR GIF FINAL
# ======================
imageio.mimsave("gaussjordanim.gif", matrices, duration=1.2)

print("GIF generado correctamente: gaussjordanim.gif")
