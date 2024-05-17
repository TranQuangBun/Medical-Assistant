import streamlit as st
import mysql.connector

#connection

conn = mysql.connector.connect(
    host="localhost",
    port="3308",
    user="root",
    password="",
    db="bloodda"
)

c = conn.cursor()

#fetch
def count_id():
    c.execute('SELECT count(ID) FROM `covid_blood`')
    data=c.fetchall()
    return data
def view_all_data():
    c.execute('SELECT * FROM `covid_blood` ORDER BY `ID` ASC')
    data=c.fetchall()
    return data