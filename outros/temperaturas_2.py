import streamlit as st

C = 0
K = C + 273.15
F = C * 9/5 + 32
st.title('Conversor de temperaturas')

column = st.columns(2)

def update(i):
    global C_slider, K_slider, F_slider, K, F, C
    match i:
        case 0:
            C = C_slider.numerator
            K = C + 273.15
            F = C * 9/5 + 32
        case 1:
            K = K_slider.numerator
            C = K - 273.15
            F = (C * 1.8) + 32
        case 2:
            F = F_slider.numerator
            C = (F - 32)*5/9
            K = C + 273.15

with column[0]:
    C_label = st.write(f'{C}')
    K_label = st.write(f'{K}')
    F_label = st.write(f'{F}')

with column[1]:
    C_slider = st.slider(label='°C',value=int(C),min_value=-100,max_value=100, on_change=lambda i = 0: update(i=i))
    K_slider = st.slider(label=' K',value=int(K),min_value= 173,max_value=374, on_change=lambda i = 1: update(i=i))
    F_slider = st.slider(label='°F',value=int(F),min_value=-148,max_value=212, on_change=lambda i = 2: update(i=i))


# 21981762949

