import streamlit as st
import pandas as pd
import sqlite3
conn = sqlite3.connect('login.db')
c = conn.cursor()

# Create a table for storing user credentials if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT,phone TEXT)''')
conn.commit()


def login(username,password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    if c.fetchone():
        return True
    else:
        return False
username=st.text_input("UserName:")
password=st.text_input("Password:")



def view_data():
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    table=st.text_input("Enter a table name:")
    c.execute('SELECT * FROM '+table)
    data = c.fetchall()
    df = pd.DataFrame(data, columns=[desc[0] for desc in c.description])
    
    return df

bt=st.checkbox("submit")
if bt:
    if not(username and password):
        st.warning("Pls enter a username and password")


    else:
        if login(username,password):
            st.success("login success")
            st.write(view_data())
        else:
            st.warning("login failed")

