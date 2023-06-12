import streamlit as st
import numpy as np
import pandas as pd

st.title('SIMPLE VECTOR MATRIX APPS')
st.text('Pastikan menekan "submit size" sebelum mendapatkan hasil operasi!')

with st.sidebar:
    tipe = st.radio('Pilih Tipe', ['Single Vector', 'Double Vector', 'Single Matrix', 'Double Matrix', 'Triple Matrix'])

with st.expander('Pilih Ukuran'):
    with st.form('Pilih Ukuran'):
        if tipe == 'Single Vector':
            size = st.number_input('Ukuran Vektor', min_value=2)
        elif tipe == "Double Matrix":
            row1 = st.number_input('Ukuran baris matrix pertama', min_value=2)
            col1 = st.number_input('Ukuran kolom matrix pertama', min_value=2)
            row2 = st.number_input('Ukuran baris matrix kedua', min_value=2)
            col2 = st.number_input('Ukuran kolom matrix kedua', min_value=2)
        elif tipe == "Single Matrix":
            row1 = st.number_input('Ukuran baris matrix', min_value=2)
            col1 = st.number_input('Ukuran kolom matrix', min_value=2)
        elif tipe == 'Double Vector':
            size1 = st.number_input('Ukuran Vektor pertama', min_value=2)
            size2 = st.number_input('Ukuran Vektor kedua', min_value=2)
        elif tipe == 'Triple Matrix':
            row1 = st.number_input('Ukuran baris matrix pertama', min_value=2)
            col1 = st.number_input('Ukuran kolom matrix pertama', min_value=2)
            row2 = st.number_input('Ukuran baris matrix kedua', min_value=2)
            col2 = st.number_input('Ukuran kolom matrix kedua', min_value=2)
            row3 = st.number_input('Ukuran baris matrix ketiga', min_value=2)
            col3 = st.number_input('Ukuran kolom matrix ketiga', min_value=2)
        submit = st.form_submit_button('Submit Size')

if tipe == 'Single Vector':
    df = pd.DataFrame(columns=range(1, size + 1), index=range(1, 2), dtype=float)

    st.write('Masukkan data untuk vektor')
    df_input = st.experimental_data_editor(df, use_container_width=True)

    if submit:
        vector = df_input.iloc[0].to_numpy()
        st.write("Vektor:", vector)

elif tipe == 'Double Vector':
    df1 = pd.DataFrame(columns=range(1, size1 + 1), index=range(1, 2), dtype=float)
    st.write('Masukkan data untuk vektor pertama')
    df1_input = st.experimental_data_editor(df1, use_container_width=True, key=1)

    df2 = pd.DataFrame(columns=range(1, size2 + 1), index=range(1, 2), dtype=float)
    st.write('Masukkan data untuk vektor kedua')
    df2_input = st.experimental_data_editor(df2, use_container_width=True, key=2)

    operasi = st.radio('Pilih Operasi', ['Dot Product', 'Cross Product'])

    if submit:
        vector1 = df1_input.iloc[0].to_numpy()
        vector2 = df2_input.iloc[0].to_numpy()

        if operasi == 'Dot Product':
            hasil = np.dot(vector1, vector2)
            st.write(hasil)
        elif operasi == 'Cross Product':
            hasil = np.cross(vector1, vector2)
            st.write(hasil)

elif tipe == 'Single Matrix':
    df = pd.DataFrame(columns=range(1, col1 + 1), index=range(1, row1 + 1), dtype=float)

    st.write('Masukkan data untuk matriks')
    df_input = st.experimental_data_editor(df, use_container_width=True)

    operasi = st.radio('Pilih Operasi', ['Transpose', 'Determinan'])

    if submit:
        matrix = df_input.to_numpy()

        if operasi == 'Transpose':
            hasil = np.transpose(matrix)
            st.write(hasil)
        elif operasi == 'Determinan':
            hasil = np.linalg.det(matrix)
            st.write("Hasil Determinan:", hasil)

elif tipe == 'Double Matrix':
    df1 = pd.DataFrame(columns=range(1, col1 + 1), index=range(1, row1 + 1), dtype=float)
    st.write('Masukkan data untuk matriks pertama')
    df1_input = st.experimental_data_editor(df1, use_container_width=True, key=1)

    df2 = pd.DataFrame(columns=range(1, col2 + 1), index=range(1, row2 + 1), dtype=float)
    st.write('Masukkan data untuk matriks kedua')
    df2_input = st.experimental_data_editor(df2, use_container_width=True, key=2)

    operasi = st.radio('Pilih Operasi', ['A * B', 'A + B', 'A - B'])

    if submit:
        matrix1 = df1_input.to_numpy()
        matrix2 = df2_input.to_numpy()

        if operasi == 'A * B':
            hasil = np.matmul(matrix1, matrix2)
            st.write(hasil)
        elif operasi == 'A + B':
            hasil = matrix1 + matrix2
            st.write(hasil)
        elif operasi == 'A - B':
            hasil = matrix1 - matrix2
            st.write(hasil)

elif tipe == 'Triple Matrix':
    df1 = pd.DataFrame(columns=range(1, col1 + 1), index=range(1, row1 + 1), dtype=float)
    st.write('Masukkan data untuk matriks pertama')
    df1_input = st.experimental_data_editor(df1, use_container_width=True, key=1)

    df2 = pd.DataFrame(columns=range(1, col2 + 1), index=range(1, row2 + 1), dtype=float)
    st.write('Masukkan data untuk matriks kedua')
    df2_input = st.experimental_data_editor(df2, use_container_width=True, key=2)

    df3 = pd.DataFrame(columns=range(1, col3 + 1), index=range(1, row3 + 1), dtype=float)
    st.write('Masukkan data untuk matriks ketiga')
    df3_input = st.experimental_data_editor(df3, use_container_width=True, key=3)

    operasi = st.radio('Pilih Operasi', ['A * B * C', 'A + B + C', 'A - B - C'])

    if submit:
        matrix1 = df1_input.to_numpy()
        matrix2 = df2_input.to_numpy()
        matrix3 = df3_input.to_numpy()

        if operasi == 'A * B * C':
            hasil = np.matmul(np.matmul(matrix1, matrix2), matrix3)
            st.write(hasil)
        elif operasi == 'A + B + C':
            hasil = matrix1 + matrix2 + matrix3
            st.write(hasil)
        elif operasi == 'A - B - C':
            hasil = matrix1 - matrix2 - matrix3
            st.write(hasil)
