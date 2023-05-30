import streamlit as st
import pandas as pd

# Membaca file CSV

st.set_page_config(
     page_title="Test2023 Web App",
     page_icon="tes",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://pawhike2023.web.app/#/',
         'Report a bug': "https://pawhike2023.web.app/#/",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
)

@st.cache
def read_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df


def calculate_total_sales(df):
    if 'jumlah' in df.columns:
        total_sales = df['jumlah'].sum()
        return total_sales
    else:
        return 0


def find_highest_sales_transaction(df):
    if 'jumlah' in df.columns:
        max_sales = df['jumlah'].max()
        transaction = df[df['jumlah'] == max_sales]
        return transaction
    else:
        return pd.DataFrame()


def count_transactions(df):
    total_transactions = len(df)
    return total_transactions


def find_sold_products(df):
    if 'produk' in df.columns:
        sold_products = df['produk'].unique()
        return sold_products
    else:
        return []

def main():
    st.title("Pengolahan Data CSV badeasaputro@gmail.com - scenario 3 // sesuaikan data format CSV!=")

    
    file = st.file_uploader("Upload file CSV", type=["csv"])
    if file is not None:
        df = read_csv_file(file)

        
        st.subheader("Data Transaksi")
        st.write(df)

        
        total_sales = calculate_total_sales(df)
        st.subheader("Total Penjualan")
        st.write(total_sales)

        
        highest_transaction = find_highest_sales_transaction(df)
        st.subheader("Transaksi dengan Penjualan Tertinggi")
        st.write(highest_transaction)

        
        total_transactions = count_transactions(df)
        st.subheader("Jumlah Transaksi")
        st.write(total_transactions)

       
        sold_products = find_sold_products(df)
        st.subheader("Daftar Produk yang Terjual")
        st.write(sold_products)

        
        option = st.radio("Pilih Jenis Data", ('Data Transaksi', 'Total Penjualan', 'Transaksi dengan Penjualan Tertinggi', 'Jumlah Transaksi', 'Daftar Produk yang Terjual'))

       
        if option == 'Data Transaksi':
            st.write(df)
        elif option == 'Total Penjualan':
            st.write(total_sales)
        elif option == 'Transaksi dengan Penjualan Tertinggi':
            st.write(highest_transaction)
        elif option == 'Jumlah Transaksi':
            st.write(total_transactions)
        elif option == 'Daftar Produk yang Terjual':
            st.write(sold_products)

if __name__ == '__main__':
    main()
