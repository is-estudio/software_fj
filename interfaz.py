import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from cliente import Cliente
from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reserva import Reserva
from logger import Logger


class App:

    def __init__(self, root):

        self.root = root
        self.root.title("SOFTWARE FJ")
        self.root.geometry("1100x650")
        self.root.config(bg="#ECF0F1")

        # =====================================
        # LISTAS INTERNAS
        # =====================================

        self.clientes = []
        self.servicios = []
        self.reservas = []

        # =====================================
        # TITULO
        # =====================================

        titulo = tk.Label(
            root,
            text="SOFTWARE FJ - SISTEMA DE GESTIÓN",
            font=("Arial", 22, "bold"),
            bg="#154360",
            fg="white",
            pady=15
        )

        titulo.pack(fill="x")

        # =====================================
        # PANEL PRINCIPAL
        # =====================================

        principal = tk.Frame(root)
        principal.pack(fill="both", expand=True)

        # =====================================
        # MENU LATERAL
        # =====================================

        menu = tk.Frame(
            principal,
            bg="#2C3E50",
            width=250
        )

        menu.pack(side="left", fill="y")

        tk.Button(
            menu,
            text="CLIENTES",
            width=20,
            height=2,
            bg="#3498DB",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.menu_clientes
        ).pack(pady=15)

        tk.Button(
            menu,
            text="SERVICIOS",
            width=20,
            height=2,
            bg="#2ECC71",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.menu_servicios
        ).pack(pady=15)

        tk.Button(
            menu,
            text="RESERVAS",
            width=20,
            height=2,
            bg="#E67E22",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.menu_reservas
        ).pack(pady=15)

        tk.Button(
            menu,
            text="ERRORES Y LOGS",
            width=20,
            height=2,
            bg="#C0392B",
            fg="white",
            font=("Arial", 11, "bold"),
            command=self.menu_logs
        ).pack(pady=15)

        # =====================================
        # CONTENIDO
        # =====================================

        self.contenido = tk.Frame(
            principal,
            bg="white"
        )

        self.contenido.pack(
            side="right",
            fill="both",
            expand=True
        )

        # =====================================
        # LOGS VISUALES
        # =====================================

        self.logs = tk.Listbox(
            root,
            height=8,
            font=("Consolas", 10)
        )

        self.logs.pack(fill="x")

        # =====================================
        # INICIO
        # =====================================

        self.menu_clientes()

    # =====================================
    # LIMPIAR CONTENIDO
    # =====================================

    def limpiar(self):

        for widget in self.contenido.winfo_children():
            widget.destroy()

    # =====================================
    # CLIENTES
    # =====================================

    def menu_clientes(self):

        self.limpiar()

        tk.Label(
            self.contenido,
            text="GESTIÓN DE CLIENTES",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=10)

        self.entry_nombre = tk.Entry(
            self.contenido,
            width=40
        )

        self.entry_nombre.pack(pady=5)
        self.entry_nombre.insert(0, "Nombre")

        self.entry_correo = tk.Entry(
            self.contenido,
            width=40
        )

        self.entry_correo.pack(pady=5)
        self.entry_correo.insert(0, "Correo")

        self.entry_telefono = tk.Entry(
            self.contenido,
            width=40
        )

        self.entry_telefono.pack(pady=5)
        self.entry_telefono.insert(0, "Telefono")

        tk.Button(
            self.contenido,
            text="Registrar Cliente",
            bg="#3498DB",
            fg="white",
            width=25,
            command=self.registrar_cliente
        ).pack(pady=10)

        # =====================================
        # TABLA CLIENTES
        # =====================================

        self.tabla_clientes = ttk.Treeview(
            self.contenido,
            columns=(
                "nombre",
                "correo",
                "telefono"
            ),
            show="headings",
            height=12
        )

        self.tabla_clientes.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla_clientes.heading(
            "correo",
            text="Correo"
        )

        self.tabla_clientes.heading(
            "telefono",
            text="Telefono"
        )

        self.tabla_clientes.column(
            "nombre",
            width=180
        )

        self.tabla_clientes.column(
            "correo",
            width=250
        )

        self.tabla_clientes.column(
            "telefono",
            width=150
        )

        self.tabla_clientes.pack(
            fill="both",
            expand=True,
            pady=10
        )

        self.actualizar_tabla_clientes()

    # =====================================
    # REGISTRAR CLIENTE
    # =====================================

    def registrar_cliente(self):

        try:

            cliente = Cliente(
                self.entry_nombre.get(),
                self.entry_correo.get(),
                self.entry_telefono.get()
            )

            self.clientes.append(cliente)

            self.actualizar_tabla_clientes()

            mensaje = (
                f"Cliente registrado: "
                f"{cliente.nombre}"
            )

            self.logs.insert(
                tk.END,
                mensaje
            )

            Logger.registrar(mensaje)

            messagebox.showinfo(
                "Éxito",
                "Cliente registrado correctamente"
            )

        except Exception as e:

            Logger.registrar(str(e))

            messagebox.showerror(
                "Error Cliente",
                str(e)
            )

    # =====================================
    # ACTUALIZAR CLIENTES
    # =====================================

    def actualizar_tabla_clientes(self):

        if not hasattr(self, "tabla_clientes"):
            return

        for item in self.tabla_clientes.get_children():
            self.tabla_clientes.delete(item)

        for cliente in self.clientes:

            self.tabla_clientes.insert(
                "",
                tk.END,
                values=(
                    cliente.nombre,
                    cliente.correo,
                    cliente.telefono
                )
            )

    # =====================================
    # SERVICIOS
    # =====================================

    def menu_servicios(self):

        self.limpiar()

        tk.Label(
            self.contenido,
            text="GESTIÓN DE SERVICIOS",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=10)

        tk.Button(
            self.contenido,
            text="Crear Sala VIP",
            bg="#2ECC71",
            fg="white",
            width=25,
            command=self.crear_sala
        ).pack(pady=5)

        tk.Button(
            self.contenido,
            text="Crear Alquiler Equipo",
            bg="#27AE60",
            fg="white",
            width=25,
            command=self.crear_equipo
        ).pack(pady=5)

        tk.Button(
            self.contenido,
            text="Crear Asesoría",
            bg="#1E8449",
            fg="white",
            width=25,
            command=self.crear_asesoria
        ).pack(pady=5)

        # =====================================
        # TABLA SERVICIOS
        # =====================================

        self.tabla_servicios = ttk.Treeview(
            self.contenido,
            columns=(
                "nombre",
                "descripcion",
                "tarifa"
            ),
            show="headings",
            height=12
        )

        self.tabla_servicios.heading(
            "nombre",
            text="Servicio"
        )

        self.tabla_servicios.heading(
            "descripcion",
            text="Descripción"
        )

        self.tabla_servicios.heading(
            "tarifa",
            text="Tarifa"
        )

        self.tabla_servicios.pack(
            fill="both",
            expand=True,
            pady=10
        )

        self.actualizar_tabla_servicios()

    # =====================================
    # CREAR SERVICIOS
    # =====================================

    def crear_sala(self):

        sala = ReservaSala(
            "Sala VIP",
            100
        )

        self.servicios.append(sala)

        self.actualizar_tabla_servicios()

    def crear_equipo(self):

        equipo = AlquilerEquipo(
            "Laptop Gamer",
            80
        )

        self.servicios.append(equipo)

        self.actualizar_tabla_servicios()

    def crear_asesoria(self):

        asesoria = AsesoriaEspecializada(
            "Python Avanzado",
            120
        )

        self.servicios.append(asesoria)

        self.actualizar_tabla_servicios()

    # =====================================
    # ACTUALIZAR SERVICIOS
    # =====================================

    def actualizar_tabla_servicios(self):

        if not hasattr(self, "tabla_servicios"):
            return

        for item in self.tabla_servicios.get_children():
            self.tabla_servicios.delete(item)

        for servicio in self.servicios:

            self.tabla_servicios.insert(
                "",
                tk.END,
                values=(
                    servicio.nombre,
                    servicio.descripcion(),
                    servicio.tarifa
                )
            )

    # =====================================
    # RESERVAS
    # =====================================

    def menu_reservas(self):

        self.limpiar()

        tk.Label(
            self.contenido,
            text="GESTIÓN DE RESERVAS",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=10)

        tk.Button(
            self.contenido,
            text="Procesar Reserva",
            bg="#E67E22",
            fg="white",
            width=25,
            command=self.crear_reserva
        ).pack(pady=10)

    def menu_logs(self):

        self.limpiar()

        tk.Label(
            self.contenido,
            text="REGISTRO DE ERRORES Y EVENTOS",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=10)

        # ======================================
        # AREA DE TEXTO
        # ======================================

        frame_logs = tk.Frame(self.contenido)

        frame_logs.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        scrollbar = tk.Scrollbar(frame_logs)

        scrollbar.pack(side="right", fill="y")

        self.text_logs = tk.Text(
            frame_logs,
            font=("Consolas", 10),
            yscrollcommand=scrollbar.set,
            wrap="word"
        )

        self.text_logs.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.config(
            command=self.text_logs.yview
        )

        # ======================================
        # CARGAR ARCHIVO LOGS
        # ======================================

        try:

            with open(
                "logs.txt",
                "r",
                encoding="utf-8"
            ) as archivo:

                contenido = archivo.read()

                self.text_logs.insert(
                    tk.END,
                    contenido
                )

        except FileNotFoundError:

            self.text_logs.insert(
                tk.END,
                "No existen logs registrados."
            )

        # =====================================
        # TABLA RESERVAS
        # =====================================

        self.tabla_reservas = ttk.Treeview(
            self.contenido,
            columns=(
                "cliente",
                "servicio",
                "estado",
                "costo"
            ),
            show="headings",
            height=12
        )

        self.tabla_reservas.heading(
            "cliente",
            text="Cliente"
        )

        self.tabla_reservas.heading(
            "servicio",
            text="Servicio"
        )

        self.tabla_reservas.heading(
            "estado",
            text="Estado"
        )

        self.tabla_reservas.heading(
            "costo",
            text="Costo"
        )

        self.tabla_reservas.pack(
            fill="both",
            expand=True,
            pady=10
        )

        self.actualizar_tabla_reservas()

    # =====================================
    # CREAR RESERVA
    # =====================================

    def crear_reserva(self):

        try:

            if not self.clientes:
                raise Exception(
                    "Debe registrar clientes"
                )

            if not self.servicios:
                raise Exception(
                    "Debe crear servicios"
                )

            cliente = self.clientes[0]
            servicio = self.servicios[0]

            reserva = Reserva(
                cliente,
                servicio,
                3
            )

            costo = reserva.procesar()

            self.reservas.append(reserva)

            self.actualizar_tabla_reservas()

            mensaje = (
                f"Reserva creada: "
                f"{cliente.nombre}"
            )

            self.logs.insert(
                tk.END,
                mensaje
            )

            Logger.registrar(mensaje)

            messagebox.showinfo(
                "Reserva",
                "Reserva procesada correctamente"
            )

        except Exception as e:

            Logger.registrar(str(e))

            messagebox.showerror(
                "Error Reserva",
                str(e)
            )

    # =====================================
    # ACTUALIZAR RESERVAS
    # =====================================

    def actualizar_tabla_reservas(self):

        if not hasattr(self, "tabla_reservas"):
            return

        for item in self.tabla_reservas.get_children():
            self.tabla_reservas.delete(item)

        for reserva in self.reservas:

            costo = reserva.servicio.calcular_costo(
                reserva.horas
            )

            self.tabla_reservas.insert(
                "",
                tk.END,
                values=(
                    reserva.cliente.nombre,
                    reserva.servicio.nombre,
                    reserva.estado,
                    costo
                )
            )