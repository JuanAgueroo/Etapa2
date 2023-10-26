#!C:\Python311\python.exe


import sqlite3
import cgi


form = cgi.FieldStorage()
nombre = form.getvalue('nombr')
edad = form.getvalue('e_eda')
materia = form.getvalue('materias')
insertar = form.getvalue('guardar')

dir = 'C:\\xampp\\htdocs\\Etapa2\\cgi-bin\\'


def conectar():
    conn = sqlite3.connect(dir + "data_db.sqlite")
    return conn


def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS estudiante (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_apellido TEXT NOT NULL,
                        edad INTEGER NOT NULL,
                        materia TEXT NOT NULL)""")
    conn.commit()
    conn.close()


def insertar_dats(nombre_apellido, edad, materia):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO estudiante (nombre_apellido, edad, materia) VALUES (?, ?, ?)""",
                   (nombre_apellido, edad, materia))
    conn.commit()
    conn.close()


def obtener_datos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estudiante")
    alumnos = cursor.fetchall()
    conn.close()
    return alumnos


crear_tabla()

if insertar:
    if nombre and edad and materia:
        insertar_dats(nombre, edad, materia)


print("Content-type: text/html\n")

datos = obtener_datos()

tabla_html = '<table>'
tabla_html += '<tr><th>Estudiante</th><th>Edad</th><th>Materia</th></tr>'

for fila in datos:
    tabla_html += '<tr>'
    for dato in fila:
        tabla_html += f'<td>{dato}</td>'
    tabla_html += '</tr>'
tabla_html += '</table>'

print(tabla_html)
