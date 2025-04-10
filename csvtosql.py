import pyodbc

try:
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=WKWZTBFSOTOJR00\MSSQLSERVER01;DATABASE=projects;Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Tb_Users')

    for row in cursor:
        print(row)

except pyodbc.Error as err:
    print("Error:", err)
