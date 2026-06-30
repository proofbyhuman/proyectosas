#!/usr/bin/env python3
"""
Motor de Dorking para auditoría de Shadow Assets.

Ejecuta consultas OSINT automatizadas para detectar activos expuestos,
credenciales filtradas y URLs sensibles en motores de búsqueda.
"""

import logging
import os
import sys
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def validate_domain(domain: str) -> bool:
    """
    Validar que el dominio tenga un formato válido.
    
    Args:
        domain: Dominio a validar
        
    Returns:
        bool: True si el dominio es válido
    """
    if not domain or not isinstance(domain, str):
        logger.error("El dominio debe ser una cadena no vacía.")
        return False
    
    # Validación básica de formato de dominio
    if '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        logger.error(f"Formato de dominio inválido: {domain}")
        return False
    
    return True


def get_target_domain() -> str:
    """
    Obtener el dominio objetivo desde variables de entorno o argumentos.
    
    Returns:
        str: Dominio objetivo
    """
    domain = os.getenv('TARGET_DOMAIN', '')
    
    if not domain:
        logger.warning("TARGET_DOMAIN no configurado en variables de entorno.")
        logger.warning("Usando dominio por defecto para demostración (NO USAR EN PRODUCCIÓN).")
        domain = "example.com"
    
    return domain


def sanitize_findings(findings: Optional[Dict]) -> Dict[str, List[Any]]:
    """
    Sanitizar y validar la estructura de resultados encontrados.
    
    Args:
        findings: Diccionario de resultados del motor de dorking
        
    Returns:
        Dict: Diccionario sanitizado con listas vacías si no hay datos
    """
    default_structure = {
        'aws_leaks': [],
        'db_exposures': [],
        'raw_urls': [],
        'sensitive_files': [],
        'subdomains': []
    }
    
    if not findings or not isinstance(findings, dict):
        logger.warning("Findings no válidos. Usando estructura por defecto.")
        return default_structure
    
    # Mantener solo las claves esperadas y asegurar que sean listas
    sanitized = {}
    for key in default_structure.keys():
        value = findings.get(key, [])
        if isinstance(value, list):
            sanitized[key] = value
        else:
            logger.warning(f"La clave '{key}' no es una lista. Usando lista vacía.")
            sanitized[key] = []
    
    return sanitized


def execute_dorking(target_domain: str) -> Optional[Dict[str, List[Any]]]:
    """
    Ejecutar el motor de dorking para un dominio objetivo.
    
    Args:
        target_domain: Dominio objetivo para la auditoría
        
    Returns:
        Dict: Resultados de la auditoría o None si hubo error
    """
    try:
        from agent.modules.dorker import DorkerEngine
    except ImportError as e:
        logger.error(f"Error importando módulo dorker: {e}")
        logger.error("Asegúrate de que el paquete 'agent' esté instalado correctamente.")
        return None
    
    try:
        logger.info(f"Inicializando motor de dorking para dominio: {target_domain}")
        engine = DorkerEngine()
        
        logger.info(f"Ejecutando auditoría de Shadow Assets para {target_domain}...")
        findings = engine.execute_dorks(target_domain=target_domain)
        
        # Sanitizar resultados
        sanitized_findings = sanitize_findings(findings)
        
        # Log de resultados
        logger.info("=" * 50)
        logger.info("RESULTADOS DE LA AUDITORÍA")
        logger.info("=" * 50)
        logger.info(f"AWS Keys expuestas: {len(sanitized_findings['aws_leaks'])}")
        logger.info(f"BBDD expuestas: {len(sanitized_findings['db_exposures'])}")
        logger.info(f"URLs crudas: {len(sanitized_findings['raw_urls'])}")
        logger.info(f"Archivos sensibles: {len(sanitized_findings.get('sensitive_files', []))}")
        logger.info(f"Subdominios encontrados: {len(sanitized_findings.get('subdomains', []))}")
        logger.info("=" * 50)
        
        return sanitized_findings
        
    except Exception as e:
        logger.error(f"Error ejecutando el motor de dorking: {e}", exc_info=True)
        return None


def main(target_domain: Optional[str] = None) -> Optional[Dict[str, List[Any]]]:
    """
    Función principal del motor de dorking.
    
    Args:
        target_domain: Dominio objetivo (opcional, se usa variable de entorno si no se proporciona)
        
    Returns:
        Dict: Resultados de la auditoría o None si hubo error
    """
    # Determinar dominio objetivo
    if target_domain is None:
        target_domain = get_target_domain()
    
    # Validar dominio
    if not validate_domain(target_domain):
        logger.error("Dominio objetivo inválido. Terminando ejecución.")
        return None
    
    logger.info(f"Dominio objetivo validado: {target_domain}")
    
    # Ejecutar dorking
    results = execute_dorking(target_domain)
    
    if results is None:
        logger.error("No se pudieron obtener resultados de la auditoría.")
        return None
    
    return results


if __name__ == "__main__":
    logger.info("Iniciando Motor de Dorking OSINT...")
    
    # Permitir pasar dominio como argumento de línea de comandos
    if len(sys.argv) > 1:
        target = sys.argv[1]
        logger.info(f"Dominio proporcionado vía línea de comandos: {target}")
    else:
        target = None
    
    results = main(target_domain=target)
    
    if results:
        print("\n✓ Auditoría completada exitosamente.")
        print(f"  - AWS Keys: {len(results['aws_leaks'])}")
        print(f"  - DB Exposures: {len(results['db_exposures'])}")
        print(f"  - Raw URLs: {len(results['raw_urls'])}")
        sys.exit(0)
    else:
        print("\n✗ Error en la auditoría. Revisar logs para más detalles.")
        sys.exit(1)