#!/bin/bash
# ============================================
# Script de Despliegue en Producción - OSINT SaaS
# ============================================

set -e  # Detener en caso de error

echo "🚀 Iniciando despliegue en producción..."

# 1. Verificar Python
echo "✓ Verificando Python..."
python3 --version

# 2. Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
fi

# 3. Activar entorno virtual
echo "🔌 Activando entorno virtual..."
source venv/bin/activate

# 4. Actualizar pip
echo "⬆️  Actualizando pip..."
pip install --upgrade pip

# 5. Instalar dependencias
echo "📥 Instalando dependencias..."
pip install -r requirements.txt

# 6. Copiar configuración de producción
echo "⚙️  Configurando variables de entorno..."
if [ ! -f ".env" ]; then
    cp config.env .env
    echo "⚠️  IMPORTANTE: Edita el archivo .env con tus credenciales reales"
fi

# 7. Validar sintaxis de los módulos principales
echo "✅ Validando sintaxis de Python..."
python3 -m py_compile motor_dorking.py
python3 -m py_compile reportescore.py
echo "✓ Sintaxis válida"

# 8. Ejecutar pruebas de humo (smoke tests)
echo "🧪 Ejecutando pruebas de humo..."
python3 -c "
import motor_dorking
import reportescore
print('✓ Imports exitosos')
"

# 9. Crear directorios necesarios
echo "📁 Creando estructura de directorios..."
mkdir -p logs
mkdir -p reports
mkdir -p data

# 10. Configurar permisos
echo "🔒 Configurando permisos..."
chmod 750 logs
chmod 750 reports
chmod 750 data

# 11. Crear archivo de log inicial
echo "📝 Inicializando sistema de logging..."
touch logs/app.log

# 12. Mostrar resumen
echo ""
echo "============================================"
echo "✅ DESPLIEGUE COMPLETADO EXITOSAMENTE"
echo "============================================"
echo ""
echo "📂 Estructura creada:"
echo "   - venv/          : Entorno virtual"
echo "   - logs/          : Directorio de logs"
echo "   - reports/       : Directorio de reportes"
echo "   - data/          : Directorio de datos"
echo ""
echo "⚙️  Próximos pasos:"
echo "   1. Editar .env con credenciales reales"
echo "   2. Configurar módulo agent.modules"
echo "   3. Ejecutar: source venv/bin/activate"
echo "   4. Ejecutar motor: python motor_dorking.py --domain tu-dominio.com"
echo "   5. Generar reporte: python reportescore.py"
echo ""
echo "🔐 Notas de seguridad:"
echo "   - No commitear el archivo .env a Git"
echo "   - Rotar credenciales regularmente"
echo "   - Revisar logs/ para monitoreo"
echo ""
