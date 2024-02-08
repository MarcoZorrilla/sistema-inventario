import mysql.connector

class compra:
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
         datos = self.consulta_compra()
         aux = ""
         for row in datos:
            aux = aux + str(row) + "\n"
        
         self.conexion.close()
         return aux



    def consulta_compra(self):
          cursor = self.conexion.cursor()
          cursor.execute( "SELECT * FROM compra_total")
          resultados = cursor.fetchall()
          cursor.close()
          return resultados
    
    def insertar_compra(self,total_compra, total_bs,fecha):
        cursor = self.conexion.cursor()
        sql = '''INSERT INTO  compra_total ( total_compra, total_bs,fecha)
        VALUES('{}', '{}', '{}')'''.format(total_compra, total_bs, fecha)
        cursor.execute(sql)
        n = cursor.rowcount
        self.conexion.commit()
        return  n
    
    def insertar_detalle_compra(self,id_repuesto,id_c_total,cantidad_compra,fecha_compra,precio_compra,total_compra_d,total_compra_detalle_bs,nombre_repuesto):
        cursor = self.conexion.cursor()
        sql = '''INSERT INTO  compra ( id_repuesto,id_c_total,cantidad_compra,fecha_compra,precio_compra,total_compra_d,total_compra_detalle_bs,nombre_repuesto)
        VALUES('{}', '{}', '{}','{}','{}','{}','{}','{}')'''.format(id_repuesto,id_c_total,cantidad_compra,fecha_compra,precio_compra,total_compra_d,total_compra_detalle_bs,nombre_repuesto)
        cursor.execute(sql)
        n = cursor.rowcount
        self.conexion.commit()
        return  n
    
    def obtener_ultimo_registro_compra(self):
        cursor = self.conexion.cursor()
        sql = "SELECT MAX(id_compra_total) FROM compra_total"
        cursor.execute(sql)
        resultado = cursor.fetchone()
        cursor.close()
        return resultado[0]
    
    def consulta_compra_detalle(self):
          cursor = self.conexion.cursor()
          cursor.execute( "SELECT * FROM compra")
          resultados = cursor.fetchall()
          cursor.close()
          return resultados 

    def fecha_compra(self, fecha_desde, fecha_hasta):
        cursor = self.conexion.cursor()
        sql = "SELECT total_compra, total_bs,fecha,id_compra_total FROM compra_total WHERE fecha BETWEEN %s AND %s;"
        cursor.execute(sql, (fecha_desde, fecha_hasta)) 
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    
    
    def total_c_fecha(self,fecha_desde,fecha_hasta):
        cursor=self.conexion.cursor()
        sql="SELECT fecha, SUM(total_compra) AS total_compras FROM compra_total WHERE fecha BETWEEN %s AND %s GROUP BY fecha"
        cursor.execute(sql, (fecha_desde, fecha_hasta)) 
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    
    def fecha_c_de(self, fecha_desde, fecha_hasta):
        cursor = self.conexion.cursor()
        sql="SELECT nombre_repuesto, cantidad_compra, precio_compra,total_compra_d,total_compra_detalle_bs FROM compra WHERE fecha_compra BETWEEN %s AND %s"
        cursor.execute(sql,(fecha_desde,fecha_hasta))
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    
    def total_cd(self,fecha_desde,fecha_hasta):
        cursor=self.conexion.cursor()
        sql="SELECT nombre_repuesto, SUM(cantidad_compra), SUM(total_compra_d),SUM(total_compra_detalle_bs),SUM(cantidad_compra)AS tota_compras FROM compra WHERE fecha_compra BETWEEN %s AND %s GROUP BY nombre_repuesto"
        cursor.execute(sql, (fecha_desde, fecha_hasta)) 
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    