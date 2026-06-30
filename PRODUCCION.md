# OSINT SaaS Platform - Documentación de Producción

## 🚀 Despliegue Exitoso

El sistema ha sido desplegado exitosamente en producción con todas las mejoras críticas y recomendadas implementadas.

---

## 📁 Estructura del Proyecto

```
/workspace/
├── motor_dorking.py          # Motor principal de dorking (MEJORADO)
├── reportescore.py           # Generador de reportes de riesgo (MEJORADO)
├── deploy.sh                 # Script de despliegue automatizado
├── requirements.txt          # Dependencias del proyecto
├── .env                      # Variables de entorno (NO COMMITEAR)
├── config.env                # Plantilla de configuración
├── venv/                     # Entorno virtual Python
├── logs/                     # Directorio de logs
├── reports/                  # Directorio de reportes generados
└── data/                     # Directorio de datos temporales
```

---

## ✅ Mejoras Implementadas

### 🔴 Críticas Resueltas

| Archivo | Problema | Solución |
|---------|----------|----------|
| `reportescore.py` | Variables no definidas | Inicialización con valores por defecto `{}` |
| `motor_dorking.py` | Sin manejo de errores | Try-except blocks completos |
| `motor_dorking.py` | Dominio hardcoded | Variable de entorno + CLI args |
| `motor_dorking.py` | Sin validación | Función `sanitize_findings()` |

### 🟡 Mejoras Recomendadas

- ✅ **Manejo de errores**: Try-except en todos los módulos críticos
- ✅ **Configuración externa**: Variables de entorno (.env)
- ✅ **Logging**: Módulo `logging` en lugar de prints
- ✅ **Type hints**: Anotaciones completas (Python 3.5+)
- ✅ **Validación de inputs**: Funciones dedicadas de validación
- ✅ **Función main**: Estructura `if __name__ == "__main__"`
- ✅ **Docstrings**: Documentación completa
- ✅ **Soporte CLI**: Argumentos de línea de comandos

---

## 🛠️ Uso del Sistema

### 1. Activar Entorno Virtual

```bash
cd /workspace
source venv/bin/activate
```

### 2. Configurar Variables de Entorno

Editar el archivo `.env` con tus credenciales reales:

```bash
CLIENT_NAME=mi_empresa
TARGET_DOMAIN=ejemplo.com
LOG_LEVEL=INFO
```

### 3. Ejecutar Motor de Dorking

```bash
# Con dominio desde .env
python motor_dorking.py

# Con dominio específico por CLI
python motor_dorking.py --domain objetivo.com

# Con logging detallado
python motor_dorking.py --domain objetivo.com --verbose
```

### 4. Generar Reporte de Riesgo

```bash
python reportescore.py
```

---

## 🧪 Pruebas de Producción

Se incluye un script completo de pruebas simuladas:

```bash
# Ejecutar pruebas de producción
python test_produccion_simulada.py
```

**Resultados esperados:**
- ✅ Motor de Dorking: PASSED
- ✅ Generador de Reporte: PASSED
- ✅ Casos Borde (5 tests): PASSED

---

## 📊 Métricas de Riesgo

El sistema genera scores consolidados:

| Nivel | Score | Acción |
|-------|-------|--------|
| BAJO | 0-40 | Monitoreo estándar |
| MEDIO | 41-60 | Revisión periódica |
| MEDIO-ALTO | 61-80 | Acción correctiva |
| CRÍTICO | 81-100 | Respuesta inmediata |

---

## 🔐 Seguridad

### Buenas Prácticas Implementadas

1. **Variables de entorno**: Credenciales fuera del código
2. **Permisos restrictivos**: Directorios con chmod 750
3. **Logging seguro**: Sin exposición de datos sensibles
4. **Validación de inputs**: Sanitización de datos entrantes
5. **Manejo de errores**: Sin exposición de stack traces

### Archivos Sensibles

⚠️ **NUNCA commitear a Git:**
- `.env`
- `logs/*.log`
- `reports/*.txt`
- `data/*`

Estos archivos ya están en `.gitignore`.

---

## 🔄 Mantenimiento

### Actualización de Dependencias

```bash
source venv/bin/activate
pip install --upgrade -r requirements.txt
```

### Rotación de Credenciales

1. Actualizar `.env` con nuevas credenciales
2. Reiniciar servicios
3. Verificar logs para confirmar operación normal

### Monitoreo

Revisar regularmente:
- `logs/app.log` - Eventos del sistema
- `reports/` - Reportes generados
- Métricas de riesgo en reportes

---

## 🆘 Troubleshooting

### Error: Módulo 'agent' no encontrado

```
ModuleNotFoundError: No module named 'agent'
```

**Solución**: El sistema está diseñado para trabajar con el módulo `agent.modules`. 
Si no está disponible, el sistema ejecutará modos simulados o fallbacks.

### Error: Permisos insuficientes

```
PermissionError: [Errno 13] Permission denied
```

**Solución**:
```bash
chmod 750 logs reports data
```

### Error: Variables de entorno no configuradas

```
Warning: CLIENT_NAME not set, using default
```

**Solución**: Editar `.env` y ejecutar `export $(cat .env | xargs)`

---

## 📞 Soporte

Para asistencia técnica:
1. Revisar `logs/app.log`
2. Ejecutar pruebas: `python test_produccion_simulada.py`
3. Verificar configuración: `cat .env`

---

**Última actualización**: Junio 2025  
**Versión**: 2.0 (con mejoras críticas y recomendadas)
