import pyodbc

# Define your connection string
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=tcp:practicesqlserverdb.database.windows.net,1433;"
    "Database=practicesqlserverdb;"
    "Uid=sqladmin;"
    "Pwd=Mahefeb#2025;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)

try:
    conn = pyodbc.connect(conn_str)
    print("Connection successful!")
    conn.close()
except pyodbc.Error as e:
    print("Error:", e)
