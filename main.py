import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Aplikasi Perhitungan EOQ (Economic Order Quantity)")

# Input
D = st.number_input("Permintaan Tahunan (unit/tahun)", min_value=1.0)
S = st.number_input("Biaya Pemesanan per Pesanan (Rp)", min_value=0.0)
H = st.number_input("Biaya Penyimpanan per Unit per Tahun (Rp)", min_value=0.0)

if D and S and H:
    # Hitung EOQ
    EOQ = np.sqrt((2 * D * S) / H)
    total_biaya_pemesanan = (D / EOQ) * S
    total_biaya_penyimpanan = (EOQ / 2) * H
    jumlah_pemesanan_pertahun = D / EOQ
    total_biaya_total = total_biaya_pemesanan + total_biaya_penyimpanan

    st.subheader("Hasil Perhitungan EOQ")
    st.write(f"EOQ (Jumlah Pemesanan Optimal): {EOQ:.2f} unit")
    st.write(f"Jumlah Pemesanan per Tahun: {jumlah_pemesanan_pertahun:.2f} kali")
    st.write(f"Total Biaya Pemesanan per Tahun: Rp {total_biaya_pemesanan:,.2f}")
    st.write(f"Total Biaya Penyimpanan per Tahun: Rp {total_biaya_penyimpanan:,.2f}")
    st.write(f"Total Biaya (Pemesanan + Penyimpanan) per Tahun: Rp {total_biaya_total:,.2f}")

    # Grafik
    Q = np.linspace(1, 2 * EOQ, 200)
    biaya_pemesanan = (D / Q) * S
    biaya_penyimpanan = (Q / 2) * H
    total_biaya = biaya_pemesanan + biaya_penyimpanan

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(Q, biaya_pemesanan, label='Biaya Pemesanan')
    ax.plot(Q, biaya_penyimpanan, label='Biaya Penyimpanan')
    ax.plot(Q, total_biaya, label='Total Biaya', linestyle='--')
    ax.axvline(x=EOQ, color='red', linestyle=':', label=f'EOQ = {EOQ:.2f}')
    ax.scatter(EOQ, total_biaya_total, color='black')

    ax.set_xlabel('Jumlah Pemesanan (Q)')
    ax.set_ylabel('Biaya (Rp)')
    ax.set_title('Grafik Biaya EOQ')
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
else:
    st.warning("Masukkan semua parameter untuk melihat hasil perhitungan.")
