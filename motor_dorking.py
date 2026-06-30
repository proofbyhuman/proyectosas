from agent.modules.dorker import DorkerEngine

# Inicializar motor
engine = DorkerEngine()

# Ejecutar auditoría de Shadow Assets
findings = engine.execute_dorks(target_domain="target-corp.com")

# Resultados
print(f"AWS Keys expuestas: {len(findings['aws_leaks'])}")
print(f"BBDD expuestas: {len(findings['db_exposures'])}")
print(f"URLs crudas: {len(findings['raw_urls'])}")