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