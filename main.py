from load_csv1 import load_csv
from mysql_connection1 import insert_data_to_mysql

csv_file = "client.csv"  
df = load_csv(csv_file)

insert_data_to_mysql(df)
