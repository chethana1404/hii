import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# --- Streamlit page config ---
st.set_page_config(page_title="Blinking Heart", page_icon="❤", layout="centered")
st.title("❤ Hii")

# --- Heart equation ---
t_vals = np.linspace(0, 2 * np.pi, 361)
x_vals = 16 * np.sin(t_vals) ** 3
y_vals = 13 * np.cos(t_vals) - 5 * np.cos(2 * t_vals) - 2 * np.cos(3 * t_vals) - np.cos(4 * t_vals)
scale = 15

placeholder = st.empty()

# Step 1: Draw heart line-by-line once
draw_points_x, draw_points_y = [], []
for i in range(len(x_vals)):
    draw_points_x.append(x_vals[i] * scale)
    draw_points_y.append(y_vals[i] * scale)

    fig, ax = plt.subplots()
    ax.plot(draw_points_x, draw_points_y, color='red', linewidth=3)
    ax.set_aspect('equal')
    ax.axis("off")
    placeholder.pyplot(fig)
    plt.close(fig)
    time.sleep(0.01)  # delay for line-by-line effect

# Step 2: Blink by fading in/out
frames = 10  # frames per fade
for _ in range(5):  # number of blinks
    # Fade out
    for alpha in np.linspace(1.0, 0.1, frames):
        fig, ax = plt.subplots()
        ax.plot(x_vals * scale, y_vals * scale, color=(1, 0, 0, alpha), linewidth=3)
        ax.set_aspect('equal')
        ax.axis("off")
        placeholder.pyplot(fig)
        plt.close(fig)
        time.sleep(0.05)

    # Fade in
    for alpha in np.linspace(0.1, 1.0, frames):
        fig, ax = plt.subplots()
        ax.plot(x_vals * scale, y_vals * scale, color=(1, 0, 0, alpha), linewidth=3)
        ax.set_aspect('equal')
        ax.axis("off")
        placeholder.pyplot(fig)
        plt.close(fig)
        time.sleep(0.05)

st.success("Animation Finished!")