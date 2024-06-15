import mysql.connector
import pandas as pd
#connection
conn = mysql.connector.connect(
    host="localhost",
    port="3308",
    user="root",
    password="",
    db="bloodda"
)

mycursor = conn.cursor()


#fetch
def verify_credentials(email, password):
    connection = conn
    if connection:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM user WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            user = cursor.fetchone()
            cursor.close()
            connection.close()
    return user
def get_news():
    mycursor.execute('SELECT title, content, image_url,link FROM news')
    news_data = mycursor.fetchall()
    return news_data
def insert_feedback(selected_progress, feedback, satisfaction_level):
    connection = conn
    if connection:
        cursor = connection.cursor()
        sql_query = """INSERT INTO feedback (selected_progress, feedback, satisfaction_level) 
                                VALUES (%s, %s, %s)"""
        record = (selected_progress, feedback, satisfaction_level)
        cursor.execute(sql_query, record)
        connection.commit()
        print("Feedback inserted successfully")
def insert_covid19(LYM, NEUT, MONO, EOS, BASO,HGB,HCT,MCV,MCH,MCHC,RDW,PLT,MPV,diseased):
    connection = conn
    if connection:
        cursor = connection.cursor()
        sql_query = """INSERT INTO covid_test_results (LYM, NEUT, MONO, EOS, BASO,HGB,HCT,MCV,MCH,MCHC,RDW,PLT,MPV)
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        record = (LYM, NEUT, MONO, EOS, BASO,HGB,HCT,MCV,MCH,MCHC,RDW,PLT,MPV)
        cursor.execute(sql_query, record)
        connection.commit()
        print("covid19 inserted successfully")
def insert_anemia(LYM, NEUT, MONO, EOS, BASO,HGB,HCT,MCV,MCH,MCHC,RDW,PLT,MPV,RBC,WBC,diseased):
    connection = conn
    if connection:
        cursor = connection.cursor()
        sql_query = """INSERT INTO anemia_test_results (LYM, NEUT, MONO, EOS, BASO,HGB,HCT,MCV,MCH,MCHC,RDW,PLT,MPV,RBC,WBC,diseased)
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        record = (LYM, NEUT, MONO, EOS, BASO,HGB,HCT,MCV,MCH,MCHC,RDW,PLT,MPV,RBC,WBC,diseased)
        cursor.execute(sql_query, record)
        connection.commit()
        print("Anemia inserted successfully")
def view_all_data():
    mycursor.execute('SELECT pcr_date,pcr FROM `covid_blood` ORDER BY `ID` ASC')
    data = mycursor.fetchall()
    df = pd.DataFrame(data, columns=['pcr_date', 'pcr'])
    df['pcr_date'] = pd.to_datetime(df['pcr_date'])
    return df

def get_user_id_from_db(user_id):
    cursor = conn.cursor(dictionary=True)

    # Use parameterized query to prevent SQL injection
    query = "SELECT id FROM user WHERE email = %s"
    cursor.execute(query, (user_id))

    result = cursor.fetchone()

    cursor.close()
    conn.close()
    if result:
        return result['id']
    return None