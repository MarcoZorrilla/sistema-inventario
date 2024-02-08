import mysql.connector

class dolar:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            user='root',
            password='13579',
            host='localhost',
            database='repuestos',
            raise_on_warnings=True
        )

    def __str__(self):
         datos = self.consulta_dolar()
         aux = ""
         for row in datos:
            aux = aux + str(row) + "\n"
        
         self.conexion.close()
          
         return aux



    def consulta_dolar(self):
          cursor = self.conexion.cursor()
          cursor.execute( "SELECT * FROM precio_dolar")
          resultados = cursor.fetchall()
          cursor.close()
          return resultados
        
    def insertar_dolar(self, fecha,precio_bs):
        cursor = self.conexion.cursor()
        sql = '''INSERT INTO precio_dolar (fecha,precio_bs)
        VALUES('{}', '{}')'''.format(fecha,precio_bs)
        cursor.execute(sql)
        n = cursor.rowcount
        self.conexion.commit()
        return n

    def obtener_ultimo_registro(self):
        cursor = self.conexion.cursor()
        sql = "SELECT precio_bs FROM precio_dolar ORDER BY id DESC LIMIT 1"
        cursor.execute(sql)
        resultado = cursor.fetchone()
        cursor.close()
        return resultado




  
