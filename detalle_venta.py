import mysql.connector

class detalle_venta:
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


    def consulta_detalle_venta(self):
          cursor = self.conexion.cursor()
          cursor.execute( "SELECT * FROM detalle_venta")
          resultados = cursor.fetchall()
          cursor.close()
          return resultados
    
    def insertar_detalle_venta(self, id_venta, total_detalle_venta,  comision_detalle, total_bolivares_detalle , id_repuesto, cantidad_detalle,fecha_detalle):
        cursor = self.conexion.cursor()
        sql = '''INSERT INTO detalle_venta (id_venta, total_detalle_venta,  comision_detalle, total_bolivares_detalle , id_repuesto, cantidad_detalle,fecha_detalle)
        VALUES('{}', '{}', '{}', '{}','{}','{}','{}')'''.format(id_venta, total_detalle_venta,  comision_detalle, total_bolivares_detalle , id_repuesto, cantidad_detalle,fecha_detalle)
        cursor.execute(sql)
        n = cursor.rowcount 
        self.conexion.commit()
        return  n
       
   
    def modificar_detalle_venta(self,id_venta, total_detalle_venta,  comision_detalle, total_bolivares_detalle , id_repuesto, cantidad_detalle):
        cursor = self.conexion.cursor()
        sql = '''UPDATE empleado SET id_venta=?, total_detalle_venta=?, comision_detalle=?, total_bolivares_detalle=? , id_repuesto=?, cantidad_detalle=? WHERE id=?'''
        cursor.execute(sql, (id, id_venta, total_detalle_venta,  comision_detalle, total_bolivares_detalle , id_repuesto, cantidad_detalle))
        n = cursor.rowcount
        self.conexion.commit()
        return n
    


    def fecha_venta_de(self, fecha_desde, fecha_hasta):
        cursor = self.conexion.cursor()
        sql = "SELECT total_detalle_venta, total_bolivares_detalle,id_repuesto FROM detalle_venta WHERE fecha_detalle BETWEEN %s AND %s;"
        cursor.execute(sql, (fecha_desde, fecha_hasta)) 
        resultado = cursor.fetchall()
        cursor.close()
        return resultado

    def total_v_id_detale(self,fecha_desde,fecha_hasta):
        cursor=self.conexion.cursor()
        sql="SELECT id_repuesto, SUM(total_detalle_venta),SUM(cantidad_detalle),SUM(total_bolivares_detalle) AS total_ventas  FROM detalle_venta  WHERE fecha_detalle BETWEEN %s AND %s GROUP BY id_repuesto"
        cursor.execute(sql, (fecha_desde, fecha_hasta)) 
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    

    