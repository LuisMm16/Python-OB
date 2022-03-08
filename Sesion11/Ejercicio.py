import sqlite3

def main():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Insertar datos
    #insertar_datos(conn,cursor)

    # Buscar alumnos
    datos = cursor.execute('SELECT * FROM Alumnos')

    for dato in datos:
        print(dato)

    cursor.close()
    conn.close()

def insertar_datos(conn, cursor):
    # Ingresar datos en la DB
    cursor.execute('INSERT INTO Alumnos (id,nombre,apellido) VALUES (1,"Luis","Martinez")')
    cursor.execute('INSERT INTO Alumnos (id,nombre,apellido) VALUES (2,"Raul","Peredo")')
    cursor.execute('INSERT INTO Alumnos (id,nombre,apellido) VALUES (3,"Marta","Neruda")')
    cursor.execute('INSERT INTO Alumnos (id,nombre,apellido) VALUES (4,"Aurelio","Playas")')
    cursor.execute('INSERT INTO Alumnos (id,nombre,apellido) VALUES (5,"Juan","Paredes")')
    cursor.execute('INSERT INTO Alumnos (id,nombre,apellido) VALUES (6,"Armando","Mendez")')
    cursor.execute('INSERT INTO Alumnos (id,nombre,apellido) VALUES (7,"Roberto","Alvarez")')
    cursor.execute('INSERT INTO Alumnos (id,nombre,apellido) VALUES (8,"Fred","Montes")')
    conn.commit()


if __name__ == '__main__':
    main()
