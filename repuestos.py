import mysql.connector

class repuesto:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            user='root',
            password='13579',
            host='localhost',
            database='repuestos',
            raise_on_warnings=True
        )

    def __str__(self):
         datos = self.consulta_repuestos()
         aux = ""
         for row in datos:
            aux = aux + str(row) + "\n"
        
         self.conexion.close()
          
         return aux



    def consulta_repuestos(self):
          cursor = self.conexion.cursor()
          cursor.execute( "SELECT * FROM repuesto")
          resultados = cursor.fetchall()
          cursor.close()
          return resultados
        
    def insertar_repuestos(self, nombre, referencia, precio, cantidad, Modelo):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO repuesto (nombre, referencia, precio, cantidad, Modelo) VALUES (%s, %s, %s, %s, %s)"
        val = (nombre, referencia, precio, cantidad, Modelo)
        cursor.execute(sql, val)
        n = cursor.rowcount
        self.conexion.commit()
        return n


    def eliminar_repuesto(self,id):
          cursor = self.conexion.cursor()
          sql= '''DELETE FROM repuesto WHERE id = {}'''.format(id)
          cursor.execute(sql)
          n = cursor.rowcount
          self.conexion.commit() 
          return n
         
    def id_repuesto(self):
         cursor = self.conexion.cursor()
         sql = "SELECT id_repuesto FROM repuesto"
         cursor.execute(sql)
         resultados = cursor.fetchall()
        
        
         ids = [resultado[0] for resultado in resultados]  # Obtener solo los IDs y almacenarlos en una lista
         
         return ids

    def precio_repuesto(self, id):
        cursor = self.conexion.cursor()
        sql = "SELECT precio FROM repuesto WHERE id_repuesto = %s"
        cursor.execute(sql, (id,))
        result = cursor.fetchone() 
        if result:
            return result[0]
        else:
            return None
    
    def nombre_repuesto(self, id):
        cursor = self.conexion.cursor()
        sql = "SELECT nombre FROM repuesto WHERE id_repuesto = %s"
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        
        if result:
            return result[0]
        else:
            return None


    def calcular_precio_bolivar(self, id_repuesto, precio):
        cursor = self.conexion.cursor()
        sql = "SELECT precio_bs FROM precio_dolar ORDER BY fecha DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        ultima_tasa_dolar = result[0]
        ultima_tasa_dolar = float(ultima_tasa_dolar)  # Convertir a tipo float
        # Calcular el precio en bolívares
        precio_bolivar = precio * ultima_tasa_dolar
        # Actualizar el precio en bolívares en la tabla de repuesto
        try:
            cursor.execute("UPDATE repuesto SET precio_bolivar = %s WHERE id_repuesto = %s", (precio_bolivar, id_repuesto))
            self.conexion.commit()  # Confirmar la actualización en la base de datos
            print("¡Actualización exitosa!")
        except Exception as e:
            print("Error al actualizar la tabla 'repuesto':", e)

    def obtener_ultimo_registro_repuesto(self):
        cursor = self.conexion.cursor()
        sql = "SELECT MAX(id_repuesto) FROM repuesto"
        cursor.execute(sql)
        resultado = cursor.fetchone()
        cursor.close()
        return resultado[0]

    def modificar_repuesto(self,id_repuesto,nombre,referencia,precio,cantidad):
        cursor = self.conexion.cursor()
        sql = '''UPDATE repuesto
                SET nombre=%s, referencia=%s, precio=%s, cantidad=%s
                WHERE id_repuesto=%s'''
        cursor.execute(sql, (nombre, referencia, precio, cantidad, id_repuesto))
        n = cursor.rowcount
        self.conexion.commit()
        return n
    
    def disminuir_cantidad(self,cantidad,id_repuesto):
        cursor = self.conexion.cursor() 
        sql = "UPDATE repuesto SET cantidad = (SELECT cantidad FROM repuesto WHERE id_repuesto = %s) - %s WHERE id_repuesto = %s"
        valores = (id_repuesto, cantidad, id_repuesto)
        cursor.execute(sql, valores)
        n=cursor.rowcount
        self.conexion.commit()
        return n
        
    def aumentra_cantidad(self,cantidad,id_repuesto):
        cursor=self.conexion.cursor()
        sql = "UPDATE repuesto SET cantidad = cantidad + %s WHERE id_repuesto = %s"
        cursor.execute(sql,(cantidad,id_repuesto))
        n=cursor.rowcount
        self.conexion.commit()
        return n

        
    def busqueda_repuesto(self,nombre):
        cursor=self.conexion.cursor()
        sql= "SELECT * FROM repuesto WHERE nombre LIKE %s"
        cursor.execute(sql, ('%' + nombre + '%',))
        productos = cursor.fetchall()
        return productos

    