# Dashboard COVID-19

Un dashboard interactivo desarrollado con Django para visualizar datos relacionados con la pandemia de COVID-19.

## Características

- Visualización de casos totales, muertes y recuperaciones
- Gráficos interactivos con Chart.js
- Interfaz responsiva usando Bootstrap
- Actualización automática de datos

## Requisitos

- Python 3.8 o superior
- Django 5.1
- Otras dependencias listadas en `requirements.txt`

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/covid-dashboard.git
   cd covid-dashboard
   ```

2. Crear y activar el entorno virtual:
   ```bash
   python -m venv .venv
   # En Windows
   .venv\Scripts\activate
   # En Linux/Mac
   source .venv/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configurar las variables de entorno:
   - Crear un archivo `.env` en la raíz del proyecto
   - Agregar las variables necesarias (ver `.env.example`)

5. Realizar las migraciones:
   ```bash
   python manage.py migrate
   ```

## Uso

1. Iniciar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

2. Abrir el navegador y visitar:
   ```
   http://localhost:8000
   ```

## Estructura del Proyecto

```
covid_dashboard/
├── covid_dashboard/     # Configuración principal del proyecto
├── dashboard/          # Aplicación principal
│   ├── management/     # Comandos personalizados
│   ├── migrations/     # Migraciones de la base de datos
│   ├── templates/      # Plantillas HTML
│   ├── models.py       # Modelos de datos
│   ├── views.py        # Lógica de las vistas
│   └── urls.py         # Configuración de URLs
└── manage.py          # Script de administración de Django
```

## Tecnologías Utilizadas

- Django - Framework web
- Chart.js - Biblioteca de gráficos
- Bootstrap - Framework CSS
- SQLite - Base de datos

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Distribuido bajo la Licencia MIT. Ver `LICENSE` para más información.

## Contacto

Tu Nombre - [@tu_twitter](https://twitter.com/tu_usuario)

Enlace del Proyecto: [https://github.com/tu-usuario/covid-dashboard](https://github.com/tu-usuario/covid-dashboard)