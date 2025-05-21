#!/bin/bash

echo "📦 Iniciando setup del entorno virtual..."

# Verificar si ya existe el entorno
if [ -d "venv" ]; then
    echo "✅ El entorno virtual ya existe. Activando..."
else
    echo "🔧 Creando entorno virtual..."
    python -m venv venv
fi

# Activar entorno virtual según sistema
if [[ "$OSTYPE" == "msys" ]]; then
    echo "💻 Detectado entorno Windows (Git Bash)"
    source venv/Scripts/activate
else
    echo "💻 Detectado entorno Linux/macOS"
    source venv/bin/activate
fi

echo "📚 Instalando dependencias..."
pip install -r requirements.txt

echo "🎉 Setup completo. Entorno activado y dependencias instaladas."