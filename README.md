# 🧾 Sistema de Registro de Visitantes

## 📌 Descripción

Este proyecto consiste en una aplicación de escritorio desarrollada en Python utilizando Tkinter.
El objetivo es gestionar el registro de visitantes en una oficina, permitiendo ingresar, visualizar y eliminar registros de manera sencilla.

El sistema fue desarrollado aplicando una arquitectura modular por capas, separando la lógica del programa, los datos y la interfaz gráfica.

---

## 🏗️ Estructura del Proyecto

```bash
visitas_app/
│
├── main.py
├── modelos/
│   └── visitante.py
├── servicios/
│   └── visita_servicio.py
└── ui/
    └── app_tkinter.py
```

---

## ⚙️ Funcionalidades

* Registro de visitantes mediante formulario
* Visualización de datos en una tabla
* Eliminación de registros seleccionados
* Limpieza automática de campos
* Validación para que la cédula solo acepte números

---

## 🧠 Tecnologías utilizadas

* Python 3
* Tkinter
* ttk (Treeview)

---

## ▶️ Cómo ejecutar el programa

1. Abrir la terminal en la carpeta del proyecto

2. Ejecutar el siguiente comando:

```bash
python -m visitas_app.main
```

---

## 🎯 Aspectos técnicos aplicados

En este proyecto se aplicaron los siguientes conceptos:

* Programación Orientada a Objetos (POO)
* Encapsulamiento
* Inyección de dependencias
* Arquitectura por capas (modelo, servicio, interfaz)

---

## 👨‍💻 Autor

Luis Santiago Flores Piña

---

## 🚀 Observaciones

Este sistema puede mejorarse agregando nuevas funcionalidades como edición de registros, validaciones más avanzadas o mejoras en la interfaz gráfica.
