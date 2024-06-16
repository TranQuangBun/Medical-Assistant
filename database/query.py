import mysql.connector
import pandas as pd

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port="3308",
            user="root",
            password="",
            db="bloodda"
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")
        return None
def verify_credentials(email, password):
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            query = "SELECT * FROM user WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            user = cursor.fetchone()
            connection.close()
            return user
    else:
        return None

def signup(name,email,phone,password):
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            query = "INSERT INTO user (name, email, phone, password) VALUES (%s, %s, %s, %s)"
            record = (name, email, phone, password)
            cursor.execute(query, record)
            new_user_id = cursor.lastrowid
            connection.commit()

            user = get_user_by_id(new_user_id)
            return user
    else:
        return False
def get_news():
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT title, content, image_url,link FROM news')
            news_data = cursor.fetchall()
            return news_data
    else:
        return None

def view_all_data():
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT pcr_date,pcr FROM `covid_blood` ORDER BY `ID` ASC')
            data = cursor.fetchall()
            df = pd.DataFrame(data, columns=['pcr_date', 'pcr'])
            df['pcr_date'] = pd.to_datetime(df['pcr_date'])
            return df
    else:
        return None
def insert_feedback(user_id,selected_progress, feedback, satisfaction_level):
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            sql_query = """INSERT INTO feedback (user_id,selected_progress, feedback, satisfaction_level)
                                            VALUES (%s,%s, %s, %s)"""
            record = (user_id,selected_progress, feedback, satisfaction_level)
            cursor.execute(sql_query, record)
            connection.commit()
            # progress = ["Covid19", "Thiếu máu"]
            # if satisfaction_level == 1:
            #     if selected_progress == "Covid19":
            #         #cập
            #     elif selected_progress == "Thiếu máu":
            print("Feedback inserted successfully")
def insert_covid19(user_id,LYM, NEUT, MONO, EOS, BASO,HGB,HCT,MCV,MCH,MCHC,RDW,PLT,MPV,diseased):
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            sql_query = """INSERT INTO covid_test_results (user_id,LYM, NEUT, MONO, EOS, BASO,HGB,HCT,MCV,MCH,MCHC,RDW,PLT,MPV,diseased)
                                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            record = (user_id,LYM, NEUT, MONO, EOS, BASO, HGB, HCT, MCV, MCH, MCHC, RDW, PLT, MPV,diseased)
            cursor.execute(sql_query, record)
            connection.commit()
            print("covid19 inserted successfully")
def insert_anemia(user_id,LYM, NEUT, MONO, EOS, BASO,HGB,HCT,MCV,MCH,MCHC,RDW,PLT,MPV,RBC,WBC,diseased):
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            sql_query = """INSERT INTO anemia_test_results (user_id,LYM, NEUT, MONO, EOS, BASO,HGB,HCT,MCV,MCH,MCHC,RDW,PLT,MPV,RBC,WBC,diseased)
                                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            record = (user_id, LYM, NEUT, MONO, EOS, BASO, HGB, HCT, MCV, MCH, MCHC, RDW, PLT, MPV, RBC, WBC, diseased)
            cursor.execute(sql_query, record)
            connection.commit()
            print("Anemia inserted successfully")
def insert_diabetes(user_id,HGB,MCHC,MCH,MCV,MPV,RBC,PLT,RDW,WBC,diseased):
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            sql_query = """INSERT INTO diabetes_test_results(user_id,HGB,MCHC,MCH,MCV,MPV,RBC,PLT,RDW,WBC,diseased)
                                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            record = (user_id,HGB,MCHC,MCH,MCV,MPV,RBC,PLT,RDW,WBC,diseased)
            cursor.execute(sql_query, record)
            connection.commit()
            print("Diabetes inserted successfully")
def get_user_by_id(id):
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            select_query = "SELECT * FROM user WHERE id = %s"
            cursor.execute(select_query, (id,))
            new_user = cursor.fetchone()
            return new_user
    else:
        return None