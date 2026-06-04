# PLS Pro

Aplicación web fullstack de e-commerce para una tienda de accesorios y productos para mascotas. Desarrollada con Django como proyecto universitario, representa una evolución completa respecto a una versión estática anterior, incorporando autenticación de usuarios, carrito de compras con sesiones, gestión de pedidos, blog con categorías, API REST y panel de administración.

## Demo local

Para correr el proyecto localmente, sigue las instrucciones de instalación más abajo.

---

## Funcionalidades

- **Tienda** — Catálogo de productos con categorías, imágenes y precios, gestionado desde el panel de administración
- **Carrito de compras** — Lógica de sesión para agregar, restar y eliminar productos en tiempo real
- **Pedidos** — Registro y gestión de órdenes de compra con líneas de detalle
- **Autenticación** — Registro e inicio de sesión de usuarios con el sistema nativo de Django
- **Blog** — Posts organizados por categorías
- **Servicios** — Sección de servicios de la tienda (veterinaria, peluquería, farmacia, etc.)
- **Contacto** — Formulario de contacto con envío de correo electrónico via SMTP
- **API REST** — Endpoints con Django REST Framework y consulta de indicadores económicos chilenos en tiempo real (mindicador.cl)
- **Panel de administración** — Gestión completa de productos, clientes, pedidos, blog y servicios

---

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python 3.10 | Lenguaje principal |
| Django 4.0.5 | Framework web |
| SQLite | Base de datos |
| Django REST Framework | API REST |
| Django Crispy Forms | Formularios con Bootstrap |
| Pillow | Manejo de imágenes |
| Bootstrap 5 | Layout responsivo |
| jQuery | Interactividad en el frontend |
| API REST (mindicador.cl) | Indicadores económicos en tiempo real |

---

## Estructura del proyecto

```
ProyectoWeb/
├── ProyectoWeb/        # Configuración principal (settings, urls, wsgi)
├── ProyectoWebApp/     # App principal (index, galería)
├── autenticacion/      # Registro, login y logout
├── tienda/             # Productos, categorías y clientes
├── carro/              # Carrito de compras con sesiones
├── pedidos/            # Gestión de pedidos
├── blog/               # Posts y categorías del blog
├── servicios/          # Servicios de la tienda
├── contacto/           # Formulario de contacto
├── media/              # Archivos subidos (imágenes)
├── db.sqlite3          # Base de datos
└── manage.py
```

---

## Instalación y ejecución local

### Requisitos

- Python 3.10

### Pasos

1. Clona el repositorio:
   ```bash
   git clone https://github.com/alysph/Examen_WEB_003.git
   cd Examen_WEB_003/WEB/ProyectoWeb
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   pip install crispy-bootstrap4
   ```

3. Agrega `'crispy_bootstrap4'` a `INSTALLED_APPS` en `ProyectoWeb/settings.py` y asegúrate de que `DATABASES` use SQLite:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

4. Aplica las migraciones:
   ```bash
   python manage.py migrate
   ```

5. Crea un superusuario para el panel de administración:
   ```bash
   python manage.py createsuperuser
   ```

6. Levanta el servidor:
   ```bash
   python manage.py runserver
   ```

7. Abre el navegador en **http://127.0.0.1:8000/**

---

## Autora

**Alison Urrea** — [GitHub](https://github.com/alysph)

---

## Licencia

Proyecto académico — Duoc UC, 2022.
