import mysql.connector

class vehiculos:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            user='root',
            password='13579',
            host='localhost',
            database='repuestos',
            raise_on_warnings=True
        )

    def __str__(self):
         datos = self.consulta_vehiculos()
         aux = ""
         for row in datos:
            aux = aux + str(row) + "\n"
        
         self.conexion.close()
          
         return aux
    
    
    def consulta_vehiculos(self):
          cursor = self.conexion.cursor()
          cursor.execute( "SELECT * FROM vehiculos")
          resultados = cursor.fetchall()
          cursor.close()
          return resultados
    
    def nombre_vehiculos(self):
         cursor = self.conexion.cursor()
         sql = "SELECT modelo FROM vehiculos"
         cursor.execute(sql)
         resultados = cursor.fetchall()
         cursor.close()
        
         ids = [resultado[0] for resultado in resultados]  # Obtener solo los IDs y almacenarlos en una lista
         
         return ids
    
    def insertar_veh(self,Modelo,tipo_vehiculo,fecha_ingreso):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO vehiculos (modelo,tipo_vehiculo,fecha_ingreso) VALUES (%s, %s, %s)"
        val = (Modelo,tipo_vehiculo,fecha_ingreso)
        cursor.execute(sql, val)
        n = cursor.rowcount
        self.conexion.commit()
        return n
    
    def eliminar_veh(self,id):
        cursor = self.conexion.cursor()
        sql= '''DELETE FROM vehiculos WHERE id_vehiculos = {}'''.format(id)
        cursor.execute(sql)
        n = cursor.rowcount
        self.conexion.commit() 
        return n
    