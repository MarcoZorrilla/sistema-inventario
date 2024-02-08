from tkinter import *
from customtkinter import *

CTk._set_appearance_mode('system')
CTk._set_defaul_color_theme("blue")


class Ventana(CTk):
    def __init__(self):
        super().__init__()
        self.create_widgets()
        self.config_pan()
        

    def config_pan(self):
        self.title("sistema crud")
        self.geometry("700x500")

    
    def create_widgets(self):
        Frame1 = CTkFrame(self, width=150, height=400)
        Frame1.place(x=0, y=0)
        self.btn_compra = CTkButton(Frame1, text="compra")
        self.btn_compra.place(x=5, y=10)
        self.btn_venta = CTkButton(Frame1, text="venta")
        self.btn_venta.place(x=5, y=40)
        self.btn_empleado = CTkButton(Frame1, text="empleado", command=self.mostrar_ventana_empleado)
        self.btn_empleado.place(x=5, y=70)
        self.btn_repuesto = CTkButton(Frame1, text="repuesto")
        self.btn_repuesto.place(x=5, y=100)
        self.btn_inventario = CTkButton(Frame1, text="inventario")
        self.btn_inventario.place(x=5, y=130)
        self.btn_vehiculos = CTkButton(Frame1, text="vehiculos")
        self.btn_vehiculos.place(x=5, y=160)

    def mostrar_ventana_empleado(self):
        global Frame2, Frame4 # Acceder a la variable global Frame2
        Frame2 = CTkFrame(self)
        Frame2.place(x=95,y=0)
        btn_consultar_compra = CTkButton(Frame2, text="consultar",)
        btn_consultar_compra.grid(row=0, column=7,padx=15,pady=10)
        btn_insetar_empleado = CTkButton(Frame2, text="insertar")
        btn_insetar_empleado.grid(row=10, column=7,padx=15,pady=10)
        btn_actualizar_empleado = CTkButton(Frame2, text="actualizar")
        btn_actualizar_empleado.grid(row=20, column=7,padx=15,pady=10)
        btn_eliminar_empleado = CTkButton(Frame2, text="eliminar")
        btn_eliminar_empleado.grid(row=30, column=7,padx=15,pady=10)
        Frame4 = CTkFrame(self)
        Frame4.place(x=200,y=0)

        lbl1=CTk.Label(Frame4, text="nombre:  ")
        lbl1.place(x=3,y=5)
        self.textnombre= CTkEntry(Frame4)
        self.textnombre.place(x=90,y=5)

        lbl2=CTkLabel(Frame4, text="apellido:   "  )
        lbl2.place(x=3,y=30)
        self.textapellido= CTkEntry(Frame4)
        self.textapellido.place(x=70,y=30)

        lbl3=CTkLabel(Frame4, text="fecha de nacimiento:  ")
        lbl3.place(x=3,y=60)
        self.textfdn= CTkEntry(Frame4)
        self.textfdn.place(x=70,y=60)

        lbl4=CTkLabel(Frame4, text="telefono:  ")
        lbl4.place(x=3,y=90)
        self.texttlf= CTkEntry(Frame4)
        self.texttlf.place(x=70,y=90)

        lbl5=CTkLabel(Frame4, text="correo:  ")
        lbl5.place(x=3,y=120)
        self.textcorreo=CTkEntry(Frame4)
        self.textcorreo.place(x=70,y=120)

        lbl6=CTkLabel(Frame4, text="cargo:  ")
        lbl6.place(x=3,y=150)
        self.textcargo=CTkEntry(Frame4)
        self.textcargo.place(x=70,y=150)

        lbl7=CTkLabel(Frame4, text="fecha de contratacion:  ")
        lbl7.place(x=3,y=180)
        self.textfdc=CTkEntry(Frame4)
        self.textfdc.place(x=70,y=180)

        self.btnguardar=CTkButton(Frame4,text="guardar")
        self.btnguardar.place(x=8,y=210)

        self.btncancelar=CTkButton(Frame4,text="cancelar")
        self.btncancelar.place(x=70,y=210)


if __name__=="main":
    vent = Ventana()
    vent.mainloop()





 


        

        
    
   
        
    



        





