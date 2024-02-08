from tkinter import *
from typing import Optional, Tuple, Union
from customtkinter import *
from PIL import Image, ImageTk
import os
from tkinter import ttk
from empleado import empleado
import mysql.connector
from tkinter import messagebox
from venta import venta
from repuestos import repuesto
from precio_dolar import dolar
from decimal import Decimal
import mysql.connector
from detalle_venta import detalle_venta
import pandas as pd
import matplotlib.pyplot as plt
from compra import compra 
from CTkTable import *
from vehiculo import vehiculos
import mysql.connector
class App(CTk): 
    def __init__(self):
        super().__init__()
        self.config_pan()
        self.create_widgets()
       

    empleados=empleado()
    ventas=venta()
    repuestos=repuesto()
    dolars=dolar()
    detalle_ventas=detalle_venta()
    compras=compra()
    vehiculos=vehiculos()

 #botones empleado
    def limpiar_inserta(self):
        self.textnombrea.delete(0,END)
        self.textapellidoa.delete(0,END)
        self.textfdna.delete(0,END)
        self.texttlfa.delete(0,END)
        self.textcorreoa.delete(0,END)
        self.textcargoa.delete(0,END)
        self.textfdca.delete(0,END)
    def limpiar_insert(self):
        self.textnombre.delete(0,END)
        self.textapellido.delete(0,END)
        self.textfdn.delete(0,END)
        self.texttlf.delete(0,END)
        self.textcorreo.delete(0,END)
        self.textcargo.delete(0,END)
        self.textfdc.delete(0,END)
    def guardar_empleado(self):
        self.empleados.insertar_empleado(self.textnombre.get(),self.textapellido.get(),self.textfdn.get(),self.texttlf.get(),self.textcorreo.get(),self.textcargo.get(),self.textfdc.get())
        self.factualizar()
        self.limpiar_insert()      
    def eliminar(self):
        self.empleados.eliminar_empleado(self.eliminar_empleados.get())
        self.eliminar_empleados.delete(0, 'end')
    def eliminar_empleado(self):
        self.eliminar_empleados = CTkEntry(self.Frame_cone3,placeholder_text="ingrese el id",width=70)
        self.eliminar_empleados.place(x=40,y=120)
        self.btn_confirmar_eliminacion = CTkButton(self.Frame_cone3,text="confirmar",command=self.eliminar,fg_color="#2a2d2e",text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,width=70)
        self.btn_confirmar_eliminacion.place(x=40,y=150)
    def factualizar(self):
            self.grid.delete(*self.grid.get_children())
            datos = self.empleados.consulta_empleados()
            for row in datos:
                self.grid.insert("",END,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))       
    def act_empleado(self):
        selected = self.grid.focus()
        self.clave = self.grid.item(selected, 'text')
        print(self.clave)
        if self.clave == '':
             messagebox.showwarning("modificar", 'debes seleccionar un elemento')
        else:
         valores = self.grid.item(selected, 'values')
         self.textnombrea.insert(0, valores[0])
         self.textapellidoa.insert(0, valores[1])
         self.textfdna.insert(0, valores[2])
         self.texttlfa.insert(0, valores[3])
         self.textcorreoa.insert(0, valores[4])
         self.textcargoa.insert(0, valores[5])
         self.textfdca.insert(0, valores[6])        
    def act_boton_guardar(self):
     self.empleados.modificar_empleado(self.clave, self.textnombrea.get(), self.textapellidoa.get(), self.textfdna.get(), self.texttlfa.get(), self.textcorreoa.get(), self.textcargoa.get(), self.textfdca.get())
     self.factualizar()
     self.limpiar_inserta()
    #botones venta
    def llenar_grid_venta(self):
        self.grid_venta.delete(*self.grid_venta.get_children())
        datov=self.ventas.consulta_venta()
        for row in datov:
            self.grid_venta.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
    def eliminar_venta(self):
        self.ventas.eliminar_venta(self.eliminar_ventax.get())
        self.eliminar_ventax.delete(0, 'end')
    def elimina_venta(self):
        self.eliminar_ventax = CTkEntry(self.frame_venta_consulta,placeholder_text="ingrese el id",width=155)
        self.eliminar_ventax.place(x=0,y=120)
        self.btn_confirmar_eliminacion_venta = CTkButton(self.frame_venta_consulta,text="confirmar",command=self.eliminar_venta,fg_color='#0F7CD1',text_color='black',border_color='#FFCC70',border_width=2,corner_radius=32)
        self.btn_confirmar_eliminacion_venta.place(x=0,y=150)
    def config_pan(self):
      self.title("sistema crud")
      self.geometry("1000x500")
    def agregar_venta(self):
        self.empleado = self.combo_emp.get()
        self.producto = self.combo_pro.get()
        self.texto1_ingresado=self.combo_cant.get()
        self.text2_ingresado=self.fecha_factura.get()
        #datos del grid
        p_comision=0.1
        precio_dolar = self.dolars.obtener_ultimo_registro()
        nombre_repuesto=self.repuestos.nombre_repuesto(self.producto)
        nombre_empleado=self.empleados.nombre_empleado(self.empleado)
        precio=self.repuestos.precio_repuesto(self.producto)
        self.cantidad=int(self.texto1_ingresado)
        self.total_precio=precio*self.cantidad
        self.total_bs=float(precio_dolar[0])*self.total_precio
        self.comision=self.total_precio*p_comision
        resultado = self.comision
        resultado_como_cadena = "{:.10f}".format(resultado)
    
        #agregar al grid
        self.grid_factura.insert("",END,text=nombre_repuesto,values=(self.producto,self.texto1_ingresado,self.text2_ingresado,self.total_precio,self.total_bs,resultado_como_cadena,nombre_empleado))
    def llenar_grid_detalle(self):
        self.grid_delalle_venta.delete(*self.grid_delalle_venta.get_children())
        datov=self.detalle_ventas.consulta_detalle_venta()
        for row in datov:
           self.grid_delalle_venta.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
    def eliminar_ve_factura(self):
        selected = self.grid_factura.focus()
        self.clave = self.grid_factura.item(selected, 'text')
        print(self.clave)
        if self.clave == '':
             messagebox.showwarning("modificar", 'debes seleccionar un elemento')
        else:
             self.grid_factura.delete(selected)
    def btn_venta_factura(self):
        
        self.total_veta_fact=CTkEntry(self.frame_venta_factura3,state="normal",fg_color="#2a2d2e",text_color="white",border_color='#2a2d2e')
        self.total_veta_fact.place(x=105,y=40)
        self.total_bs_fact=CTkEntry(self.frame_venta_factura3,state="normal",fg_color="#2a2d2e",text_color="white",border_color='#2a2d2e')
        self.total_bs_fact.place(x=105,y=60)
        self.total_com_fact=CTkEntry(self.frame_venta_factura3,state="normal",fg_color="#2a2d2e",text_color="white",border_color='#2a2d2e')
        self.total_com_fact.place(x=105,y=80)
        self.total_fecha_fact=CTkEntry(self.frame_venta_factura3,state="normal",fg_color="#2a2d2e",text_color="white",border_color='#2a2d2e')
        self.total_fecha_fact.place(x=105,y=100)
        self.total_emplid_fact=CTkEntry(self.frame_venta_factura3,state="normal",fg_color="#2a2d2e",text_color="white",border_color='#2a2d2e')
        self.total_emplid_fact.place(x=105,y=120)

        self.total = 0
        for fila in self.grid_factura.get_children():
           valor = self.grid_factura.set(fila, "col4")
           if valor:
              self.total += Decimal(valor)
        self.total_veta_fact.insert(0, Decimal(self.total))

        self.totalbs = 0
        for fila in self.grid_factura.get_children():
           valorbs = self.grid_factura.set(fila, "col5")
           if valorbs:
              self.totalbs += Decimal(valorbs)
        self.total_bs_fact.insert(0, "{:.2f}".format(Decimal(self.totalbs)))

        self.totalcom = 0
        for fila in self.grid_factura.get_children():
           valorcom = self.grid_factura.set(fila, "col6")
           if valorcom:
              self.totalcom += float(valorcom)
        self.total_com_fact.insert(0,float(self.totalcom))

        self.fecha_venta = self.fecha_factura.get()
        self.total_fecha_fact.insert(0,str(self.fecha_venta))

        self.id_empleado_venta = self.combo_emp.get()
        self.total_emplid_fact.insert(0,int(self.id_empleado_venta))
    def btn_guardar_venta(self):
        self.ventas.insertar_venta(self.total_emplid_fact.get() ,self.total_veta_fact.get() , self.total_bs_fact.get(), self.total_com_fact.get(),self.total_fecha_fact.get())
        self.id_venta=self.ventas.obtener_ultimo_registro_venta()
        self.fecha_detalle_gird=self.fecha_factura.get()
        fila_seleccionada = self.grid_factura.get_children()
        for fila in fila_seleccionada:
            valores = self.grid_factura.item(fila, 'values')
            columna1 = valores[0]
            columna2 = valores[1]
            columna3 = valores[2]
            columna4 = valores[3]
            columna5 = valores[4]
            columna6 = valores[5]
            self.detalle_ventas.insertar_detalle_venta(self.id_venta ,  columna4,   columna6, columna5, columna1, columna2,self.fecha_detalle_gird) 
        print(columna2)
        print(columna1)
        self.repuestos.disminuir_cantidad(columna2,columna1)       
    def llenar_grid_toplevel1(self):
        self.grid_tl_venta.delete(*self.grid_tl_venta.get_children())
        datosv=self.ventas.fecha_venta(self.entry_consulta_fecha1.get(),self.entry_consulta_fecha2.get())
        for row in datosv:
            self.grid_tl_venta.insert("",END,text=row[0],values=(row[1]))  
    def llenar_tl2(self):
        self.grid_tl_venta2.delete(*self.grid_tl_venta2.get_children())
        datosy=self.ventas.id_venta(self.entry_consulta_fecha1.get(),self.entry_consulta_fecha2.get())
        for row in datosy:
            self.grid_tl_venta2.insert("",END,text=row[0],values=(row[1],row[2],row[3]))      
    def llenar_tl3(self):
        self.grid_tl_venta3.delete(*self.grid_tl_venta3.get_children())
        datosy=self.ventas.total_v_id(self.entry_consulta_fecha1.get(),self.entry_consulta_fecha2.get())
        for row in datosy:
            self.grid_tl_venta3.insert("",END,text=row[0],values=(row[1],row[2]))      
    def llenar_tl4(self):
        self.grid_tl_venta4.delete(*self.grid_tl_venta4.get_children())
        datosy=self.ventas.total_v_fecha(self.entry_consulta_fecha1.get(),self.entry_consulta_fecha2.get())
        for row in datosy:
            self.grid_tl_venta4.insert("",END,text=row[0],values=(row[1]))        
    def top_level(self):
       self.ventana_toplevel = CTkToplevel(self,fg_color="#2a2d2e") 
       self.frametp_v= CTkFrame(self.ventana_toplevel,width=250,height=275,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
       self.frametp_v.place(x=20,y=30)
       self.frametp_v2= CTkFrame(self.ventana_toplevel,width=295,height=275,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
       self.frametp_v2.place(x=300,y=30) 
       self.frametp_v3= CTkFrame(self.ventana_toplevel,width=260,height=275,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
       self.frametp_v3.place(x=620,y=30)
       self.frametp_v4= CTkFrame(self.ventana_toplevel,width=220,height=220,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
       self.frametp_v4.place(x=20,y=325)
       #grid1
       self.grid_tl_venta = ttk.Treeview(self.frametp_v, columns=("col1"))
       self.grid_tl_venta.column("#0",width=30)            
       self.grid_tl_venta.column("col1",width=50,anchor=CENTER)  
       self.grid_tl_venta.heading("#0",text="Total venta",anchor=CENTER)
       self.grid_tl_venta.heading("col1",text="Fecha venta",anchor=CENTER)          
       self.grid_tl_venta.place(x=20,y=40,width=200,height=250)
       self.llenar_grid_toplevel1()
       scrollbar = ttk.Scrollbar(self.frametp_v, orient="vertical", command=self.grid_tl_venta.yview)
       self.grid_tl_venta.configure(yscrollcommand=scrollbar.set)
       scrollbar.place(x=230, y=40, height=250)
        #grid2
       self.grid_tl_venta2 = ttk.Treeview(self.frametp_v2, columns=("col1","col2","col3"))
       self.grid_tl_venta2.column("#0",width=30)            
       self.grid_tl_venta2.column("col1",width=60,anchor=CENTER)
       self.grid_tl_venta2.column("col2",width=60,anchor=CENTER)
       self.grid_tl_venta2.column("col3",width=60,anchor=CENTER)  
       self.grid_tl_venta2.heading("#0",text="Total venta",anchor=CENTER)
       self.grid_tl_venta2.heading("col1",text="Fecha venta",anchor=CENTER)    
       self.grid_tl_venta2.heading("col2",text="id empleado",anchor=CENTER)     
       self.grid_tl_venta2.heading("col3",text="comision",anchor=CENTER)           
       self.grid_tl_venta2.place(x=20,y=40,width=310,height=250)
       self.llenar_tl2()
       scrollbar2 = ttk.Scrollbar(self.frametp_v2, orient="vertical", command=self.grid_tl_venta2.yview)
       self.grid_tl_venta2.configure(yscrollcommand=scrollbar.set)
       scrollbar2.place(x=330, y=40, height=250)
       #grid3
       self.grid_tl_venta3= ttk.Treeview(self.frametp_v3, columns=("col1","col2"))
       self.grid_tl_venta3.column("#0",width=70)            
       self.grid_tl_venta3.column("col1",width=70,anchor=CENTER)
       self.grid_tl_venta3.column("col2",width=90,anchor=CENTER)
       self.grid_tl_venta3.heading("#0",text="Id empleado",anchor=CENTER)
       self.grid_tl_venta3.heading("col1",text="Total venta ",anchor=CENTER)   
       self.grid_tl_venta3.heading("col2",text="Total comision ",anchor=CENTER)   
       self.grid_tl_venta3.place(x=20,y=40,width=240,height=250)
       self.llenar_tl3()
       scrollbar3 = ttk.Scrollbar(self.frametp_v3, orient="vertical", command=self.grid_tl_venta3.yview)
       self.grid_tl_venta3.configure(yscrollcommand=scrollbar.set)
       scrollbar3.place(x=273, y=40, height=250)
       #grid4
       self.grid_tl_venta4= ttk.Treeview(self.frametp_v4, columns=("col1"))
       self.grid_tl_venta4.column("#0",width=30)           
       self.grid_tl_venta4.column("col1",width=50,anchor=CENTER)
       self.grid_tl_venta4.heading("#0",text="Fecha",anchor=CENTER)
       self.grid_tl_venta4.heading("col1",text="Total venta",anchor=CENTER)          
       self.grid_tl_venta4.place(x=20,y=40,width=200,height=220)
       self.llenar_tl4()
       scrollbar4 = ttk.Scrollbar(self.frametp_v4, orient="vertical", command=self.grid_tl_venta4.yview)
       self.grid_tl_venta4.configure(yscrollcommand=scrollbar.set)
       scrollbar4.place(x=242, y=40, height=220)     
    def fupdateven(self):
       self.grid_venta.delete(*self.grid_venta.get_children())
       datos = self.ventas.consulta_venta()
       for row in datos:
           self.grid_venta.insert("",END,text=row[0], values=(row[1],row[2],row[3],row[4],row[5]))
    def top_level_detalle(self):
        self.ventana_toplevel_de= CTkToplevel(self,fg_color="#2a2d2e")
        self.frame_d_tl= CTkFrame(self.ventana_toplevel_de,width=290,height=275,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frame_d_tl.place(x=20,y=40) 
        self.frame_d_tl2=CTkFrame(self.ventana_toplevel_de,width=460,height=275,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frame_d_tl2.place(x=370,y=40)
        self.grid_tl_venta2_d = ttk.Treeview(self.frame_d_tl, columns=("col1","col2","col3"))
        self.grid_tl_venta2_d.column("#0",width=70)            
        self.grid_tl_venta2_d.column("col1",width=90,anchor=CENTER)
        self.grid_tl_venta2_d.column("col2",width=90,anchor=CENTER)
        
        self.grid_tl_venta2_d.heading("#0",text="Total venta",anchor=CENTER)
        self.grid_tl_venta2_d.heading("col1",text="Total Bolivares",anchor=CENTER)   
        self.grid_tl_venta2_d.heading("col2",text="id repuesto",anchor=CENTER)     
          
        self.grid_tl_venta2_d.place(x=20,y=50,width=300,height=250)
        self.llenar_tlde()
        scrollbar = ttk.Scrollbar(self.frame_d_tl, orient="vertical", command=self.grid_tl_venta2_d.yview)
        self.grid_tl_venta2_d.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=330, y=50, height=250)
        #grid
        self.grid_tl_venta2_d2 = ttk.Treeview(self.frame_d_tl2, columns=("col1","col2","col3"))
        self.grid_tl_venta2_d2.column("#0",width=70)            
        self.grid_tl_venta2_d2.column("col1",width=90,anchor=CENTER)
        self.grid_tl_venta2_d2.column("col2",width=90,anchor=CENTER)
        self.grid_tl_venta2_d2.column("col3",width=90,anchor=CENTER)
        
        
        self.grid_tl_venta2_d2.heading("#0",text="Id repuesto",anchor=CENTER)
        self.grid_tl_venta2_d2.heading("col1",text="Total",anchor=CENTER)  
        self.grid_tl_venta2_d2.heading("col2",text="Total cantidad",anchor=CENTER)    
        self.grid_tl_venta2_d2.heading("col3",text="Total bolivares",anchor=CENTER)      
        self.grid_tl_venta2_d2.place(x=20,y=50,width=500,height=250)
        self.llenar_tlde2()
        scrollbar2 = ttk.Scrollbar(self.frame_d_tl2, orient="vertical", command=self.grid_tl_venta2_d2.yview)
        self.grid_tl_venta2_d2.configure(yscrollcommand=scrollbar.set)
        scrollbar2.place(x=523, y=50, height=250)
       #grid3
    def llenar_tlde(self):
        self.grid_tl_venta2_d.delete(*self.grid_tl_venta2_d.get_children())
        datosy=self.detalle_ventas.fecha_venta_de(self.entry_consultad_fecha1d.get(), self.entry_consultad_fecha2d.get())
        for row in datosy:
            self.grid_tl_venta2_d.insert("",END,text=row[0],values=(row[1],row[2]))
    def llenar_tlde2(self):
        self.grid_tl_venta2_d2.delete(*self.grid_tl_venta2_d2.get_children())
        datosv=self.detalle_ventas.total_v_id_detale(self.entry_consultad_fecha1d.get(),self.entry_consultad_fecha2d.get())
        for row in datosv:
            self.grid_tl_venta2_d2.insert("",END,text=row[0],values=(row[1],row[2],row[3])) 
    #botones compra
    def llenar_grid_compra(self):
        self.grid_compra.delete(*self.grid_compra.get_children())
        datov=self.compras.consulta_compra()
        for row in datov:
            self.grid_compra.insert("",END,text=row[0],values=(row[1],row[2],row[3]))     
    def agregar_compra(self):
        self.preoducto_c=self.combo_producto.get()
        self.precio_c_factura=self.precio_compra.get()
        self.cant_factura_c=self.compra_cant.get()
        self.f_factura_compra=self.fecha_factura_compra.get()

        print(self.precio_c_factura)
        print(self.preoducto_c)
        print(self.cant_factura_c)
        print(self.f_factura_compra)

        #datos del grid
        precio_dolar = self.dolars.obtener_ultimo_registro()
        nombre_repuesto=self.repuestos.nombre_repuesto(self.preoducto_c)
        precio=float(self.precio_c_factura)*float(self.cant_factura_c)
        total_bs=round(float(precio)*float(precio_dolar[0]),2)
        #agregar grid
        self.grid_factura_compra.insert("",END,text=nombre_repuesto,values=(self.preoducto_c,self.cant_factura_c,self.f_factura_compra,self.precio_c_factura,precio,total_bs,))  
    def btn_compra_fac(self):

        self.total_compra_fact=CTkEntry(self.frame_compra_factura3,state="normal",fg_color="#2a2d2e",text_color="white",border_color='#2a2d2e')
        self.total_compra_fact.place(x=115,y=47)
        self.total_bs_fact_compra=CTkEntry(self.frame_compra_factura3,state="normal",fg_color="#2a2d2e",text_color="white",border_color='#2a2d2e')
        self.total_bs_fact_compra.place(x=115,y=73)
        self.total_fecha_fact_compra=CTkEntry(self.frame_compra_factura3,state="normal",fg_color="#2a2d2e",text_color="white",border_color='#2a2d2e')
        self.total_fecha_fact_compra.place(x=115,y=100)
        

        self.total_compra = 0
        for fila in self.grid_factura_compra.get_children():
           valor = self.grid_factura_compra.set(fila, "col5")
           if valor:
              self.total_compra += Decimal(valor)
        self.total_compra_fact.insert(0, Decimal(self.total_compra))

        self.totalbs_compra = 0
        for fila in self.grid_factura_compra.get_children():
           valorbs = self.grid_factura_compra.set(fila, "col6")
           if valorbs:
              self.totalbs_compra += Decimal(valorbs)
        self.total_bs_fact_compra.insert(0, "{:.2f}".format(Decimal(self.totalbs_compra)))


        self.fecha__compra = self.fecha_factura_compra.get()
        self.total_fecha_fact_compra.insert(0,str(self.fecha__compra)) 
    def btn_guardar_compra(self):
        
        self.compras.insertar_compra(self.total_compra_fact.get(),self.total_bs_fact_compra.get(),self.fecha__compra)
        self.id_detalle_compra=self.compras.obtener_ultimo_registro_compra()
        fila_seleccionada = self.grid_factura_compra.get_children()
        for fila in fila_seleccionada:
            valores = self.grid_factura_compra.item(fila, 'values')
            columna1 = valores[0]
            columna2 = valores[1]
            columna3 = valores[2]
            columna4 = valores[3]
            columna5 = valores[4]
            columna6 = valores[5]

            n_r_c=self.repuestos.nombre_repuesto(columna1)

            self.compras.insertar_detalle_compra(columna1,self.id_detalle_compra, columna2,columna3, columna4,columna5,columna6,n_r_c)          
            self.repuestos.aumentra_cantidad(columna2,columna1)
    def eliminar_co_factura(self):
        selected = self.grid_factura_compra.focus()
        self.clave_co = self.grid_factura_compra.item(selected, 'text')
        print(self.clave_co)
        if self.clave_co == '':
             messagebox.showwarning("modificar", 'debes seleccionar un elemento')
        else:
             self.grid_factura_compra.delete(selected)  
    def llenar_grid_detalle_c(self):
        self.grid_factura_detalle.delete(*self.grid_factura_detalle.get_children())
        datov=self.compras.consulta_compra_detalle()
        for row in datov:
            self.grid_factura_detalle.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))   
    def top_level_compra(self):
        self.ventana_toplevel_compra = CTkToplevel(self,fg_color="#2a2d2e") 
        self.frametp_c= CTkFrame(self.ventana_toplevel_compra,width=295,height=275,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frametp_c.place(x=20,y=30)
        self.frametp_c1= CTkFrame(self.ventana_toplevel_compra,width=260,height=275,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frametp_c1.place(x=350,y=30)
        

        self.grid_tl_compra =ttk.Treeview(self.frametp_c, columns=("col1","col2","col3","col4"))
        self.grid_tl_compra.column("#0",width=70)            
        self.grid_tl_compra.column("col1",width=70,anchor=CENTER)
        self.grid_tl_compra.column("col2",width=90,anchor=CENTER)
        self.grid_tl_compra.column("col3",width=90,anchor=CENTER)
        self.grid_tl_compra.column("col4",width=90,anchor=CENTER)

        self.grid_tl_compra.heading("#0",text="Total compra",anchor=CENTER)
        self.grid_tl_compra.heading("col1",text="Total bs ",anchor=CENTER)   
        self.grid_tl_compra.heading("col2",text="Fecha ",anchor=CENTER)   
        self.grid_tl_compra.heading("col4",text="Id compra ",anchor=CENTER) 
        self.grid_tl_compra.place(x=20,y=40,width=240,height=250)
        self.llenar_tlc()
        scrollbar= ttk.Scrollbar(self.frametp_c, orient="vertical", command=self.grid_tl_compra.yview)
        self.grid_tl_compra.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=293, y=40, height=250)

        self.grid_tl_compra3 =ttk.Treeview(self.frametp_c1, columns=("col1"))
        self.grid_tl_compra3.column("#0",width=70)            
        self.grid_tl_compra3.column("col1",width=70,anchor=CENTER)
        self.grid_tl_compra3.heading("#0",text="Total venta ",anchor=CENTER)   
        self.grid_tl_compra3.heading("col1",text="Total comision ",anchor=CENTER) 
        self.grid_tl_compra3.place(x=40,y=40,width=200,height=200)
        self.llenar_tlc2()
        scrollbar3= ttk.Scrollbar(self.frametp_c1, orient="vertical", command=self.grid_tl_compra3.yview)
        self.grid_tl_compra3.configure(yscrollcommand=scrollbar.set)
        scrollbar3.place(x=243, y=40, height=200)
    def llenar_tlc(self):
        self.grid_tl_compra.delete(* self.grid_tl_compra.get_children())
        datosy=self.compras.fecha_compra(self.entry_consulta_fecha1c.get(),self.entry_consulta_fecha2c.get())
        for row in datosy:
            self.grid_tl_compra.insert("",END,text=row[0],values=(row[1],row[2],row[3]))    
    def llenar_tlc2(self):
        self.grid_tl_compra3.delete(* self.grid_tl_compra3.get_children())
        datosy=self.compras.total_c_fecha(self.entry_consulta_fecha1c.get(),self.entry_consulta_fecha2c.get())
        for row in datosy:
            self.grid_tl_compra3.insert("",END,text=row[0],values=(row[1]))  
    def top_level_d_compra(self):
        self.ventana_toplevel_comprad = CTkToplevel(self,fg_color="#2a2d2e") 
        self.frame_dc= CTkFrame(self.ventana_toplevel_comprad,width=315,height=275,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frame_dc.place(x=30,y=30) 
        self.frame_dc1= CTkFrame(self.ventana_toplevel_comprad,width=330,height=275,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frame_dc1.place(x=500,y=30) 

        self.grid_tl_comprad = ttk.Treeview(self.frame_dc, columns=("col1","col2","col3","col4"))
        self.grid_tl_comprad.column("#0",width=60)            
        self.grid_tl_comprad.column("col1",width=60,anchor=CENTER)
        self.grid_tl_comprad.column("col2",width=60,anchor=CENTER)
        self.grid_tl_comprad.column("col3",width=60,anchor=CENTER) 
        self.grid_tl_comprad.column("col4",width=60,anchor=CENTER) 
        self.grid_tl_comprad.heading("#0",text="Repuesto",anchor=CENTER)
        self.grid_tl_comprad.heading("col1",text="Cantidad",anchor=CENTER)    
        self.grid_tl_comprad.heading("col2",text="Precio ",anchor=CENTER)     
        self.grid_tl_comprad.heading("col3",text="Total",anchor=CENTER)    
        self.grid_tl_comprad.heading("col4",text="Total bs",anchor=CENTER)        
        self.grid_tl_comprad.place(x=20,y=40,width=330,height=250)
        self.tl_cd()
        scrollbar = ttk.Scrollbar(self.frame_dc, orient="vertical", command=self.grid_tl_comprad.yview)
        self.grid_tl_comprad.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=360, y=40, height=250)
       #grid3
        self.grid_tl_comprad1 = ttk.Treeview(self.frame_dc1, columns=("col1","col2","col3"))
        self.grid_tl_comprad1.column("#0",width=60)            
        self.grid_tl_comprad1.column("col1",width=60,anchor=CENTER)
        self.grid_tl_comprad1.column("col2",width=60,anchor=CENTER)
        self.grid_tl_comprad1.column("col3",width=60,anchor=CENTER) 
        self.grid_tl_comprad1.heading("#0",text="Repuesto",anchor=CENTER)
        self.grid_tl_comprad1.heading("col1",text="Total Cantidad",anchor=CENTER)    
        self.grid_tl_comprad1.heading("col2",text="Total ",anchor=CENTER)     
        self.grid_tl_comprad1.heading("col3",text="Total bs",anchor=CENTER)    
        self.grid_tl_comprad1.place(x=20,y=40,width=330,height=250)
        self.tl_cd1()
        scrollbar2 = ttk.Scrollbar(self.frame_dc1, orient="vertical", command=self.grid_tl_comprad1.yview)
        self.grid_tl_comprad1.configure(yscrollcommand=scrollbar.set)
        scrollbar2.place(x=360, y=40, height=250)
    def tl_cd(self):
        self.grid_tl_comprad.delete(* self.grid_tl_comprad.get_children())
        datosy=self.compras.fecha_c_de(self.entry_consultac_fecha1d.get(), self.entry_consultac_fecha2d.get())
        for row in datosy:
            self.grid_tl_comprad.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4]))  
    def tl_cd1(self):
        self.grid_tl_comprad1.delete(* self.grid_tl_comprad1.get_children())
        datosy=self.compras.total_cd(self.entry_consultac_fecha1d.get(), self.entry_consultac_fecha2d.get())
        for row in datosy:
            self.grid_tl_comprad1.insert("",END,text=row[0],values=(row[1],row[2],row[3]))  
    #botones repuesto
    def guardar_repuesto(self):

        self.repuestos.insertar_repuestos(self.textnombrere.get(),self.textreferencia.get(),self.textopreciore.get(),self.textcantidadre.get(),self.combo_empre.get())
        id_re=self.repuestos.obtener_ultimo_registro_repuesto()
        preciore=self.repuestos.precio_repuesto(id_re)
        self.repuestos.calcular_precio_bolivar(id_re,preciore)
        self.llenar_grid_repuesto()
        jd=self.repuestos.nombre_repuesto(id_re)
        self.repuestos.busqueda_repuesto(jd)
         
    def limpiar_guardar_repuesto(self):
        self.textnombrere.delete(0,END)
        self.textreferencia.delete(0,END)
        self.textopreciore.delete(0,END)
        self.cantidadre.delete(0,END)
    def llenar_grid_repuesto(self):
        self.grid_repuesto.delete(*self.grid_repuesto.get_children())
        datov=self.repuestos.consulta_repuestos()
        for row in datov:
            self.grid_repuesto.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
    def act_repuesto(self):
        selected = self.grid_repuesto.focus()
        self.clavere = self.grid_repuesto.item(selected, 'text')
        print(self.clavere)
        if self.clavere == '':
             messagebox.showwarning("modificar", 'debes seleccionar un elemento')
        else:
         valores = self.grid_repuesto.item(selected, 'values')
         self.textnombrere.insert(0, valores[0])
         self.textreferenciare.insert(0, valores[1])
         self.preciore.insert(0, valores[2])
         self.cantidadre.insert(0, valores[3])
    def limpiar_act_repuesto(self):
        self.textnombrere.delete(0,END)
        self.textreferenciare.delete(0,END)
        self.preciore.delete(0,END)
        self.cantidadre.delete(0,END)
    def btn_act_re(self):
        self.repuestos.modificar_repuesto(self.clavere,self.textnombrere.get(),self.textreferenciare.get(),self.preciore.get(),self.cantidadre.get())
        self.limpiar_act_repuesto()
    def consulta_repuesto(self):
        nrepuesto=self.econsultare.get()
        self.grid_repuesto.delete(*self.grid_repuesto.get_children())
        datos=self.repuestos.busqueda_repuesto(nrepuesto)
        for row in datos:
            self.grid_repuesto.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
    #botones vehiculos
    def llenar_grid_vehiculo(self):
        self.grid_vehiculo.delete(*self.grid_vehiculo.get_children())
        datov=self.vehiculos.consulta_vehiculos()
        for row in datov:
            self.grid_vehiculo.insert("",END,text=row[0],values=(row[1],row[2],row[3]))  
    def guardar_ve(self):
        self.vehiculos.insertar_veh( self.textnombrerev.get(), self.textreferenciav.get(),self.textopreciorev.get())  
    def eli_ve(self):
        self.eliminar_vehiculo = CTkEntry(self.Frame_vehiculo2,placeholder_text="ingrese el id",width=100,fg_color="#2a2d2e",text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32)
        self.eliminar_vehiculo.place(x=20,y=120)
        self.btn_confirmar_eliminacionv = CTkButton(self.Frame_vehiculo2,text="confirmar",command=self.eliminarve,fg_color="green",text_color='white',width=70)
        self.btn_confirmar_eliminacionv.place(x=40,y=150)
    def eliminarve(self):
        self.vehiculos.eliminar_veh(self.eliminar_vehiculo.get())
        self.eliminar_vehiculo.delete(0, 'end')
    #botones dolar
    def g_dolar(self):
        self.dolars.insertar_dolar(self.textnombrered.get(), self.textreferenciad.get()) 
    def llenar_g_Dolar(self):
        self.grid_dolar.delete(*self.grid_dolar.get_children())
        datov=self.dolars.consulta_dolar()
        for row in datov:
            self.grid_dolar.insert("",END,text=row[0],values=(row[1],row[2]))  
    
    #menulateral
    def create_widgets(self):
        #imagenes
        self.mi_image = ImageTk.PhotoImage(Image.open("comentario-dolar.png").resize((40,40)))
        self.mi_empleado = ImageTk.PhotoImage(Image.open("usuarios-alt.png").resize((40,40)))
        self.mi_compra = ImageTk.PhotoImage(Image.open("carrito-de-compras (2).png").resize((40,40)))
        self.mi_inventario = ImageTk.PhotoImage(Image.open("alt-de-inventario.png").resize((40,40)))
        self.mi_repuesto = ImageTk.PhotoImage(Image.open("dharmachakra.png").resize((40,40)))
        self.mi_vehiculo= ImageTk.PhotoImage(Image.open("ciclomotor.png").resize((40,40)))
        self.inicio=ImageTk.PhotoImage(Image.open("hogar (1).png").resize((40,40)))
        #Frame
        self.Frametop=CTkFrame(self,width=1090,height=45,fg_color="#2a2d2e")
        self.Frametop.place(x=0,y=0)
        self.Framemenu = CTkFrame(self, width=150,height=480,fg_color="#2a2d2e")
        self.Framemenu.place(x=0,y=50)
        self.Frame_home=CTkFrame(self,width=938,height=480,fg_color="#2a2d2e")
        self.Frame_home.place(x=150,y=50)
        self.Frame_dolar=CTkFrame(self.Frame_home,width=290,height=275,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.Frame_dolar.place(x=20,y=40) 
        self.Frame_dolar2=CTkFrame(self.Frame_home,width=290,height=275,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.Frame_dolar2.place(x=320,y=40)
        #HOME
        lbl=CTkLabel(self.Frame_dolar2,text="Precio Dolar",font=("Arial",25),text_color="white")
        lbl.place(x=100,y=5)
        lbli=CTkLabel(self.Frame_dolar,text="ingresar",font=("Arial",25),text_color="white")
        lbli.place(x=100,y=5)
        lbli1=CTkLabel(self.Frame_dolar,text="Fecha",font=("Arial",15),text_color="white")
        lbli1.place(x=10,y=70)
        lbli2=CTkLabel(self.Frame_dolar,text="Precio",font=("Arial",15),text_color="white")
        lbli2.place(x=10,y=100)
        self.btnguardarv=CTkButton(self.Frame_dolar,text="Guardar",command=self.g_dolar,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32,width=50)
        self.btnguardarv.place(x=80,y=230)
        self.textnombrered= CTkEntry(self.Frame_dolar,placeholder_text="Fecha",fg_color="#2a2d2e",text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32)
        self.textnombrered.place(x=120,y=70)
        self.textreferenciad= CTkEntry(self.Frame_dolar,placeholder_text="Precio",fg_color="#2a2d2e",text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32)
        self.textreferenciad.place(x=120,y=100)
        style = ttk.Style()
   
        style.theme_use("default")
   
        style.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=25,
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
   
        style.configure("Treeview.Heading",
                            background="#565b5e",
                            foreground="white",
                            relief="flat")
        style.map("Treeview.Heading",
                      background=[('active', '#3484F0')])
        #GRID
        self.grid_dolar = ttk.Treeview(self.Frame_dolar2, columns=("col1","col2","col3"))
        self.grid_dolar.column("#0",width=70)            
        self.grid_dolar.column("col1",width=90,anchor=CENTER)
        self.grid_dolar.column("col2",width=90,anchor=CENTER)
        
        self.grid_dolar.heading("#0",text="Id",anchor=CENTER)
        self.grid_dolar.heading("col1",text="Fecha",anchor=CENTER)   
        self.grid_dolar .heading("col2",text="Precio",anchor=CENTER)     
          
        self.grid_dolar.place(x=20,y=50,width=300,height=250)
        self.llenar_g_Dolar()
        scrollbar = ttk.Scrollbar(self.Frame_dolar2, orient="vertical", command=self.grid_dolar.yview)
        self.grid_dolar.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=323, y=50, height=250)
        #TOP
        nombre_em=CTkLabel(self.Frametop,text="REPUESTOS JME",font=("Arial",30),text_color="white")
        nombre_em.place(x=450,y=5)
        # BOTONES
        self.btn_inicio = CTkButton(self.Framemenu, text="Inicio        ",command=self.create_widgets,image=self.inicio,fg_color='transparent', text_color='white',height=30)
        self.btn_inicio.place(x=0, y=10)
        self.btn_compra = CTkButton(self.Framemenu, text="Compra    ", command=self.mostra_ventana_compra, image=self.mi_compra, fg_color='transparent', text_color='white',height=30)
        self.btn_compra.place(x=0, y=55)
        self.btn_venta = CTkButton(self.Framemenu, text="Ventas     ", command=self.mostrar_ventana_consulta_venta,image=self.mi_image,fg_color='transparent',text_color='white',height=30)
        self.btn_venta.place(x=0, y=100)
        self.btn_empleado = CTkButton(self.Framemenu, text="Empleado", command=self.consultar_empleado, image=self.mi_empleado, fg_color='transparent', text_color='white',height=30)
        self.btn_empleado.place(x=0, y=145)
        self.btn_repuesto = CTkButton(self.Framemenu, text="Repuesto  ",command=self.mostrar_ventana_repuesto,image=self.mi_repuesto,  fg_color='transparent', text_color='white',height=30)
        self.btn_repuesto.place(x=0, y=190)
        self.btn_vehiculos = CTkButton(self.Framemenu, text="Vehiculos",command=self.mostrar_ventana_vehiculos,image=self.mi_vehiculo,fg_color='transparent',text_color='white',height=30)
        self.btn_vehiculos.place(x=0, y=240)
    #ventanas empleados
    def mostrar_ventana_empleado(self):
        self.Frame_prin=CTkFrame(self,width=938,height=480,fg_color="#2a2d2e")
        self.Frame_prin.place(x=150,y=50)
        self.Frame_prin2=CTkFrame(self.Frame_prin,width=650,height=250,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.Frame_prin2.place(x=280,y=110)
        #top
        btn_consultar_empleado = CTkButton(self.Frame_prin,text="consultar",command=self.consultar_empleado,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_consultar_empleado.place(x=250,y=3)
        btn_insetar_empleado = CTkButton(self.Frame_prin, text="insertar",command=self.inser_emplea, fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_insetar_empleado.place(x=400,y=3)
        btn_actualizar_empleado = CTkButton(self.Frame_prin, text="actualizar",command=self.act_empl,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_actualizar_empleado.place(x=550,y=3)

        lbl=CTkLabel(self.Frame_prin2,text="EMPLEADOS",font=("Arial",20),text_color="white")
        lbl.place(x=220,y=10)
        style = ttk.Style()
   
        style.theme_use("default")
   
        style.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=25,
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
   
        style.configure("Treeview.Heading",
                            background="#565b5e",
                            foreground="white",
                            relief="flat")
        style.map("Treeview.Heading",
                      background=[('active', '#3484F0')])
        

        self.grid = ttk.Treeview(self.Frame_prin2, columns=("col1","col2","col3","col4","col5","col6","col7"),style="Treeview")

        self.grid.column("#0",width=30)            
        self.grid.column("col1",width=50,anchor=CENTER)
        self.grid.column("col2",width=50,anchor=CENTER)
        self.grid.column("col3",width=70,anchor=CENTER)
        self.grid.column("col4",width=50,anchor=CENTER)
        self.grid.column("col5",width=80,anchor=CENTER)
        self.grid.column("col6",width=50,anchor=CENTER)
        self.grid.column("col7",width=80,anchor=CENTER)

        self.grid.heading("#0",text="Id",anchor=CENTER)
        self.grid.heading("col1",text="Nombre",anchor=CENTER)
        self.grid.heading("col2",text="Apellido",anchor=CENTER)
        self.grid.heading("col3",text="fecha de nacimiento",anchor=CENTER)
        self.grid.heading("col4",text="telefono",anchor=CENTER)
        self.grid.heading("col5",text="correo",anchor=CENTER)
        self.grid.heading("col6",text="cargo",anchor=CENTER)
        self.grid.heading("col7",text="fecha de contratacion",anchor=CENTER)
        self.grid.place(x=10,y=50,width=780,height=230)
        self.factualizar()
        scrollbar = ttk.Scrollbar(self.Frame_prin2, orient="vertical", command=self.grid.yview)
        self.grid.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=794, y=50, height=230)
    def inser_emplea(self):
        #FRAME
        self.Frame_princ=CTkFrame(self,width=938,height=480,fg_color="#2a2d2e")
        self.Frame_princ.place(x=150,y=50)
        self.Frame_princ2=CTkFrame(self.Frame_princ,width=320,height=325,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.Frame_princ2.place(x=315,y=70)
        #BOTONES
        btn_consultar_empleado = CTkButton(self.Frame_princ,text="Consultar",command=self.consultar_empleado,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_consultar_empleado.place(x=250,y=3)
        btn_insetar_empleado = CTkButton(self.Frame_princ, text="Insertar",command=self.inser_emplea, fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_insetar_empleado.place(x=400,y=3)
        btn_actualizar_empleado = CTkButton(self.Frame_princ, text="Actualizar", command=self.act_empl,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_actualizar_empleado.place(x=550,y=3)
        #CONTENIDO
        self.textnombre= CTkEntry(self.Frame_princ2,placeholder_text="Nombre",width=120)
        self.textnombre.place(x=146,y=70)
        self.textapellido= CTkEntry(self.Frame_princ2,placeholder_text="Apellido",width=120)
        self.textapellido.place(x=146,y=100)
        self.textfdn= CTkEntry(self.Frame_princ2,placeholder_text="Fecha de nacimiento",width=120)
        self.textfdn.place(x=146,y=130)
        self.texttlf= CTkEntry(self.Frame_princ2,placeholder_text="Telefono",width=120)
        self.texttlf.place(x=146,y=160)
        self.textcorreo= CTkEntry(self.Frame_princ2,placeholder_text="Correo",width=120)
        self.textcorreo.place(x=146,y=190)
        self.textcargo=CTkEntry(self.Frame_princ2,placeholder_text="Cargo",width=120)
        self.textcargo.place(x=146,y=220)
        self.textfdc= CTkEntry(self.Frame_princ2,placeholder_text="Fecha de contratacion",width=120)
        self.textfdc.place(x=146,y=250)
        self.btnguardar=CTkButton(self.Frame_princ2,text="Guardar",command=self.guardar_empleado,border_color='#FFCC70',border_width=2,corner_radius=32,width=50,fg_color="green")
        self.btnguardar.place(x=110,y=290)
        
        #label
        lbl=CTkLabel(self.Frame_princ2,text="ingresar",text_color="white",font=("Arial",30))
        lbl.place(x=100,y=5)
        lbli1=CTkLabel(self.Frame_princ2,text="Nombre",text_color="white")
        lbli1.place(x=10,y=70)
        lbli2=CTkLabel(self.Frame_princ2,text="Apellido",text_color="white")
        lbli2.place(x=10,y=100)
        lbli3=CTkLabel(self.Frame_princ2,text="Fecha de nacimiento",text_color="white")
        lbli3.place(x=10,y=130)
        lbli4=CTkLabel(self.Frame_princ2,text="Telefono",text_color="white")
        lbli4.place(x=10,y=160)
        lbli5=CTkLabel(self.Frame_princ2,text="Correo",text_color="white")
        lbli5.place(x=10,y=190)
        lbli6=CTkLabel(self.Frame_princ2,text="Cargo",text_color="white")
        lbli6.place(x=10,y=220)
        lbli7=CTkLabel(self.Frame_princ2,text="Fecha de contratacion",text_color="white")
        lbli7.place(x=10,y=250)
    def consultar_empleado(self):
            #FRAME
            self.Frame_cone=CTkFrame(self,width=938,height=480,fg_color="#2a2d2e")
            self.Frame_cone.place(x=150,y=50) 
            self.Frame_cone2=CTkFrame(self.Frame_cone,width=680,height=250,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
            self.Frame_cone2.place(x=180,y=50)
            self.Frame_cone3=CTkFrame(self.Frame_cone,width=150,height=250,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
            self.Frame_cone3.place(x=10,y=50)
            #TOP
            #TOP
            btn_consultar_empleado = CTkButton(self.Frame_cone,text="consultar",command=self.consultar_empleado,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
            btn_consultar_empleado.place(x=250,y=3)
            btn_insetar_empleado = CTkButton(self.Frame_cone, text="insertar",command=self.inser_emplea, fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
            btn_insetar_empleado.place(x=400,y=3)
            btn_actualizar_empleado = CTkButton(self.Frame_cone, text="actualizar",command=self.act_empl,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
            btn_actualizar_empleado.place(x=550,y=3)
            #botonesdelcontenido
            btn_actualizar=CTkButton(self.Frame_cone3,text="refrescar",command=self.factualizar,fg_color="#2a2d2e",text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32)
            btn_actualizar.place(x=5,y=55)
            btn_actualizar=CTkButton(self.Frame_cone3,text="eliminar",command=self.eliminar_empleado,fg_color="#2a2d2e",text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32)
            btn_actualizar.place(x=5,y=90)
            #label
            lbl=CTkLabel(self.Frame_cone2,text="EMPLEADOS",font=("Arial",20),text_color="white")
            lbl.place(x=220,y=5)
            style = ttk.Style()
            style.theme_use("default")
            style.configure("Treeview",
                                background="#2a2d2e",
                                foreground="white",
                                rowheight=25,
                                fieldbackground="#343638",
                                bordercolor="#343638",
                                borderwidth=0)
            style.map('Treeview', background=[('selected', '#22559b')])
            style.configure("Treeview.Heading",
                                background="#565b5e",
                                foreground="white",
                                relief="flat")
            style.map("Treeview.Heading",
                        background=[('active', '#3484F0')])

            self.grid = ttk.Treeview(self.Frame_cone2, columns=("col1","col2","col3","col4","col5","col6","col7"),style="Treeview")

            self.grid.column("#0",width=30)
            self.grid.column("col1",width=50,anchor=CENTER)
            self.grid.column("col2",width=50,anchor=CENTER)
            self.grid.column("col3",width=70,anchor=CENTER)
            self.grid.column("col4",width=50,anchor=CENTER)
            self.grid.column("col5",width=50,anchor=CENTER)
            self.grid.column("col6",width=50,anchor=CENTER)
            self.grid.column("col7",width=80,anchor=CENTER)

            self.grid.heading("#0",text="Id",anchor=CENTER)
            self.grid.heading("col1",text="Nombre",anchor=CENTER)
            self.grid.heading("col2",text="Apellido",anchor=CENTER)
            self.grid.heading("col3",text="fecha de nacimiento",anchor=CENTER)
            self.grid.heading("col4",text="telefono",anchor=CENTER)
            self.grid.heading("col5",text="correo",anchor=CENTER)
            self.grid.heading("col6",text="cargo",anchor=CENTER)
            self.grid.heading("col7",text="fecha de contratacion",anchor=CENTER)
            self.grid.place(x=10,y=50,width=800,height=200)
            self.factualizar()
            scrollbar = ttk.Scrollbar(self.Frame_cone2, orient="vertical", command=self.grid.yview)
            self.grid.configure(yscrollcommand=scrollbar.set)
            scrollbar.place(x=818, y=50, height=200)    
    def act_empl(self):
        #frame
        self.Frame_cone=CTkFrame(self,width=938,height=480,fg_color="#2a2d2e")
        self.Frame_cone.place(x=150,y=50)
        self.Frame_cone2=CTkFrame(self.Frame_cone,width=680,height=300,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.Frame_cone2.place(x=210,y=50)
        self.Frame_cone3=CTkFrame(self.Frame_cone,width=180,height=300,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.Frame_cone3.place(x=10,y=50)
        #botones
        btn_consultar_empleado = CTkButton(self.Frame_cone,text="consultar",command=self.consultar_empleado,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_consultar_empleado.place(x=250,y=3)
        btn_insetar_empleado = CTkButton(self.Frame_cone, text="insertar",command=self.inser_emplea, fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_insetar_empleado.place(x=400,y=3)
        btn_actualizar_empleado = CTkButton(self.Frame_cone, text="actualizar", fg_color="#2a2d2e", command=self.act_empl,text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_actualizar_empleado.place(x=550,y=3)


        style = ttk.Style()
   
        style.theme_use("default")
   
        style.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=25,
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
   
        style.configure("Treeview.Heading",
                            background="#565b5e",
                            foreground="white",
                            relief="flat")
        style.map("Treeview.Heading",
                      background=[('active', '#3484F0')])
        

        self.grid = ttk.Treeview(self.Frame_cone2, columns=("col1","col2","col3","col4","col5","col6","col7"),style="Treeview")

        self.grid.column("#0",width=30)            
        self.grid.column("col1",width=50,anchor=CENTER)
        self.grid.column("col2",width=50,anchor=CENTER)
        self.grid.column("col3",width=70,anchor=CENTER)
        self.grid.column("col4",width=50,anchor=CENTER)
        self.grid.column("col5",width=80,anchor=CENTER)
        self.grid.column("col6",width=50,anchor=CENTER)
        self.grid.column("col7",width=80,anchor=CENTER)

        self.grid.heading("#0",text="Id",anchor=CENTER)
        self.grid.heading("col1",text="Nombre",anchor=CENTER)
        self.grid.heading("col2",text="Apellido",anchor=CENTER)
        self.grid.heading("col3",text="fecha de nacimiento",anchor=CENTER)
        self.grid.heading("col4",text="telefono",anchor=CENTER)
        self.grid.heading("col5",text="correo",anchor=CENTER)
        self.grid.heading("col6",text="cargo",anchor=CENTER)
        self.grid.heading("col7",text="fecha de contratacion",anchor=CENTER)
        self.grid.place(x=10,y=40,width=800,height=250)
        self.factualizar()
        scrollbar = ttk.Scrollbar(self.Frame_cone2, orient="vertical", command=self.grid.yview)
        self.grid.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=820, y=40, height=250)
        self.grid['selectmode']='browse'
        btn_act=CTkButton(self.Frame_cone3,text="actualizar",command= self.act_empleado,fg_color="#2a2d2e",text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30,width=30)
        btn_act.place(x=40,y=4)
        #entry
        self.textnombrea= CTkEntry(self.Frame_cone3,placeholder_text="nombre")
        self.textnombrea.place(x=10,y=40)
        self.textapellidoa= CTkEntry(self.Frame_cone3,placeholder_text="apellido")
        self.textapellidoa.place(x=10,y=70)
        self.textfdna= CTkEntry(self.Frame_cone3,placeholder_text="fecha de nacimiento")
        self.textfdna.place(x=10,y=100)
        self.texttlfa= CTkEntry(self.Frame_cone3,placeholder_text="telefono")
        self.texttlfa.place(x=10,y=130)
        self.textcorreoa= CTkEntry(self.Frame_cone3,placeholder_text="correo")
        self.textcorreoa.place(x=10,y=160)
        self.textcargoa=CTkEntry(self.Frame_cone3,placeholder_text="cargo")
        self.textcargoa.place(x=10,y=190)
        self.textfdca= CTkEntry(self.Frame_cone3,placeholder_text="fecha de contratacion")
        self.textfdca.place(x=10,y=220)
        self.btnguardaract=CTkButton(self.Frame_cone3,text="guardar",command=self.act_boton_guardar,border_color='#FFCC70',border_width=2,corner_radius=32)
        self.btnguardaract.place(x=10,y=250)
    #ventanas compra
    def mostra_ventana_compra(self):
        self.frame_compra_inicio=CTkFrame(self,width=938,height=480,fg_color="#2a2d2e")
        self.frame_compra_inicio.place(x=150,y=50)
        self.frame_compra_inicio2=CTkFrame(self.frame_compra_inicio,width=588,height=320,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frame_compra_inicio2.place(x=220,y=50)
        self.frame_cvc= CTkFrame(self.frame_compra_inicio,width=167,height=320,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frame_cvc.place(x=20,y=50)
        #label
        #top
        btn_consultar_compra = CTkButton(self.frame_compra_inicio,text="Consultar",command=self.mostra_ventana_compra,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_consultar_compra.place(x=250,y=3)
        btn_insetar_empleado = CTkButton(self.frame_compra_inicio, text="Insertar",command=self.mostrar_ventana_fac_compra,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_insetar_empleado.place(x=400,y=3)
        btn_actualizar_empleado = CTkButton(self.frame_compra_inicio, text="Detalle",command=self.mostrar_ventana_detalle_compra,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_actualizar_empleado.place(x=550,y=3)
        #label
        lbl=CTkLabel(self.frame_compra_inicio2,text="COMPRAS",font=("Arial",20),text_color="white")
        lbl.place(x=236,y=10)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=25,
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
   
        style.configure("Treeview.Heading",
                            background="#565b5e",
                            foreground="white",
                            relief="flat")
        style.map("Treeview.Heading",
                      background=[('active', '#3484F0')])
        #grid
        self.grid_compra = ttk.Treeview(self.frame_compra_inicio2, columns=("col1","col2","col3"),style="Treeview")
        self.grid_compra.column("#0",width=30)            
        self.grid_compra.column("col1",width=50,anchor=CENTER)
        self.grid_compra.column("col2",width=50,anchor=CENTER)
        self.grid_compra.column("col3",width=70,anchor=CENTER)
        self.grid_compra.heading("#0",text="Id compra",anchor=CENTER)
        self.grid_compra.heading("col1",text="Total compra",anchor=CENTER)
        self.grid_compra.heading("col2",text="Total bolivares",anchor=CENTER)
        self.grid_compra.heading("col3",text="Fecha",anchor=CENTER)
        self.grid_compra.place(x=114,y=50,width=500,height=300)
        self.llenar_grid_compra()
        scrollbar = ttk.Scrollbar(self.frame_compra_inicio2, orient="vertical", command=self.grid_compra.yview)
        self.grid_compra.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=620, y=50, height=300)

        lbl1=CTkLabel(self.frame_cvc,text="CONSULTA COMPRAS",text_color="white")
        lbl1.place(x=20,y=5)
        lbl2=CTkLabel(self.frame_cvc,text="Desde",text_color="white")
        lbl2.place(x=20,y=25)
        lbl3=CTkLabel(self.frame_cvc,text="Hasta",text_color="white")
        lbl3.place(x=20,y=75)
        #botones
        btn_confimar_consulta=CTkButton(self.frame_cvc,text="Confirmar",width=70,fg_color="green",command=self.top_level_compra)
        btn_confimar_consulta.place(x=20,y=200)
        #entry
        self.entry_consulta_fecha1c=CTkEntry(self.frame_cvc,width=90,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32)
        self.entry_consulta_fecha1c.place(x=15,y=48)
        self.entry_consulta_fecha2c=CTkEntry(self.frame_cvc,width=90,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32)
        self.entry_consulta_fecha2c.place(x=15,y=98)
    def mostrar_ventana_fac_compra(self):
        self.ids_repuestos_compra = self.repuestos.id_repuesto()
        self.valores_repuesto_compra = [str(id) for id in self.ids_repuestos_compra]
        #Frame
        self.frame_compra_factura=CTkFrame(self,width=938,height=480,fg_color="#2a2d2e")
        self.frame_compra_factura.place(x=150,y=50)
        self.frame_compra_factura2=CTkFrame(self.frame_compra_factura,width=740,height=237,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frame_compra_factura2.place(x=70,y=50)
        self.frame_compra_factura3=CTkFrame(self.frame_compra_factura,width=300,height=180,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frame_compra_factura3.place(x=70,y=297)
        
        #top
        btn_consultar_compra = CTkButton(self.frame_compra_factura,text="Consultar",command=self.mostra_ventana_compra,fg_color="#2a2d2e", border_color='#FFCC70',border_width=2,corner_radius=32,text_color='white',height=30)
        btn_consultar_compra.place(x=250,y=3)
        btn_insetar_empleado = CTkButton(self.frame_compra_factura, text="Factura",command=self.mostrar_ventana_fac_compra,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_insetar_empleado.place(x=400,y=3)
        btn_actualizar_empleado = CTkButton(self.frame_compra_factura, text="Detalle",command=self.mostrar_ventana_detalle_compra,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32, text_color='white',height=30)
        btn_actualizar_empleado.place(x=550,y=3)
        #label
        lblfactura1=CTkLabel(self.frame_compra_factura2,text="Producto",text_color="white")
        lblfactura1.place(x=50,y=55)
        lblfactura2=CTkLabel(self.frame_compra_factura2,text="Precio",text_color="white")
        lblfactura2.place(x=205,y=55)
        lblfactura3=CTkLabel(self.frame_compra_factura2,text="Cantidad",text_color="white")
        lblfactura3.place(x=350,y=55)
        lblfactura4=CTkLabel(self.frame_compra_factura2,text="Fecha",text_color="white")
        lblfactura4.place(x=510,y=55)
        lblfactura5=CTkLabel(self.frame_compra_factura2,text="Factura Compra",text_color="white",font=("Arial",15))
        lblfactura5.place(x=310,y=10)
        lblfactura5=CTkLabel(self.frame_compra_factura3,text="TOTAL",text_color="white",font=("Arial",20))
        lblfactura5.place(x=110,y=10)
        lblv1=CTkLabel(self.frame_compra_factura3,text="Total precio:  ",text_color="white")
        lblv1.place(x=10,y=47)
        lblv2=CTkLabel(self.frame_compra_factura3,text="Total bolivares:",text_color="white")
        lblv2.place(x=10,y=73)
        lblv2=CTkLabel(self.frame_compra_factura3,text="Fecha:",text_color="white")
        lblv2.place(x=10,y=100)

        
        #combobox
        self.combo_producto = CTkComboBox(self.frame_compra_factura2,values=self.valores_repuesto_compra,width=90,height=20,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32,text_color="white")
        self.combo_producto.place(x=110, y=55)
        #entry
        self.precio_compra=CTkEntry(self.frame_compra_factura2,width=90,height=20,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32,text_color="white")
        self.precio_compra.place(x=250,y=55)
        self.compra_cant = CTkEntry(self.frame_compra_factura2,width=90,height=20,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32,text_color="white")
        self.compra_cant.place(x=410, y=55)
        self.fecha_factura_compra = CTkEntry(self.frame_compra_factura2,width=90,height=20,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32,text_color="white")
        self.fecha_factura_compra.place(x=550,y=55)
        #botones
        btn_guardar_venta=CTkButton(self.frame_compra_factura2,text="Agregar",command=self.agregar_compra,fg_color="green",width=50)
        btn_guardar_venta.place(x=654,y=55)
        btn_confirmar_venta=CTkButton(self.frame_compra_factura2,text="Confirmar",command=self.btn_compra_fac,width=50)
        btn_confirmar_venta.place(x=587,y=200)
        btn_eliminar_venta_producto=CTkButton(self.frame_compra_factura2,text="Eliminar",command=self.eliminar_co_factura,width=30,fg_color="red",text_color="black",hover_color="#7C0A02")
        btn_eliminar_venta_producto.place(x=670,y=120)
        btn_guardar_venta_producto=CTkButton(self.frame_compra_factura3,text="Guardar",command=self.btn_guardar_compra,width=50)
        btn_guardar_venta_producto.place(x=90,y=140)
        btn_imprimir_venta_producto=CTkButton(self.frame_compra_factura3,text="Imprimir",width=50)
        btn_imprimir_venta_producto.place(x=155,y=140)
        
        
        #tabla
        self.grid_factura_compra = ttk.Treeview(self.frame_compra_factura2, columns=("col1","col2","col3","col4","col5","col6"))

        self.grid_factura_compra.column("#0",width=30)            
        self.grid_factura_compra.column("col1",width=50,anchor=CENTER)
        self.grid_factura_compra.column("col2",width=50,anchor=CENTER)
        self.grid_factura_compra.column("col3",width=70,anchor=CENTER)
        self.grid_factura_compra.column("col4",width=50,anchor=CENTER)
        self.grid_factura_compra.column("col5",width=80,anchor=CENTER)
        self.grid_factura_compra.column("col6",width=80,anchor=CENTER)

        self.grid_factura_compra.heading("#0",text="Nombre",anchor=CENTER)
        self.grid_factura_compra.heading("col1",text="Id repuesto",anchor=CENTER)
        self.grid_factura_compra.heading("col2",text="Cantidad",anchor=CENTER)
        self.grid_factura_compra.heading("col3",text="Fecha de compra",anchor=CENTER)
        self.grid_factura_compra.heading("col4",text="Precio compra",anchor=CENTER)
        self.grid_factura_compra.heading("col5",text="Total",anchor=CENTER)
        self.grid_factura_compra.heading("col6",text="Total Bolivares",anchor=CENTER)
        self.grid_factura_compra.place(x=48,y=110,width=750,height=130)
        scrollbar = ttk.Scrollbar(self.frame_compra_factura2, orient="vertical", command=self.grid_factura_compra.yview)
        self.grid_factura_compra.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=808, y=110, height=130)
    def mostrar_ventana_detalle_compra(self):

        self.frame_compra_detalle=CTkFrame(self,width=938,height=480,fg_color="#2a2d2e")
        self.frame_compra_detalle.place(x=150,y=50)
        self.frame_compra_detalle2=CTkFrame(self.frame_compra_detalle,width=685,height=340,fg_color="#2a2d2e", border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frame_compra_detalle2.place(x=170,y=50)
        self.frame_compra_detalle3=CTkFrame(self.frame_compra_detalle,width=150,height=340,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frame_compra_detalle3.place(x=10,y=50)

        #top
        btn_consultar_compra = CTkButton(self.frame_compra_detalle,text="Consultar",command=self.mostra_ventana_compra,fg_color="#2a2d2e", border_color='#FFCC70',border_width=2,corner_radius=32,text_color='white',height=30)
        btn_consultar_compra.place(x=250,y=3)
        btn_insetar_empleado = CTkButton(self.frame_compra_detalle, text="Factura",command=self.mostrar_ventana_fac_compra,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_insetar_empleado.place(x=400,y=3)
        btn_actualizar_empleado = CTkButton(self.frame_compra_detalle, text="Detalle",command=self.mostrar_ventana_detalle_compra,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32, text_color='white',height=30)
        btn_actualizar_empleado.place(x=550,y=3)
        #label
        lbl1=CTkLabel(self.frame_compra_detalle2,text="DETALLE COMPRA",text_color="white",font=("Arial",20))
        lbl1.place(x=230,y=10)
        self.grid_factura_detalle = ttk.Treeview(self.frame_compra_detalle2, columns=("col1","col2","col3","col4","col5","col6","col7","col8"))

        self.grid_factura_detalle.column("#0",width=35)            
        self.grid_factura_detalle.column("col1",width=55,anchor=CENTER)
        self.grid_factura_detalle.column("col2",width=50,anchor=CENTER)
        self.grid_factura_detalle.column("col3",width=70,anchor=CENTER)
        self.grid_factura_detalle.column("col4",width=50,anchor=CENTER)
        self.grid_factura_detalle.column("col5",width=80,anchor=CENTER)
        self.grid_factura_detalle.column("col6",width=80,anchor=CENTER)
        self.grid_factura_detalle.column("col7",width=80,anchor=CENTER)
        self.grid_factura_detalle.column("col8",width=80,anchor=CENTER)

        self.grid_factura_detalle.heading("#0",text="Id detalle",anchor=CENTER)
        self.grid_factura_detalle.heading("col1",text="Id repuesto",anchor=CENTER)
        self.grid_factura_detalle.heading("col2",text="Id compra",anchor=CENTER)
        self.grid_factura_detalle.heading("col3",text="Cantidad",anchor=CENTER)
        self.grid_factura_detalle.heading("col4",text="Fecha",anchor=CENTER)
        self.grid_factura_detalle.heading("col5",text="Precio de compra",anchor=CENTER)
        self.grid_factura_detalle.heading("col6",text="Total",anchor=CENTER)
        self.grid_factura_detalle.heading("col7",text="Total Bolivares",anchor=CENTER)
        self.grid_factura_detalle.heading("col8",text="Nombre Respuesto",anchor=CENTER)
        self.grid_factura_detalle.place(x=50,y=70,width=778,height=300)
        self.llenar_grid_detalle_c()
        scrollbar = ttk.Scrollbar(self.frame_compra_detalle2, orient="vertical", command=self.grid_factura_detalle.yview)
        self.grid_factura_detalle.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=831, y=70, height=300)

        #label
        lbl1=CTkLabel(self.frame_compra_detalle3,text="CONSULTA",text_color="white")
        lbl1.place(x=40,y=8)
        lbl2=CTkLabel(self.frame_compra_detalle3,text="Desde",text_color="white")
        lbl2.place(x=20,y=33)
        lbl3=CTkLabel(self.frame_compra_detalle3,text="Hasta",text_color="white")
        lbl3.place(x=20,y=85)
        #entry
        self.entry_consultac_fecha1d=CTkEntry( self.frame_compra_detalle3,width=90,fg_color="#2a2d2e", border_color='#FFCC70',border_width=2,corner_radius=22,text_color="white")
        self.entry_consultac_fecha1d.place(x=15,y=58)
        self.entry_consultac_fecha2d=CTkEntry( self.frame_compra_detalle3,width=90,fg_color="#2a2d2e", border_color='#FFCC70',border_width=2,corner_radius=22,text_color="white")
        self.entry_consultac_fecha2d.place(x=15,y=108)
        #botones
        btn_confimar_consulta_detalle_c=CTkButton( self.frame_compra_detalle3,text="Confirmar",width=50,command=self.top_level_d_compra,fg_color="green")
        btn_confimar_consulta_detalle_c.place(x=28,y=200)
    #ventanas venta
    def mostrar_ventana_consulta_venta(self):
        self.frame_consulta_venta=CTkFrame(self,width=938,height=480,fg_color="#2a2d2e")
        self.frame_consulta_venta.place(x=150,y=50)
        self.frame_consulta_venta2=CTkFrame(self.frame_consulta_venta,width=685,height=260,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frame_consulta_venta2.place(x=220,y=70)
        #top
        btn_consultar_compra = CTkButton(self.frame_consulta_venta,text="Consultar",command=self.mostrar_ventana_consulta_venta,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_consultar_compra.place(x=250,y=3)
        btn_insetar_empleado = CTkButton(self.frame_consulta_venta, text="Factura",command=self.mostrar_ventana_factura,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)        
        btn_insetar_empleado.place(x=400,y=3)
        btn_actualizar_empleado = CTkButton(self.frame_consulta_venta, text="Detalle",command=self.mostrar_ventana_detalle_factura,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_actualizar_empleado.place(x=550,y=3)
        #inicio
        style = ttk.Style()
   
        style.theme_use("default")
   
        style.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=25,
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
   
        style.configure("Treeview.Heading",
                            background="#565b5e",
                            foreground="white",
                            relief="flat")
        style.map("Treeview.Heading",
                      background=[('active', '#3484F0')])

        #grid
        self.grid_venta = ttk.Treeview(self.frame_consulta_venta2, columns=("col1","col2","col3","col4","col5"),style="Treeview")
        self.grid_venta.column("#0",width=30)            
        self.grid_venta.column("col1",width=50,anchor=CENTER)
        self.grid_venta.column("col2",width=50,anchor=CENTER)
        self.grid_venta.column("col3",width=70,anchor=CENTER)
        self.grid_venta.column("col4",width=50,anchor=CENTER)
        self.grid_venta.column("col5",width=80,anchor=CENTER)  
    
        self.grid_venta.heading("#0",text="Id venta",anchor=CENTER)
        self.grid_venta.heading("col1",text="Id empleado",anchor=CENTER)
        self.grid_venta.heading("col2",text="Fecha venta",anchor=CENTER)
        self.grid_venta.heading("col3",text="Total venta",anchor=CENTER)
        self.grid_venta.heading("col4",text="Total bolivares",anchor=CENTER)
        self.grid_venta.heading("col5",text="Comision",anchor=CENTER)
        self.grid_venta.place(x=10,y=50,width=800,height=250)
        self.fupdateven()
        scrollbar = ttk.Scrollbar(self.frame_consulta_venta2, orient="vertical", command=self.grid_venta.yview)
        self.grid_venta.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=818, y=50, height=250)
       
       
        self.frame_cv= CTkFrame(self.frame_consulta_venta,width=167,height=260,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frame_cv.place(x=20,y=70)
        #label
        lbl=CTkLabel(self.frame_consulta_venta2,text="VENTAS",text_color="white",font=("Arial",15))
        lbl.place(x=300,y=5)
        lbl1=CTkLabel(self.frame_cv,text="CONSULTA VENTAS",text_color="white")
        lbl1.place(x=20,y=5)
        lbl2=CTkLabel(self.frame_cv,text="Desde",text_color="white")
        lbl2.place(x=20,y=25)
        lbl3=CTkLabel(self.frame_cv,text="Hasta",text_color="white")
        lbl3.place(x=20,y=75)
        
        #botones
        btn_confimar_consulta=CTkButton(self.frame_cv,text="Confirmar",width=70,command=self.top_level,fg_color="green")
        btn_confimar_consulta.place(x=20,y=200)
        #entry
        self.entry_consulta_fecha1=CTkEntry(self.frame_cv,width=90,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32,text_color="white")
        self.entry_consulta_fecha1.place(x=15,y=48)
        self.entry_consulta_fecha2=CTkEntry(self.frame_cv,width=90,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32,text_color="white")
        self.entry_consulta_fecha2.place(x=15,y=98)
      
    def mostrar_ventana_detalle_factura(self):
        self.frame_detalle_venta=CTkFrame(self,width=938,height=480,fg_color="#2a2d2e")
        self.frame_detalle_venta.place(x=150,y=50)
        self.frame_cvd= CTkFrame(self.frame_detalle_venta,width=150,height=290,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frame_cvd.place(x=10,y=80)
        self.frame_detalle_venta2=CTkFrame(self.frame_detalle_venta,width=668,height=290,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frame_detalle_venta2.place(x=170,y=80)
         #top
        btn_consultar_detalle_venta= CTkButton(self.frame_detalle_venta,text="Consultar",command=self.mostrar_ventana_consulta_venta,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_consultar_detalle_venta.place(x=250,y=3)
        btn_facturar_compra = CTkButton(self.frame_detalle_venta, text="Factura",command=self.mostrar_ventana_factura,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)       
        btn_facturar_compra.place(x=400,y=3)
        btn_detalle_venta = CTkButton(self.frame_detalle_venta, text="Detalle",command=self.mostrar_ventana_detalle_factura,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_detalle_venta.place(x=550,y=3)
        #labels
        detalle=CTkLabel(self.frame_detalle_venta2,text="DETALLE VENTAS",font=("Arial",15),text_color="white")
        detalle.place(x=220,y=8)

        style = ttk.Style()
   
        style.theme_use("default")
   
        style.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=25,
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
   
        style.configure("Treeview.Heading",
                            background="#565b5e",
                            foreground="white",
                            relief="flat")
        style.map("Treeview.Heading",
                      background=[('active', '#3484F0')])
        

        #inicio
        self.grid_delalle_venta = ttk.Treeview(self.frame_detalle_venta2, columns=("col1","col2","col3","col4","col5","col6","col7"),style="Treeview")

        self.grid_delalle_venta.column("#0",width=30)            
        self.grid_delalle_venta.column("col1",width=50,anchor=CENTER)
        self.grid_delalle_venta.column("col2",width=50,anchor=CENTER)
        self.grid_delalle_venta.column("col3",width=70,anchor=CENTER)
        self.grid_delalle_venta.column("col4",width=50,anchor=CENTER)
        self.grid_delalle_venta.column("col5",width=80,anchor=CENTER)
        self.grid_delalle_venta.column("col6",width=80,anchor=CENTER)
        self.grid_delalle_venta.column("col7",width=80,anchor=CENTER)

        self.grid_delalle_venta.heading("#0",text="Id detalle",anchor=CENTER)
        self.grid_delalle_venta.heading("col1",text="Id venta",anchor=CENTER)          
        self.grid_delalle_venta.heading("col2",text="Total detalle",anchor=CENTER)
        self.grid_delalle_venta.heading("col3",text="Comision",anchor=CENTER)
        self.grid_delalle_venta.heading("col4",text="Total bolivares",anchor=CENTER)
        self.grid_delalle_venta.heading("col5",text="Id repuesto",anchor=CENTER)
        self.grid_delalle_venta.heading("col6",text="Cantidad",anchor=CENTER)
        self.grid_delalle_venta.heading("col7",text="Fecha",anchor=CENTER)
        self.grid_delalle_venta.place(x=10,y=50,width=800,height=270)
        self.llenar_grid_detalle()
        scrollbar = ttk.Scrollbar(self.frame_detalle_venta2, orient="vertical", command=self.grid_delalle_venta.yview)
        self.grid_venta.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=813, y=50, height=270)
        
        #label
        lbl1=CTkLabel(self.frame_cvd,text="CONSULTA",text_color="white")
        lbl1.place(x=40,y=8)
        lbl2=CTkLabel(self.frame_cvd,text="Desde",text_color="white")
        lbl2.place(x=20,y=33)
        lbl3=CTkLabel(self.frame_cvd,text="Hasta",text_color="white")
        lbl3.place(x=20,y=85)
        #entry
        self.entry_consultad_fecha1d=CTkEntry(self.frame_cvd,width=90,fg_color="#2a2d2e", border_color='#FFCC70',border_width=2,corner_radius=22,text_color="white")
        self.entry_consultad_fecha1d.place(x=15,y=58)
        self.entry_consultad_fecha2d=CTkEntry(self.frame_cvd,width=90,fg_color="#2a2d2e", border_color='#FFCC70',border_width=2,corner_radius=22,text_color="white")
        self.entry_consultad_fecha2d.place(x=15,y=108)
        #botones
        btn_confimar_consulta_detalle_v=CTkButton(self.frame_cvd,text="Confirmar",width=50,command=self.top_level_detalle)
        btn_confimar_consulta_detalle_v.place(x=28,y=200)
        #entry
    def mostrar_ventana_factura(self):
        #valores combobox
        self.ids_empleados = self.empleados.id_empelados()
        self.valores_combobox = [str(id) for id in self.ids_empleados]
        self.ids_repuestos = self.repuestos.id_repuesto()
        self.valores_repuesto = [str(id) for id in self.ids_repuestos]
        #Frame
        self.frame_venta_factura=CTkFrame(self,width=938,height=480,fg_color="#2a2d2e")
        self.frame_venta_factura.place(x=150,y=50)
        self.frame_venta_factura2=CTkFrame(self.frame_venta_factura,width=725,height=222,fg_color="#2a2d2e", border_color='#FFCC70',border_width=2,corner_radius=22)
        self.frame_venta_factura2.place(x=70,y=50)
        self.frame_venta_factura3=CTkFrame(self.frame_venta_factura,width=300,height=187,fg_color="#2a2d2e", border_color='#FFCC70',border_width=2,corner_radius=22)
        self.frame_venta_factura3.place(x=70,y=287)
        #top
        btn_consultar_compra = CTkButton(self.frame_venta_factura,text="Consultar",command=self.mostrar_ventana_consulta_venta,fg_color="#2a2d2e", border_color='#FFCC70',border_width=2,corner_radius=32,text_color='white',height=30)
        btn_consultar_compra.place(x=250,y=3)
        btn_insetar_empleado = CTkButton(self.frame_venta_factura, text="Factura",command=self.mostrar_ventana_factura,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_insetar_empleado.place(x=400,y=3)
        btn_actualizar_empleado = CTkButton(self.frame_venta_factura, text="Detalle",command=self.mostrar_ventana_detalle_factura,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32, text_color='white',height=30)
        btn_actualizar_empleado.place(x=550,y=3)
        #label
        lblfactura=CTkLabel(self.frame_venta_factura2,text="Factura Venta",text_color="white",font=("Arial",15))
        lblfactura.place(x=290,y=5)
        lblfactura1=CTkLabel(self.frame_venta_factura2,text="Empleado",text_color="white")
        lblfactura1.place(x=46,y=36)
        lblfactura2=CTkLabel(self.frame_venta_factura2,text="Producto",text_color="white")
        lblfactura2.place(x=185,y=36)
        lblfactura3=CTkLabel(self.frame_venta_factura2,text="Cantidad",text_color="white")
        lblfactura3.place(x=315,y=36)
        lblfactura4=CTkLabel(self.frame_venta_factura2,text="Fecha",text_color="white")
        lblfactura4.place(x=445,y=36)
        lblv0=CTkLabel(self.frame_venta_factura3,text="TOTAL",text_color="white",font=("Arial",20))
        lblv0.place(x=110,y=10)
        lblv1=CTkLabel(self.frame_venta_factura3,text="Total precio:  ",text_color="white")
        lblv1.place(x=10,y=40)
        lblv2=CTkLabel(self.frame_venta_factura3,text="Total bolivares:",text_color="white")
        lblv2.place(x=10,y=60)
        lblv2=CTkLabel(self.frame_venta_factura3,text="comision:",text_color="white")
        lblv2.place(x=10,y=80)
        lblv2=CTkLabel(self.frame_venta_factura3,text="Fecha",text_color="white")
        lblv2.place(x=10,y=100)
        lblv2=CTkLabel(self.frame_venta_factura3,text="Empleado:",text_color="white")
        lblv2.place(x=10,y=120)
        #guardarventa
        
        #combobox
        self.combo_emp = CTkComboBox(self.frame_venta_factura2,values=self.valores_combobox,width=50,height=20,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32)
        self.combo_emp.place(x=112,y=40)
        self.combo_pro = CTkComboBox(self.frame_venta_factura2, values=self.valores_repuesto,width=50,height=20,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32)
        self.combo_pro.place(x=245, y=40)
        #entry
        self.combo_cant = CTkEntry(self.frame_venta_factura2,width=50,height=20,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32)
        self.combo_cant.place(x=377, y=40)
        self.fecha_factura = CTkEntry(self.frame_venta_factura2,width=80,height=20,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32)
        self.fecha_factura.place(x=497,y=40)
        #botones
        btn_guardar_venta=CTkButton(self.frame_venta_factura2,text="Agregar",command=self.agregar_venta,width=50)
        btn_guardar_venta.place(x=650,y=36)
        btn_confirmar_venta=CTkButton(self.frame_venta_factura2,text="Confirmar",command=self.btn_venta_factura,width=50)
        btn_confirmar_venta.place(x=600,y=180)
        btn_eliminar_venta_producto=CTkButton(self.frame_venta_factura2,text="Eliminar",command=self.eliminar_ve_factura,width=30,fg_color="red",text_color="black",hover_color="#7C0A02")
        btn_eliminar_venta_producto.place(x=655,y=80)
        btn_guardar_venta_producto=CTkButton(self.frame_venta_factura3,text="Guardar",command=self.btn_guardar_venta,width=50)
        btn_guardar_venta_producto.place(x=80,y=150)
        btn_imprimir_venta_producto=CTkButton(self.frame_venta_factura3,text="Imprimir",width=50)
        btn_imprimir_venta_producto.place(x=150,y=150)

        style = ttk.Style()
   
        style.theme_use("default")
   
        style.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=25,
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
   
        style.configure("Treeview.Heading",
                            background="#565b5e",
                            foreground="white",
                            relief="flat")
        style.map("Treeview.Heading",
                      background=[('active', '#3484F0')])
        
        
        #tabla
        self.grid_factura = ttk.Treeview(self.frame_venta_factura2, columns=("col1","col2","col3","col4","col5","col6","col7"),style="Treeview")

        self.grid_factura.column("#0",width=30)            
        self.grid_factura.column("col1",width=50,anchor=CENTER)
        self.grid_factura.column("col2",width=50,anchor=CENTER)
        self.grid_factura.column("col3",width=70,anchor=CENTER)
        self.grid_factura.column("col4",width=50,anchor=CENTER)
        self.grid_factura.column("col5",width=80,anchor=CENTER)
        self.grid_factura.column("col6",width=50,anchor=CENTER)
        self.grid_factura.column("col7",width=80,anchor=CENTER)

        self.grid_factura.heading("#0",text="Nombre",anchor=CENTER)
        self.grid_factura.heading("col1",text="Id repuesto",anchor=CENTER)
        self.grid_factura.heading("col2",text="Cantidad",anchor=CENTER)
        self.grid_factura.heading("col3",text="Fecha de venta",anchor=CENTER)
        self.grid_factura.heading("col4",text="Total",anchor=CENTER)
        self.grid_factura.heading("col5",text="Total precio bolivares",anchor=CENTER)
        self.grid_factura.heading("col6",text="Comision",anchor=CENTER)
        self.grid_factura.heading("col7",text="Empleado",anchor=CENTER)
        self.grid_factura.place(x=10,y=90,width=800,height=120)
    #ventanas vehiculos
    def mostrar_ventana_vehiculos(self):
        self.frame_vehiculo=CTkFrame(self,width=938,height=480,fg_color="#2a2d2e")
        self.frame_vehiculo.place(x=150,y=50)
        self.frame_vehiculo1=CTkFrame(self.frame_vehiculo,width=540,height=250,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frame_vehiculo1.place(x=180,y=50)
        self.Frame_vehiculo2=CTkFrame(self.frame_vehiculo,width=150,height=250,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.Frame_vehiculo2.place(x=10,y=50)
        #top
        btn_consultar_vehiculo = CTkButton(self.frame_vehiculo,text="Consultar",fg_color="#2a2d2e", command=self.mostrar_ventana_vehiculos,text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_consultar_vehiculo.place(x=250,y=3)
        btn_insetar_vehiculo = CTkButton(self.frame_vehiculo, text="Insertar",fg_color="#2a2d2e",command=self.ingresar_vehiculo, text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_insetar_vehiculo.place(x=400,y=3)
        btn_actualizar_vehiculo = CTkButton(self.frame_vehiculo, text="Actualizar",fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_actualizar_vehiculo.place(x=560,y=3)

        style = ttk.Style()
   
        style.theme_use("default")
   
        style.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=25,
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
   
        style.configure("Treeview.Heading",
                            background="#565b5e",
                            foreground="white",
                            relief="flat")
        style.map("Treeview.Heading",
                      background=[('active', '#3484F0')])
        self.grid_vehiculo= ttk.Treeview(self.frame_vehiculo1, columns=("col1","col2","col3"), style="Treeview")

        self.grid_vehiculo.column("#0",width=60)            
        self.grid_vehiculo.column("col1",width=50,anchor=CENTER)
        self.grid_vehiculo.column("col2",width=50,anchor=CENTER)
        self.grid_vehiculo.column("col3",width=70,anchor=CENTER)

        self.grid_vehiculo.heading("#0",text="Id vehiculo",anchor=CENTER)
        self.grid_vehiculo.heading("col1",text="Modelo",anchor=CENTER)
        self.grid_vehiculo.heading("col2",text="Vehiculo",anchor=CENTER)
        self.grid_vehiculo.heading("col3",text="Fecha ingreso",anchor=CENTER)
        self.grid_vehiculo.place(x=30,y=30,width=600,height=250)
        self.llenar_grid_vehiculo()
        scrollbar = ttk.Scrollbar(self.frame_vehiculo1, orient="vertical", command=self.grid_vehiculo.yview)
        self.grid_vehiculo.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=632, y=30, height=250)
        btn_eliminarvehi=CTkButton(self.Frame_vehiculo2,text="eliminar",command=self.eli_ve,fg_color="#2a2d2e",text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32)
        btn_eliminarvehi.place(x=5,y=90)
    def ingresar_vehiculo(self):
        self.frame_ingresar_vehiculo=CTkFrame(self,width=938,height=480,fg_color="#2a2d2e")
        self.frame_ingresar_vehiculo.place(x=150,y=50)
        self.Frame_insertar_vehiculo1=CTkFrame(self.frame_ingresar_vehiculo,width=320,height=290,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.Frame_insertar_vehiculo1.place(x=280,y=50)
        btn_consultar_vehiculo1= CTkButton(self.frame_ingresar_vehiculo,text="Consultar",fg_color="#2a2d2e",command=self.mostrar_ventana_vehiculos ,text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_consultar_vehiculo1.place(x=250,y=3)
        btn_insetar_vehiculo1 = CTkButton(self.frame_ingresar_vehiculo, text="Insertar",fg_color="#2a2d2e",command=self.ingresar_vehiculo, text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_insetar_vehiculo1.place(x=400,y=3)
        btn_actualizar_vehiculo1 = CTkButton(self.frame_ingresar_vehiculo, text="Actualizar",fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)

        btn_actualizar_vehiculo1.place(x=560,y=3)
        #entrys
        self.textnombrerev= CTkEntry(self.Frame_insertar_vehiculo1,placeholder_text="Modelo",fg_color="#2a2d2e",text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32)
        self.textnombrerev.place(x=120,y=70)
        self.textreferenciav= CTkEntry(self.Frame_insertar_vehiculo1,placeholder_text="Tipo vehiculo",fg_color="#2a2d2e",text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32)
        self.textreferenciav.place(x=120,y=100)
        self.textopreciorev= CTkEntry(self.Frame_insertar_vehiculo1,placeholder_text="Fecha ingreso",fg_color="#2a2d2e",text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32)
        self.textopreciorev.place(x=120,y=130)
        #label
        lbli=CTkLabel(self.Frame_insertar_vehiculo1,text="ingresar",font=("Arial",25),text_color="white")
        lbli.place(x=100,y=5)
        lbli1=CTkLabel(self.Frame_insertar_vehiculo1,text="Modelo",font=("Arial",15),text_color="white")
        lbli1.place(x=10,y=70)
        lbli2=CTkLabel(self.Frame_insertar_vehiculo1,text="Tipo vehiculo",font=("Arial",15),text_color="white")
        lbli2.place(x=10,y=100)
        lbli3=CTkLabel(self.Frame_insertar_vehiculo1,text="Fecha ingreso",font=("Arial",15),text_color="white")
        lbli3.place(x=10,y=130)
        self.btnguardarv=CTkButton(self.Frame_insertar_vehiculo1,text="Guardar",command=self.guardar_ve,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32,width=50)
        self.btnguardarv.place(x=80,y=230)
        

    #ventanas repuesto
    def mostrar_ventana_repuesto(self):
        self.frame_repuesto=CTkFrame(self,width=938,height=480,fg_color="#2a2d2e")
        self.frame_repuesto.place(x=150,y=50)
        self.frame_repuesto2=CTkFrame(self.frame_repuesto,width=600,height=290,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.frame_repuesto2.place(x=210,y=50)
        self.Frame_repuesto3=CTkFrame(self.frame_repuesto,width=150,height=290,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.Frame_repuesto3.place(x=40,y=50)
        #top
        btn_consultar_vehiculo = CTkButton(self.frame_repuesto,text="Consultar",fg_color="#2a2d2e",command=self.mostrar_ventana_repuesto,text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_consultar_vehiculo.place(x=250,y=3)
        btn_insetar_vehiculo = CTkButton(self.frame_repuesto, text="Insertar",fg_color="#2a2d2e",command=self.mostrar_ventana_insetar_re ,text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_insetar_vehiculo.place(x=400,y=3)
        btn_actualizar_vehiculo = CTkButton(self.frame_repuesto, text="Actualizar",fg_color="#2a2d2e",command=self.mostrar_ventana_up_re, text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_actualizar_vehiculo.place(x=550,y=3)
        
        #label
        lbl=CTkLabel(self.frame_repuesto2,text="REPUESTOS",text_color="white",font=("Arial",20))
        lbl.place(x=230,y=5)
        lbl1=CTkLabel(self.Frame_repuesto3,text="Consulta",text_color="white",font=("Arial",20))
        lbl1.place(x=30,y=5)
        lbl2=CTkLabel(self.Frame_repuesto3,text="Nombre repuesto",text_color="white")
        lbl2.place(x=20,y=30)
        
        #Entry
        self.econsultare=CTkEntry(self.Frame_repuesto3,width=100,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32,text_color="white")
        self.econsultare.place(x=20,y=53)
        #boton
        btn_c_re=CTkButton(self.Frame_repuesto3,text="consultar",fg_color="green",width=50,command=self.consulta_repuesto)
        btn_c_re.place(x=30,y=170)
        style = ttk.Style()

   
        style.theme_use("default")
   
        style.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=25,
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
   
        style.configure("Treeview.Heading",
                            background="#565b5e",
                            foreground="white",
                            relief="flat")
        style.map("Treeview.Heading",
                      background=[('active', '#3484F0')])
        
        self.grid_repuesto= ttk.Treeview(self.frame_repuesto2, columns=("col1","col2","col3","col4","col5","col6","col7"),style="Treeview")
        
        
        self.grid_repuesto.column("#0",width=30)            
        self.grid_repuesto.column("col1",width=50,anchor=CENTER)
        self.grid_repuesto.column("col2",width=50,anchor=CENTER)
        self.grid_repuesto.column("col3",width=70,anchor=CENTER)
        self.grid_repuesto.column("col4",width=50,anchor=CENTER)
        self.grid_repuesto.column("col5",width=80,anchor=CENTER)
        self.grid_repuesto.column("col6",width=50,anchor=CENTER)
        self.grid_repuesto.column("col7",width=50,anchor=CENTER)
        
        self.grid_repuesto.heading("#0",text="Id repuesto",anchor=CENTER)
        self.grid_repuesto.heading("col1",text="Nombre",anchor=CENTER)
        self.grid_repuesto.heading("col2",text="Referencia",anchor=CENTER)
        self.grid_repuesto.heading("col3",text="Precio",anchor=CENTER)
        self.grid_repuesto.heading("col4",text="Cantidad",anchor=CENTER)
        self.grid_repuesto.heading("col5",text="Precio Bolivar",anchor=CENTER)
        self.grid_repuesto.heading("col6",text="Comision",anchor=CENTER)
        self.grid_repuesto.heading("col7",text="vehiculo",anchor=CENTER)
        self.grid_repuesto.place(x=70,y=40,width=600,height=300)

        self.llenar_grid_repuesto()
        scrollbar = ttk.Scrollbar(self.frame_repuesto2, orient="vertical", command=self.grid_repuesto.yview)
        self.grid_repuesto.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=680, y=40, height=300)
    def mostrar_ventana_insetar_re(self):
        
        self.Frame_insertar_re=CTkFrame(self,width=938,height=480,fg_color="#2a2d2e")
        self.Frame_insertar_re.place(x=150,y=50)
        self.Frame_insertar_re2=CTkFrame(self.Frame_insertar_re,width=320,height=290,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.Frame_insertar_re2.place(x=280,y=50)

        #valor combobox
        self.nombre_repuesto = self.vehiculos.nombre_vehiculos()
        self.valores_comboboxre = [str(id) for id in self.nombre_repuesto]
        #BOTONES
        btn_consultar_empleado = CTkButton(self.Frame_insertar_re,text="Consultar",command=self.mostrar_ventana_repuesto,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_consultar_empleado.place(x=250,y=3)
        btn_insetar_empleado = CTkButton(self.Frame_insertar_re, text="Insertar", fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_insetar_empleado.place(x=400,y=3)
        btn_actualizar_empleado = CTkButton(self.Frame_insertar_re, text="Actualizar",command=self.mostrar_ventana_up_re,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_actualizar_empleado.place(x=550,y=3)
        #CONTENIDO
        self.textnombrere= CTkEntry(self.Frame_insertar_re2,placeholder_text="Nombre")
        self.textnombrere.place(x=100,y=70)
        self.textreferencia= CTkEntry(self.Frame_insertar_re2,placeholder_text="Referencia")
        self.textreferencia.place(x=100,y=100)
        self.textopreciore= CTkEntry(self.Frame_insertar_re2,placeholder_text="Precio")
        self.textopreciore.place(x=100,y=130)
        self.textcantidadre= CTkEntry(self.Frame_insertar_re2,placeholder_text="Cantidad")
        self.textcantidadre.place(x=100,y=160)
        self.combo_empre= CTkComboBox(self.Frame_insertar_re2,values=self.valores_comboboxre,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32)
        self.combo_empre.place(x=100,y=190)
       
        self.btnguardar=CTkButton(self.Frame_insertar_re2,text="Guardar",command=self.guardar_repuesto,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32,width=50)
        self.btnguardar.place(x=80,y=230)
        self.btncancelar=CTkButton(self.Frame_insertar_re2,text="Cancelar",border_color='#FFCC70',fg_color="#2a2d2e",border_width=2,corner_radius=32,width=50)
        self.btncancelar.place(x=160,y=230)
        #label
        lbli=CTkLabel(self.Frame_insertar_re2,text="ingresar",font=("Arial",25),text_color="white")
        lbli.place(x=100,y=5)
        lbli1=CTkLabel(self.Frame_insertar_re2,text="Nombre",font=("Arial",15),text_color="white")
        lbli1.place(x=10,y=70)
        lbli2=CTkLabel(self.Frame_insertar_re2,text="Referencia",font=("Arial",15),text_color="white")
        lbli2.place(x=10,y=100)
        lbli3=CTkLabel(self.Frame_insertar_re2,text="Precio",font=("Arial",15),text_color="white")
        lbli3.place(x=10,y=130)
        lbli4=CTkLabel(self.Frame_insertar_re2,text="Cantidad",font=("Arial",15),text_color="white")
        lbli4.place(x=10,y=160)    
        lbli4=CTkLabel(self.Frame_insertar_re2,text="Vehiculo",font=("Arial",15),text_color="white")
        lbli4.place(x=10,y=190)    
    def mostrar_ventana_up_re(self):
        #frame
        self.Frame_up_re=CTkFrame(self,width=938,height=480,fg_color="#2a2d2e")
        self.Frame_up_re.place(x=150,y=50)
        self.Frame_up_re2=CTkFrame(self.Frame_up_re,width=595,height=300,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.Frame_up_re2.place(x=250,y=70)
        self.Frame_up_re3=CTkFrame(self.Frame_up_re,width=180,height=300,fg_color="#2a2d2e",border_color='#FFCC70',border_width=2,corner_radius=32)
        self.Frame_up_re3.place(x=30,y=70)
        #botones
        btn_consultar_empleado = CTkButton(self.Frame_up_re,text="Consultar",command=self.mostrar_ventana_repuesto,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_consultar_empleado.place(x=250,y=3)
        btn_insetar_empleado = CTkButton(self.Frame_up_re, text="Insertar", command=self.mostrar_ventana_insetar_re,fg_color="#2a2d2e", text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_insetar_empleado.place(x=400,y=3)
        btn_actualizar_empleado = CTkButton(self.Frame_up_re, text="Actualizar",command=self.mostrar_ventana_up_re,fg_color="#2a2d2e",text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30)
        btn_actualizar_empleado.place(x=550,y=3)
     
        
        style = ttk.Style()
   
        style.theme_use("default")
   
        style.configure("Treeview",
                            background="#2a2d2e",
                            foreground="white",
                            rowheight=25,
                            fieldbackground="#343638",
                            bordercolor="#343638",
                            borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
   
        style.configure("Treeview.Heading",
                            background="#565b5e",
                            foreground="white",
                            relief="flat")
        style.map("Treeview.Heading",
                      background=[('active', '#3484F0')])
        self.grid_repuesto= ttk.Treeview(self.Frame_up_re2, columns=("col1","col2","col3","col4","col5","col6"), style="Treeview")

        self.grid_repuesto.column("#0",width=30)            
        self.grid_repuesto.column("col1",width=50,anchor=CENTER)
        self.grid_repuesto.column("col2",width=50,anchor=CENTER)
        self.grid_repuesto.column("col3",width=70,anchor=CENTER)
        self.grid_repuesto.column("col4",width=50,anchor=CENTER)
        self.grid_repuesto.column("col5",width=80,anchor=CENTER)
        self.grid_repuesto.column("col6",width=50,anchor=CENTER)
        
    
        self.grid_repuesto.heading("#0",text="Id repuesto",anchor=CENTER)
        self.grid_repuesto.heading("col1",text="Nombre",anchor=CENTER)
        self.grid_repuesto.heading("col2",text="Referencia",anchor=CENTER)
        self.grid_repuesto.heading("col3",text="Precio",anchor=CENTER)
        self.grid_repuesto.heading("col4",text="Cantidad",anchor=CENTER)
        self.grid_repuesto.heading("col5",text="Precio bolivar",anchor=CENTER)
        self.grid_repuesto.heading("col6",text="Comision",anchor=CENTER)
        self.grid_repuesto.place(x=80,y=50,width=600,height=250)
        self.llenar_grid_repuesto()
        scrollbar = ttk.Scrollbar(self.Frame_up_re2, orient="vertical", command=self.grid_repuesto.yview)
        self.grid_repuesto.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(x=687, y=50, height=250)
        self.grid_repuesto['selectmode']='browse'
        btn_act=CTkButton(self.Frame_up_re3,text="actualizar",command= self.act_repuesto,fg_color="#2a2d2e",text_color='white',border_color='#FFCC70',border_width=2,corner_radius=32,height=30,width=50)
        btn_act.place(x=40,y=10)
        #entry
        self.textnombrere= CTkEntry(self.Frame_up_re3,placeholder_text="Nombre")
        self.textnombrere.place(x=10,y=70)
        self.textreferenciare= CTkEntry(self.Frame_up_re3,placeholder_text="Referencia")
        self.textreferenciare.place(x=10,y=100)
        self.preciore= CTkEntry(self.Frame_up_re3,placeholder_text="Precio")
        self.preciore.place(x=10,y=130)
        self.cantidadre= CTkEntry(self.Frame_up_re3,placeholder_text="Cantidad")
        self.cantidadre.place(x=10,y=160)
       
        self.btnguardaract=CTkButton(self.Frame_up_re3,text="Confirmar",command=self.btn_act_re,border_color='#FFCC70',border_width=2,corner_radius=32,width=50)
        self.btnguardaract.place(x=40,y=220)



if __name__=="__main__":
    app = App()
    app.mainloop()