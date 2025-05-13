import mysql.connector

def connect_to_mysql():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",         
        password="Test1234",  
        database="etl_project"  
    )
    return conn

def insert_data_to_mysql(df):
    conn = connect_to_mysql()
    cursor = conn.cursor()

    for index, row in df.iterrows():
        sql = """
        INSERT INTO client (id, nom, prenom, age)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE 
            nom = VALUES(nom),
            prenom = VALUES(prenom),
            age = VALUES(age)
        """
        cursor.execute(sql, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()

    print("Données insérées avec succès !")
