import sqlite3 as sql3
import pandas as pd

try:
    con = sql3.connect('movies_data.db')
    con.row_factory = lambda c, row: row[0]

    cursor  = con.cursor()
    print('SQLite3 Data Base Connected Successfully')

    
    # create table
    cursor.execute('CREATE TABLE Movies(name varchar(10) PRIMARY KEY NOT NULL, actor varchar(10) NOT NULL, actress varchar(10) NOT NULL, director varchar(10) NOT NULL, year_of_release int NOT NULL);') 
    
    table_data = [('Inception','Leonardo DiCaprio', 'Marion Cotillard', 'Christopher Nolan', 2010), ('Never Back Down', 'Sean Faris', 'Amber Heard', 'Jeff Wadlow', 2008),('Edge of Tomorrow', 'Tom Cruise', 'Emily Blunt', 'Doug Liman', 2014)]
    
    # insert table
    cursor.executemany('INSERT INTO Movies (name,actor,actress,director,year_of_release) VALUES (?,?,?,?,?);',table_data)

    print("Data Successfully inserted into the table\n")
    movies_data = {}
    
    movies_data['Movie_name'] = cursor.execute('SELECT name FROM Movies;').fetchall()
    movies_data['Actor'] = cursor.execute('SELECT actor FROM Movies;').fetchall()
    movies_data['Actress'] = cursor.execute('SELECT actress FROM Movies;').fetchall()
    movies_data['Director'] = cursor.execute('SELECT director FROM Movies;').fetchall()
    movies_data['Year_of_Release'] = cursor.execute('SELECT year_of_release FROM Movies;').fetchall()

    df = pd.DataFrame(movies_data)

    print("Table Data:\n")
    print(df,'\n')
    con.commit()
    cursor.close()
    con.close()
except sql3.Error as e:
    print("Error!",e)

finally:
    if con:
        con.close()
        print('SQLite Connection closed')