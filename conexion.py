from empleado import empleado

 def mostrar_ventana_empleado(self):
        global Frame2, Frame4 # Acceder a la variable global Frame2
        Frame2 = Frame(self)
        Frame2.place(x=95,y=0)
        btn_consultar_compra = Button(Frame2, text="consultar",)
        btn_consultar_compra.grid(row=0, column=7,padx=15,pady=10)
        btn_insetar_empleado = ttk.Button(Frame2, text="insertar")
        btn_insetar_empleado.grid(row=10, column=7,padx=15,pady=10)
        btn_actualizar_empleado = ttk.Button(Frame2, text="actualizar")
        btn_actualizar_empleado.grid(row=20, column=7,padx=15,pady=10)
        btn_eliminar_empleado = Button(Frame2, text="eliminar")
        btn_eliminar_empleado.grid(row=30, column=7,padx=15,pady=10)
        Frame4 = Frame(self)
        Frame4.place(x=200,y=0)

        lbl1=Label(Frame4, text="nombre:  ")
        lbl1.place(x=3,y=5)
        self.textnombre= Entry(Frame4)
        self.textnombre.place(x=90,y=5)

        lbl2=Label(Frame4, text="apellido:   "  )
        lbl2.place(x=3,y=30)
        self.textapellido= Entry(Frame4)
        self.textapellido.place(x=70,y=30)

        lbl3=Label(Frame4, text="fecha de nacimiento:  ")
        lbl3.place(x=3,y=60)
        self.textfdn= Entry(Frame4)
        self.textfdn.place(x=70,y=60)

        lbl4=Label(Frame4, text="telefono:  ")
        lbl4.place(x=3,y=90)
        self.texttlf= Entry(Frame4)
        self.texttlf.place(x=70,y=90)

        lbl5=Label(Frame4, text="correo:  ")
        lbl5.place(x=3,y=120)
        self.textcorreo= Entry(Frame4)
        self.textcorreo.place(x=70,y=120)

        lbl6=Label(Frame4, text="cargo:  ")
        lbl6.place(x=3,y=150)
        self.textcargo= Entry(Frame4)
        self.textcargo.place(x=70,y=150)

        lbl7=Label(Frame4, text="fecha de contratacion:  ")
        lbl7.place(x=3,y=180)
        self.textfdc= Entry(Frame4)
        self.textfdc.place(x=70,y=180)

        self.btnguardar=Button(Frame4,text="guardar")
        self.btnguardar.place(x=8,y=210)

        self.btncancelar=Button(Frame4,text="cancelar")
        self.btncancelar.place(x=70,y=210)

        self.grid = ttk.Treeview(self, columns=("col1","col2","col3","col4","col5","col6"))

        self.grid.column("#0",width=30)
        self.grid.column("col1",width=40,anchor=CENTER)
        self.grid.column("col2",width=40,anchor=CENTER)
        self.grid.column("col3",width=90,anchor=CENTER)
        self.grid.column("col4",width=40,anchor=CENTER)
        self.grid.column("col5",width=40,anchor=CENTER)
        self.grid.column("col6",width=40,anchor=CENTER)

        self.grid.heading("#0",text="Id",anchor=CENTER)
        self.grid.heading("col1",text="Nombre",anchor=CENTER)
        self.grid.heading("col2",text="Apellido",anchor=CENTER)
        self.grid.heading("col3",text="fecha de nacimiento",anchor=CENTER)
        self.grid.heading("col4",text="telefono",anchor=CENTER)
        self.grid.heading("col5",text="correo",anchor=CENTER)
        self.grid.heading("col6",text="cargo",anchor=CENTER)
        self.grid.heading("0",text="fecha de contratacion",anchor=CENTER)
        
        self.grid.place(x=388,y=0,width=680,height=259)
def mostrar_ventana_compra(self):
        global Frame2, Frame3, Frame4
        self.borrar_contenido_frame4()
        if Frame2:
            Frame2.destroy()  # Eliminar cualquier contenido presente en Frame2
        Frame2 = Frame(self, bg="grey")
        Frame2.pack(side="right",fill="both", expand=True)
        btn_inventa = Button(Frame2, text="compra")
        btn_inventa.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.2)
        if Frame3:
            Frame3.destroy()
        Frame3 = Frame(Frame2, bg="black")  # Crear el nuevo Frame dentro de Frame2
        Frame3.pack(side="right",fill="both", expand=True)
        btn_insetar_compra = ttk.Button(Frame3, text="insetar", style='Pro.TButton')
        btn_insetar_compra.grid(row=0, column=7,padx=15,pady=1)
    

    def mostrar_ventana_venta(self):
        global Frame2  # Acceder a la variable global Frame2
        if Frame2:
            Frame2.destroy()  # Eliminar cualquier contenido presente en Frame2
        Frame2 = Frame(self, bg="grey")
        Frame2.pack(side="right", expand=True, fill="both")
        btn_venta = Button(Frame2, text="venta")
        btn_venta.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.2)
        

    def mostrar_ventana_repuesto(self):
        global Frame2  # Acceder a la variable global Frame2
        if Frame2:
            Frame2.destroy()  # Eliminar cualquier contenido presente en Frame2
        Frame2 = Frame(self, bg="grey")
        Frame2.pack(side="right", expand=True, fill="both")
        btn_empleado = Button(Frame2, text="repuesto")
        btn_empleado.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.2)

    def mostrar_ventana_inventario(self):
        global Frame2  # Acceder a la variable global Frame2
        if Frame2:
            Frame2.destroy()  # Eliminar cualquier contenido presente en Frame2
        Frame2 = Frame(self, bg="grey")

        Frame2.pack(side="right", expand=True, fill="both")
        btn_empleado = Button(Frame2, text="inventario")
        btn_empleado.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.2)


    def mostrar_ventana_vehiculos(self):
        global Frame2  # Acceder a la variable global Frame2
        if Frame2:
            Frame2.destroy()  # Eliminar cualquier contenido presente en Frame2
        Frame2 = Frame(self, bg="grey")
        Frame2.pack(side="right", expand=True, fill="both")
        btn_empleado = Button(Frame2, text="vehiculos")
        btn_empleado.place(relx=0.1, rely=0.7, relwidth=0.3, relheight=0.2)

    s = ttk.Style()
    s.configure("Pro.TButton", background="#0000FF")
    s.map("Pro.TButton",foreground=[("active", "#FFA500")])






