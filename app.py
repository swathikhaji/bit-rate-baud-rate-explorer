
import streamlit as st

st.set_page_config(
    page_title="Bit Rate and Baud Rate Explorer",
    page_icon="📡",
    layout="centered"
)

st.title("📡 Bit Rate and Baud Rate Explorer")
st.write("Computer Networks Mini Project")

st.divider()

st.header("Bit Rate Calculator")
st.write("Enter the values below to calculate the bit rate.")

baud_rate = st.number_input(
    "Baud Rate (symbols per second)",
    min_value=1,
    value=1000,
    step=100
)

bits_per_symbol = st.selectbox(
    "Bits per Symbol",
    options=[1, 2, 3]
)

if st.button("Calculate Bit Rate"):
    bit_rate = baud_rate * bits_per_symbol

    st.subheader("Calculation")
    st.latex(
        r"\text{Bit Rate} = \text{Baud Rate} \times \text{Bits per Symbol}"
    )

    st.write(
        f"{baud_rate} × {bits_per_symbol} = {bit_rate} bps"
    )

    st.success(f"Calculated Bit Rate: {bit_rate:,} bps")
    st.metric("Bit Rate in Kilobits per Second", f"{bit_rate / 1000:.2f} kbps")

st.caption("Formula: Bit Rate = Baud Rate × Bits per Symbol")
