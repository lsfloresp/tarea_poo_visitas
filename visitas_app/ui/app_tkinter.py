import tkinter as tk
from tkinter import ttk, messagebox


class AppTkinter:
    def __init__(self, servicio):
        self.servicio = servicio

        self.root = tk.Tk()
        self.root.title("Sistema de Registro de Visitantes")
        self.root.geometry("650x450")
        self.root.configure(bg="#a9cce3")

        self.crear_widgets()

    def validar_cedula(self, valor):
        if valor == "":
            return True
        return valor.isdigit() and len(valor) <= 10

    def crear_widgets(self):
        # ===== ESTILO =====
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview",
                        background="#ecf0f1",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#ecf0f1")

        style.map("Treeview",
                  background=[("selected", "#a9cce3")])

        # ===== FORMULARIO =====
        # Cédula
        tk.Label(self.root, text="Cédula", bg="#a9cce3").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        vcmd = (self.root.register(self.validar_cedula), "%P")
        self.entry_cedula = tk.Entry(self.root, validate="key", validatecommand=vcmd)
        self.entry_cedula.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Nombre
        tk.Label(self.root, text="Nombre", bg="#a9cce3").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # --- BOTÓN LIMPIAR  ---
        # Lo ponemos en la fila 0 y que abarque 2 filas para que esté centrado respecto a los dos campos de arriba
        tk.Button(self.root, text="Limpiar Campos", width=15, bg="#2980b9", fg="white",
                  command=self.limpiar).grid(row=0, column=2, rowspan=2, padx=20, pady=5)

        # Motivo
        tk.Label(self.root, text="Motivo", bg="#a9cce3").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        # Aumentamos el width a 50 para que sea mucho más largo
        self.entry_motivo = tk.Entry(self.root, width=54)
        self.entry_motivo.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="w")

        # ===== CONTENEDOR DE BOTONES =====
        frame_botones = tk.Frame(self.root, bg="#a9cce3")
        frame_botones.grid(row=3, column=0, columnspan=4, pady=15)

        tk.Button(frame_botones, text="Registrar", width=15, bg="#27ae60", fg="white",
                  command=self.registrar).grid(row=0, column=0, padx=10)

        tk.Button(frame_botones, text="Actualizar", width=15, bg="#f39c12", fg="white",
                  command=self.actualizar).grid(row=0, column=1, padx=10)

        tk.Button(frame_botones, text="Eliminar", width=15, bg="#c0392b", fg="white",
                  command=self.eliminar).grid(row=0, column=2, padx=10)

        # ===== TABLA =====
        self.tree = ttk.Treeview(self.root, columns=("Cedula", "Nombre", "Motivo"), show="headings")
        self.tree.heading("Cedula", text="Cédula")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Motivo", text="Motivo")
        self.tree.column("Cedula", width=120)
        self.tree.column("Nombre", width=150)
        self.tree.column("Motivo", width=300)  # Más espacio para el motivo en la tabla también
        self.tree.grid(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        self.tree.bind("<<TreeviewSelect>>", self.cargar_datos)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.actualizar_tabla()

    # ================= FUNCIONES =================

    def registrar(self):
        cedula = self.entry_cedula.get().strip()
        nombre = self.entry_nombre.get().strip()
        motivo = self.entry_motivo.get().strip()

        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        if len(cedula) != 10:
            messagebox.showerror("Error de Cédula", "La cédula debe tener exactamente 10 dígitos")
            return

        if self.servicio.registrar(cedula, nombre, motivo):
            messagebox.showinfo("Éxito", "Visitante registrado correctamente")
            self.actualizar_tabla()
            self.limpiar()
        else:
            messagebox.showerror("Error", "La cédula ya existe")

    def actualizar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for v in self.servicio.listar():
            self.tree.insert("", "end", values=(v.cedula, v.nombre, v.motivo))

    def cargar_datos(self, event):
        seleccionado = self.tree.selection()

        if not seleccionado:
            return

        valores = self.tree.item(seleccionado[0], "values")

        self.limpiar()

        self.entry_cedula.insert(0, valores[0])
        self.entry_nombre.insert(0, valores[1])
        self.entry_motivo.insert(0, valores[2])

    def eliminar(self):
        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un registro")
            return

        cedula = self.tree.item(seleccionado[0], "values")[0]

        # Preguntar antes de proceder
        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este registro?")

        if confirmar:  # Si el usuario presiona "Sí"
            if self.servicio.eliminar(cedula):
                messagebox.showinfo("Éxito", "Registro eliminado")
                self.actualizar_tabla()
                self.limpiar()
            else:
                messagebox.showerror("Error", "No se pudo eliminar")

    def actualizar(self):
        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un registro para actualizar")
            return

        cedula_original = self.tree.item(seleccionado[0], "values")[0]

        nueva_cedula = self.entry_cedula.get().strip()
        nuevo_nombre = self.entry_nombre.get().strip()
        nuevo_motivo = self.entry_motivo.get().strip()

        if not nueva_cedula or not nuevo_nombre or not nuevo_motivo:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        # Validación Exactamente 10 dígitos
        if len(nueva_cedula) != 10:
            messagebox.showerror("Error de Cédula", "La cédula debe tener exactamente 10 dígitos")
            return

        # Borrar y registrar
        self.servicio.eliminar(cedula_original)
        self.servicio.registrar(nueva_cedula, nuevo_nombre, nuevo_motivo)

        messagebox.showinfo("Éxito", "Registro actualizado")
        self.actualizar_tabla()
        self.limpiar()

    def limpiar(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)
        self.entry_cedula.focus()

    def run(self):
        self.root.mainloop()