from visitas_app.servicios.visita_servicio import VisitaServicio
from visitas_app.ui.app_tkinter import AppTkinter


def main():
    servicio = VisitaServicio()
    app = AppTkinter(servicio)
    app.run()


if __name__ == "__main__":
    main()