import streamlit as st
import pandas as pd

data = pd.read_csv('data.csv')
data.dropna()
data.drop_duplicates()
st.dataframe(data)
st.write('Thong ke du lieu')
dd = data.describe()
dd.index = ['Số dòng', 'Gia tri trung binh', 'Do lech chuan', 'Gia tri nho nhat', 'Gia tri trung vi 25%', 'Gia tri trung vi 50%', 'Gia tri trung vi 75%', 'Giá trị lớn nhất']
st.dataframe(dd)
dsnha = data[data['Giá bán/m2']>100]
st.dataframe(dsnha)
gtln = data['Giá bán/m2'].max()
dsnha = data[data['Giá bán/m2']==gtln]
tenhuyen = dsnha['Quận/Huyện'].unique()[0]
st.write(f'Quận {tenhuyen} có giá nhà cao nhất là: {round(gtln,2)} triệu vnd/m2')
gtnn = data['Giá bán/m2'].min()
ds1 = data[data['Giá bán/m2']==gtnn]
tenhuyen1 = ds1['Quận/Huyện'].unique()[0]
st.write(f'Quận {tenhuyen1} có giá nhà thấp nhất là: {round(gtnn,2)} triệu vnd/m2')
st.write('Đặc điểm loại hình nhà ở có giá cao nhất là: ', dsnha['Loại hình nhà ở'].unique()[0])
st.write('Đặc điểm loại hình nhà ở có giá thấp nhất là: ', ds1['Loại hình nhà ở'].unique()[0])
dstongln = data['Giá bán (tổng)'].max()
dstongnn = data['Giá bán (tổng)'].min()
st.write('Thông tin ngôi nhà có giá trị đắt nhất là: ', data[data['Giá bán (tổng)']==dstongln])
st.write('Thông tin ngôi nhà có giá trị thấp nhất là: ', data[data['Giá bán (tổng)']==dstongnn])
