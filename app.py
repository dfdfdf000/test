import streamlit as st
import control as cnt
import matplotlib.pyplot as plt
import numpy as np

st.title("202021076_우동연")

# 주어진 전달함수
num = 100
den = [1, 5, 6]

sys_open_loop = cnt.TransferFunction(num, den)

# 폐루프 전달함수 계산
sys_closed_loop = cnt.feedback(sys_open_loop)

st.write("폐루프 전달함수:", sys_closed_loop)

# unit step 응답곡선 계산
t, y = cnt.step_response(sys_closed_loop)

# 응답곡선 그리기
fig1, ax1 = plt.subplots()
ax1.plot(t, y)
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Amplitude")
ax1.set_title("Unit Step Response")
ax1.grid()

st.pyplot(fig1)

# 주파수 응답 (보드선도) 계산
mag, phase, omega = cnt.bode(sys_closed_loop, dB=True, Plot=False)

# 보드선도 그리기
fig2, (ax2, ax3) = plt.subplots(2, 1, figsize=(8, 12))
ax2.semilogx(omega, mag)
ax2.set(xlabel="Frequency (rad/s)", ylabel="Magnitude (dB)")
ax2.set_title("Bode Magnitude Plot")
ax2.grid(which="both")

ax3.semilogx(omega, phase)
ax3.set(xlabel="Frequency (rad/s)", ylabel="Phase (deg)")
ax3.set_title("Bode Phase Plot")
ax3.grid(which="both")

st.pyplot(fig2)
