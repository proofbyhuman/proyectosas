from agent.modules.reporter import generate_client_dossier

# Consolidar ambas verticales en un dossier visual
generate_client_dossier(
    talent_data=talent_results,
    shadow_assets_data=shadow_results,
    client_name="Empresa Cliente S.A."
)
# Output: reports/Empresa_Cliente_SA_OSINT_Dossier.html