from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd

menu = st.sidebar.selectbox('Menu', ['Home', 'Dataset', 'Graph', 'About'], )

if menu == 'Home':
    
    st.write('<h4 style="text-align: center; font-weight: bold;">Prediksi Angka Kemiskinan di Indonesia</h4>',
            unsafe_allow_html=True)
    st.image('id-04.png')
    st.write('<h5 style="text-align: center;">Nama Kelompok :</h5>',
             unsafe_allow_html=True)
    st.write('<h5 style="text-align: center;">1. Avilia Indyra Rizki S.</h5>',
        unsafe_allow_html=True)
    st.write(
        '<h5 style="text-align: center;">2. Fahrul Roziqin Akbar </h5>',
        unsafe_allow_html=True)
    st.write('<h5 style="text-align: center;">3. Harbina Putri Nafiah</h5>',
        unsafe_allow_html=True)
    st.write('<h5 style="text-align: center;">4. Kresnabayu Dwirifanto</h5>',
        unsafe_allow_html=True)
    st.write('')
elif menu == 'Dataset':
    st.header('Dataset')
    df = pd.read_csv('2021socio_economic_indonesia.csv')
    st.write(df)
    st.dataframe(df.describe())
    count_data = df['province'].value_counts()
    st.write("Jumlah Data Per Provinsi")
    st.table(count_data)
elif menu == 'Graph':
    st.write('<h4 style="text-align: center; font-weight: bold;">Prediksi Angka Kemiskinan Indonesia</h4>',
            unsafe_allow_html=True)
    data = pd.read_csv('2021socio_economic_indonesia.csv')  # Ganti 'dataset_motor.csv' dengan nama dataset Anda
    X = data[['reg_gdp', 'life_exp', 'avg_schooltime', 'exp_percap']]
    y = data['poorpeople_percentage']

    # Memisahkan data menjadi data latih (training) dan data uji (testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    # Membuat model Decision Tree Regressor
    model = DecisionTreeRegressor(random_state=42)
    model.fit(X_train, y_train)
    reg = st.number_input("Regional GDP : ", value=None, placeholder="Type a number...")
    lifexp = st.number_input("Life Expectancy : ", value=None, placeholder="Type a number...")
    avg = st.number_input("Average School Time : ", value=None, placeholder="Type a number...")
    expercap = st.number_input("Expenses per Capita : ", value=None, placeholder="Type a number...")

    if st.button('Prediksi'):
        new_data = pd.DataFrame(
            {'reg_gdp': [reg], 'life_exp': [lifexp], 'avg_schooltime': [avg], 'exp_percap': expercap})
        predicted_cc = model.predict(new_data)
        if predicted_cc[0] > 15.00 :
            hasil = "Kemiskinan Tinggi"
        elif 15 > predicted_cc[0] > 10:
            hasil = "Kemisikianan Menengah"
        else :
            hasil = "Kemiskinan Rendah"
        st.markdown(
            f'<p style="background-color:#4F7942;color:#FFFFFF;"> Regional GDP : {reg}<br>Life Expectancy : {lifexp}<br>School Time : {avg}<br>Expenses per Capita : {expercap}<br>----------------------------------------<br>{predicted_cc[0]} = {hasil}</p>',
            unsafe_allow_html=True)

    data = pd.read_csv('2021socio_economic_indonesia.csv')
    most_poor = data.sort_values(by='poorpeople_percentage', ascending=False).head(300)
    fig1, ax = plt.subplots(figsize=(15, 10))
    sns.scatterplot(data=most_poor, x='poorpeople_percentage',
                    y='reg_gdp', hue='province', ax=ax)
    st.write('<h4 style="text-align: center; font-weight: bold;">Persentase Kemiskinan per Provinsi</h4>',
            unsafe_allow_html=True)
    st.pyplot(fig1)
    gdp = data.sort_values(by='reg_gdp').head(300)
    # Membuat figure dan axes dengan ukuran yang ditentukan
    fig6, ax = plt.subplots(figsize=(12, 6))

    # Membuat barplot pada axes yang ditentukan
    sns.barplot(data=gdp, x='province', y='reg_gdp', ax=ax ,palette='coolwarm')

    # Menambahkan judul dan label pada axes
    st.write('<h4 style="text-align: center; font-weight: bold;">Regional GDP Semua Provinsi</h4>',
            unsafe_allow_html=True)
    ax.set_xlabel('Provinsi')
    ax.set_ylabel('Regional GDP')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig6)
    penghasilan_perkapita = data.sort_values(by='exp_percap').head(300)
    # Membuat figure dan axes dengan ukuran yang ditentukan
    fig66, ax = plt.subplots(figsize=(12, 6))

    # Membuat barplot pada axes yang ditentukan
    sns.barplot(data=penghasilan_perkapita, x='province', y='exp_percap', ax=ax ,palette='coolwarm')

    # Menambahkan judul dan label pada axes
    st.write('<h4 style="text-align: center; font-weight: bold;">Pendapatan Per Kapita di semua Provinsi</h4>',
            unsafe_allow_html=True)
    ax.set_xlabel('Provinsi')
    ax.set_ylabel('Pendapatan Per Kapita')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig66)
    sekolah = data.sort_values(by='avg_schooltime').head(300)
    # Membuat figure dan axes dengan ukuran yang ditentukan
    fig7, ax = plt.subplots(figsize=(12, 6))

    # Membuat barplot pada axes yang ditentukan
    sns.barplot(data=sekolah, x='province', y='avg_schooltime', ax=ax ,palette='coolwarm')

    # Menambahkan judul dan label pada axes
    st.write('<h4 style="text-align: center; font-weight: bold;">Rata Rata Jam Sekolah di semua Provinsi</h4>',
            unsafe_allow_html=True)
    ax.set_xlabel('Provinsi')
    ax.set_ylabel('Rata Rata Jam Sekolah')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig7)
    
elif menu == 'About':
    st.write('<h4 style="text-align: center; font-weight: bold;">About</h4>',
            unsafe_allow_html=True)
    with open("deskripsi.txt", "r") as f:
        data = f.read()
    st.write(data)
