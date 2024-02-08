import mysql.connector

class empleado:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            user='root',
            password='13579',
            host='localhost',
            database='repuestos',
            raise_on_warnings=True
        )

    def __str__(self):
         datos = self.consulta_empleados()
         aux = ""
         for row in datos:
            aux = aux + str(row) + "\n"
        
         self.conexion.close()
          
         return aux



    def consulta_empleados(self):
          cursor = self.conexion.cursor()
          cursor.execute( "SELECT * FROM empleado")
          resultados = cursor.fetchall()
          cursor.close()
          return resultados
        
    def insertar_empleado(self,nombre,apellido,feha_de_nacimiento,telefono,correo,cargo,fecha_de_contratacion):
           cursor = self.conexion.cursor()
           sql = '''INSERT INTO empleado (nombre,apellido,feha_de_nacimiento,telefono,correo,cargo,fecha_de_contratacion)
          VALUES('{}','{}','{}','{}','{}','{}','{}') '''.format(nombre,apellido,feha_de_nacimiento,telefono,correo,cargo,fecha_de_contratacion)
           cursor.execute(sql)
           n = cursor.rowcount 
           self.conexion.commit()
           
           return n

    def eliminar_empleado(self,id):
          cursor = self.conexion.cursor()
          sql= '''DELETE FROM empleado WHERE id = {}'''.format(id)
          cursor.execute(sql)
          n = cursor.rowcount
          self.conexion.commit() 
          return n

    def modificar_empleado(self,id,nombre,apellido,feha_de_nacimiento,telefono,correo,cargo,fecha_de_contratacion):
         cursor = self.conexion.cursor()
         sql= '''UPDATE empleado
         SET nombre='{}',apellido='{}',feha_de_nacimiento='{}',telefono='{}',correo='{}',cargo='{}',fecha_de_contratacion='{}'
         WHERE id={}'''.format(nombre,apellido,feha_de_nacimiento,telefono,correo,cargo,fecha_de_contratacion,id)
         cursor.execute(sql)
         n = cursor.rowcount
         self.conexion.commit() 
         return n
    
          
    def id_empelados(self):
         cursor = self.conexion.cursor()
         sql = "SELECT id FROM empleado"
         cursor.execute(sql)
         resultados = cursor.fetchall()
         cursor.close()
        
         ids = [resultado[0] for resultado in resultados]  # Obtener solo los IDs y almacenarlos en una lista
         
         return ids


    def nombre_empleado(self, id):
        cursor = self.conexion.cursor()
        sql = "SELECT nombre FROM empleado WHERE id = %s"
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        cursor.close()
        
        if result:
            return result[0]
        else:
            return None

    
    

    
     

    