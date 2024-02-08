import mysql.connector

class venta:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            user='root',
            password='13579',
            host='localhost',
            database='repuestos',
            raise_on_warnings=True
        )

        self.cursor = self.conexion.cursor()
    
    def __str__(self):
         datos = self.consulta_venta()
         aux = ""
         for row in datos:
            aux = aux + str(row) + "\n"
        
         self.conexion.close()
          
         return aux



    def consulta_venta(self):
          cursor = self.conexion.cursor()
          cursor.execute( "SELECT * FROM venta")
          resultados = cursor.fetchall()
          cursor.close()
          return resultados
    
    def insertar_venta(self, id, total_venta, total_precio_bs, comision,  fecha_venta):
        cursor = self.conexion.cursor()
        sql = '''INSERT INTO venta (id, total_venta, total_precio_bs, comision,  fecha_venta)
        VALUES('{}', '{}', '{}', '{}','{}')'''.format(id, total_venta, total_precio_bs, comision,  fecha_venta)
        cursor.execute(sql)
        n = cursor.rowcount
        self.conexion.commit()
        return  n
       
   
    def modificar_venta(self, id_venta, id, cantidad, fecha_venta, id_repuesto):
        cursor = self.conexion.cursor()
        sql = '''UPDATE empleado SET id=?, cantidad=?, fecha_venta=?, id_repuesto=? WHERE id=?'''
        cursor.execute(sql, (id, cantidad, fecha_venta, id_repuesto, id_venta))
        n = cursor.rowcount
        self.conexion.commit()
        return n
    
    def eliminar_venta(self, id):
        cursor = self.conexion.cursor()
        sql = 'DELETE FROM venta WHERE id_venta = %s'
        cursor.execute(sql, (id,))
        n = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return n
    
    def obtener_ultimo_registro_venta(self):
        cursor = self.conexion.cursor()
        sql = "SELECT MAX(id_venta) FROM venta"
        cursor.execute(sql)
        resultado = cursor.fetchone()
        cursor.close()
        return resultado[0]
    
    def fecha_venta(self, fecha_desde, fecha_hasta):
        cursor = self.conexion.cursor()
        sql = "SELECT total_venta, fecha_venta FROM venta WHERE fecha_venta BETWEEN %s AND %s;"
        cursor.execute(sql, (fecha_desde, fecha_hasta)) 
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    
    def id_venta(self, fecha_desde, fecha_hasta):
        cursor = self.conexion.cursor()
        sql = "SELECT total_venta, fecha_venta, id, comision FROM venta WHERE fecha_venta BETWEEN %s AND %s;"
        cursor.execute(sql, (fecha_desde, fecha_hasta)) 
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
            
    def total_v_id(self,fecha_desde,fecha_hasta):
        cursor=self.conexion.cursor()
        sql="SELECT id, SUM(total_venta),SUM(comision) AS total_ventas  FROM venta  WHERE fecha_venta BETWEEN %s AND %s GROUP BY id"
        cursor.execute(sql, (fecha_desde, fecha_hasta)) 
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    
    def total_v_fecha(self,fecha_desde,fecha_hasta):
        cursor=self.conexion.cursor()
        sql="SELECT fecha_venta, SUM(total_venta) AS total_ventas FROM venta WHERE fecha_venta BETWEEN %s AND %s GROUP BY fecha_venta"
        cursor.execute(sql, (fecha_desde, fecha_hasta)) 
        resultado = cursor.fetchall()
        cursor.close()
        return resultado



 

    
        






