🧾 Sistema de Registro de Visitantes

📌 Descripción
Esta es una aplicación de escritorio desarrollada en Python con Tkinter para la gestión de visitantes. El sistema permite registrar, visualizar, actualizar y eliminar datos, asegurando la integridad de la información mediante validaciones de longitud y tipo de dato.

El proyecto sigue una arquitectura modular por capas, separando la definición de datos (Modelos), la lógica de almacenamiento (Servicios) y la visualización (UI).

🏗️ Estructura del Proyecto
Bash
visitas_app/
│
├── main.py                # Punto de entrada
├── modelos/
│   └── visitante.py       # Clase Visitante (Dataclass)
├── servicios/
│   └── visita_servicio.py # Lógica de almacenamiento (Encapsulamiento)
└── ui/
    └── app_tkinter.py     # Interfaz gráfica y validaciones

⚙️ Funcionalidades Implementadas
Gestión CRUD Completa: Registro, actualización y eliminación de visitantes.

Validación de Cédula: Restricción técnica para permitir únicamente 10 dígitos numéricos (bloqueo de teclado al llegar al límite).

Seguridad: Cuadro de diálogo para confirmar la eliminación de registros y evitar borrados accidentales.

Interfaz Optimizada: * El campo Motivo tiene una longitud extendida para descripciones largas.

El botón Limpiar se reubicó estratégicamente junto a los campos de entrada para mayor comodidad.

Los botones de acción principal (Registrar, Actualizar, Eliminar) están alineados en una sola fila.

Limpieza Automática: Los campos de texto se vacían automáticamente después de registrar, actualizar o eliminar un usuario.

🧠 Conceptos de POO Aplicados
Encapsulamiento: Uso de atributos privados (__visitantes) para proteger la integridad de la lista.

Inyección de Dependencias: La interfaz gráfica recibe el servicio de lógica como un parámetro en su constructor.

Manejo de Eventos: Uso de bind para cargar datos de la tabla a los campos de texto con un solo clic.

▶️ Cómo ejecutar el programa
Abre una terminal en la carpeta raíz del proyecto.

Ejecuta el comando:

Bash
python -m visitas_app.main

👨‍💻 Autor
Luis Santiago Flores Piña

🚀 Observaciones
Esta versión incluye mejoras en la Experiencia de Usuario (UX), como el enfoque automático en el campo de cédula tras limpiar y la validación estricta de campos obligatorios antes de procesar cualquier cambio.