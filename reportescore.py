#!/usr/bin/env python3
"""
Módulo de generación de reporte de score OSINT.

Consolida las verticales de Talent Intelligence y Shadow Assets
en un dossier visual para el cliente.
"""

import logging
import os
import sys
from typing import Any, Dict, Optional

from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def validate_data(data: Any, data_name: str) -> bool:
    """
    Validar que los datos de entrada no sean None y tengan estructura válida.
    
    Args:
        data: Datos a validar
        data_name: Nombre del dato para mensajes de error
        
    Returns:
        bool: True si los datos son válidos
    """
    if data is None:
        logger.error(f"{data_name} es None. Debe inicializarse antes de generar el reporte.")
        return False
    
    if not isinstance(data, dict):
        logger.warning(f"{data_name} no es un diccionario. Tipo recibido: {type(data)}")
        return False
    
    return True


def get_client_name() -> str:
    """
    Obtener el nombre del cliente desde variables de entorno o usar valor por defecto.
    
    Returns:
        str: Nombre del cliente formateado
    """
    client_name = os.getenv('CLIENT_NAME', 'Empresa Cliente S.A.')
    logger.info(f"Generando reporte para cliente: {client_name}")
    return client_name


def main(talent_results: Optional[Dict] = None, shadow_results: Optional[Dict] = None) -> Optional[str]:
    """
    Función principal para generar el dossier del cliente.
    
    Args:
        talent_results: Resultados del módulo de Talent Intelligence
        shadow_results: Resultados del módulo de Shadow Assets
        
    Returns:
        str: Ruta del archivo generado o None si hubo error
    """
    try:
        from agent.modules.reporter import generate_client_dossier
    except ImportError as e:
        logger.error(f"Error importando módulo reporter: {e}")
        logger.error("Asegúrate de que el paquete 'agent' esté instalado correctamente.")
        return None
    
    # Validar datos de entrada
    if talent_results is None:
        logger.warning("talent_results no proporcionado. Usando diccionario vacío.")
        talent_results = {}
    
    if shadow_results is None:
        logger.warning("shadow_results no proporcionado. Usando diccionario vacío.")
        shadow_results = {}
    
    # Validar estructura de datos
    if not validate_data(talent_results, "talent_results"):
        talent_results = {}
    
    if not validate_data(shadow_results, "shadow_results"):
        shadow_results = {}
    
    # Obtener nombre del cliente
    client_name = get_client_name()
    
    try:
        logger.info("Generando dossier del cliente...")
        output_path = generate_client_dossier(
            talent_data=talent_results,
            shadow_assets_data=shadow_results,
            client_name=client_name
        )
        logger.info(f"Dossier generado exitosamente: {output_path}")
        return output_path
    except Exception as e:
        logger.error(f"Error generando el dossier: {e}", exc_info=True)
        return None


if __name__ == "__main__":
    # Ejemplo de uso con datos de prueba
    # En producción, estos datos vendrían de otros módulos
    logger.info("Iniciando generación de reporte de score...")
    
    # NOTA: En producción, importar y ejecutar los módulos correspondientes
    # para obtener talent_results y shadow_results reales
    talent_results_example = {}  # Reemplazar con datos reales
    shadow_results_example = {}  # Reemplazar con datos reales
    
    output_file = main(
        talent_results=talent_results_example,
        shadow_results=shadow_results_example
    )
    
    if output_file:
        print(f"Reporte generado: {output_file}")
        sys.exit(0)
    else:
        print("Error generando el reporte. Revisar logs para más detalles.")
        sys.exit(1)