import numpy as np
import imageio
from PIL import Image, ImageDraw, ImageFont
import io

def draw_matrix(matrix):
    img = Image.new("RGB", (420, 220), "white")
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    x0, y0, step = 20, 20, 30
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            d.text((x0 + j*60, y0 + i*step), f"{val:.2f}", fill="black", font=font)
    return img

def gauss_jordan_steps():
    A = np.array([[2., 1., -3., 5.],
                  [3., -2., 2., 6.],
                  [5., -3., -1., 16.]])

    steps = []
    M = A.astype(float)

    steps.append("### 🔹 Matriz inicial\n" + str(M))

    M[0] = M[0] / 2
    steps.append("### Paso 1: F1 → (1/2)F1\n" + str(M))

    M[1] = M[1] - 3*M[0]
    steps.append("### Paso 2: F2 → F2 - 3F1\n" + str(M))

    M[2] = M[2] - 5*M[0]
    steps.append("### Paso 3: F3 → F3 - 5F1\n" + str(M))

    M[1] = (-2/7)*M[1]
    steps.append("### Paso 4: F2 → (-2/7)F2\n" + str(M))

    M[2] = M[2] + (11/2)*M[1]
    steps.append("### Paso 5: F3 → F3 + (11/2)F2\n" + str(M))

    M[2] = (-7/26)*M[2]
    steps.append("### Paso 6: F3 → (-7/26)F3\n" + str(M))

    M[1] = M[1] + (13/7)*M[2]
    steps.append("### Paso 7: F2 → F2 + (13/7)F3\n" + str(M))

    M[0] = M[0] + (3/2)*M[2]
    steps.append("### Paso 8: F1 → F1 + (3/2)F3\n" + str(M))

    M[0] = M[0] - (1/2)*M[1]
    steps.append("### Paso 9: F1 → F1 - (1/2)F2\n" + str(M))

    return steps

def gauss_jordan_animation():
    A = np.array([[2., 1., -3., 5.],
                  [3., -2., 2., 6.],
                  [5., -3., -1., 16.]])

    M = A.astype(float)

    frames = []
    frames.append(draw_matrix(M))

    M[0] = M[0] / 2
    frames.append(draw_matrix(M))

    M[1] = M[1] - 3*M[0]
    frames.append(draw_matrix(M))

    M[2] = M[2] - 5*M[0]
    frames.append(draw_matrix(M))

    M[1] = (-2/7)*M[1]
    frames.append(draw_matrix(M))

    M[2] = M[2] + (11/2)*M[1]
    frames.append(draw_matrix(M))

    M[2] = (-7/26)*M[2]
    frames.append(draw_matrix(M))

    M[1] = M[1] + (13/7)*M[2]
    frames.append(draw_matrix(M))

    M[0] = M[0] + (3/2)*M[2]
    frames.append(draw_matrix(M))

    M[0] = M[0] - (1/2)*M[1]
    frames.append(draw_matrix(M))

    buffer = io.BytesIO()
    imageio.mimsave(buffer, frames, format="GIF", fps=1)
    buffer.seek(0)
    return buffer
