import tkinter as tk
from tkinter import ttk, messagebox


class AppTkinter:
    def __init__(self, servicio):
        self.servicio = servicio  # inyección de dependencias

        self.root = tk.Tk()
        self.root.title("Sistema de Registro de Visitantes")
        self.root.geometry("650x450")

        self.crear_widgets()

    def crear_widgets(self):
        # ===== FORMULARIO =====
        tk.Label(self.root, text="Cédula").grid(row=0, column=0, padx=10, pady=5)
        self.entry_cedula = tk.Entry(self.root)
        self.entry_cedula.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Nombre").grid(row=1, column=0, padx=10, pady=5)
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Motivo").grid(row=2, column=0, padx=10, pady=5)
        self.entry_motivo = tk.Entry(self.root)
        self.entry_motivo.grid(row=2, column=1, padx=10, pady=5)

        # ===== BOTONES =====
        tk.Button(self.root, text="Registrar", width=15, command=self.registrar)\
            .grid(row=3, column=0, padx=10, pady=10)

        tk.Button(self.root, text="Eliminar", width=15, command=self.eliminar)\
            .grid(row=3, column=1, padx=10, pady=10)

        tk.Button(self.root, text="Limpiar", width=15, command=self.limpiar)\
            .grid(row=3, column=2, padx=10, pady=10)

        # ===== TABLA =====
        self.tree = ttk.Treeview(
            self.root,
            columns=("Cedula", "Nombre", "Motivo"),
            show="headings"
        )

        self.tree.heading("Cedula", text="Cédula")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Motivo", text="Motivo")

        self.tree.column("Cedula", width=120)
        self.tree.column("Nombre", width=200)
        self.tree.column("Motivo", width=200)

        self.tree.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Permitir que la tabla se expanda
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def registrar(self):
        cedula = self.entry_cedula.get().strip()
        nombre = self.entry_nombre.get().strip()
        motivo = self.entry_motivo.get().strip()

        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        if self.servicio.registrar(cedula, nombre, motivo):
            messagebox.showinfo("Éxito", "Visitante registrado correctamente")
            self.actualizar_tabla()
            self.limpiar()
        else:
            messagebox.showerror("Error", "La cédula ya existe")

    def eliminar(self):
        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un registro")
            return

        item = seleccionado[0]
        valores = self.tree.item(item, "values")

        if not valores:
            return

        cedula = valores[0]

        if self.servicio.eliminar(cedula):
            messagebox.showinfo("Éxito", "Registro eliminado")
            self.actualizar_tabla()
        else:
            messagebox.showerror("Error", "No se pudo eliminar")

    def actualizar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for v in self.servicio.listar():
            self.tree.insert("", "end", values=(v.cedula, v.nombre, v.motivo))

    def limpiar(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)
        self.entry_cedula.focus()

    def run(self):
        self.root.mainloop()