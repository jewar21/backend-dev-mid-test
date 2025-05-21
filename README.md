# Backend Dev Mid Test

Este repositorio contiene la solución a la prueba técnica para **Backend Developer Mid** de **Jikkosoft**.

---

## ✍️ Descripción General

La prueba se divide en tres ejercicios principales:

1. **Diseño de una base de datos para una plataforma de blogs**
2. **Implementación de una función para encontrar dos números que sumen un objetivo**
3. **Desarrollo de un sistema de gestión de biblioteca con programación orientada a objetos**

---

## ⚙️ Configuración del Proyecto

### Requisitos

- Python 3.8 o superior
- Git Bash / Terminal compatible con `bash`
- Acceso a internet para instalar dependencias

### Instrucciones de uso

```bash
# Clonar el repositorio
git clone https://github.com/jewar21/backend-dev-mid-test.git
cd backend-dev-mid-test

# Ejecutar el script de setup
bash setup_env.sh
```

Esto creará un entorno virtual, lo activará y descargará las dependencias.

---

## 📁 Estructura del Proyecto

```
backend-dev-mid-test/
├── database/                  # Punto 1: Base de datos para blog
│   ├── blog_platform.png      # Diagrama ER
│   ├── blog_platform.sql
│   └── models.py              # Modelos SQLAlchemy
├── .gitignore
├── README.md
├── requirements.txt
└── setup_env.sh
```

---

## 🧠 Punto 1: Base de Datos de Blog

Se diseñó una base de datos relacional que permite:
- Registrar usuarios
- Publicar entradas de blog
- Comentar en entradas
- Etiquetar publicaciones

### Diagrama ER

![Diagrama ER](database/blog_platform.png)

### Archivos
- `blog_platform.sql`: script SQL para crear la base de datos
- `models.py`: versión en SQLAlchemy de los modelos

---