🔒 Protocolo OPSEC (CSI_TorVPN)
El agente OSINT opera bajo un protocolo de Seguridad Operacional estricto:
Aislamiento de Red: Todo el tráfico del agente se enruta a través de una red Docker aislada (tor_network) con salida exclusiva por Tor SOCKS5.
Rotación de Circuitos: Se emite NEWNYM al controlador Tor después de cada batch de peticiones.
Evasión de Fingerprinting: Se utiliza curl_cffi para imitar handshakes TLS de navegadores reales (JA3 evasion).
Humanización: Delays aleatorios (distribución de Poisson) y rotación de User-Agents.
Credenciales Enmascaradas: Las claves detectadas se almacenan siempre enmascaradas (AKIA...XXXX).
🎨 Workspaces (Frontend)
La plataforma ofrece dos interfaces visualmente independientes:
🎯 Talent Workspace (Modo RRHH)
Paleta clara (blancos, azules suaves)
Tipografía: Inter
Enfoque: Tarjetas de perfiles, embudos, exportación CSV
Métricas: Perfiles enriquecidos, contactos, tasa de respuesta
🔥 Shadow Assets Workspace (Modo SecOps)
Paleta oscura (negro, verde terminal, rojo crítico)
Tipografía: JetBrains Mono
Enfoque: Terminal en vivo, grafos de red, alertas CVSS
Métricas: Leaks críticos, BBDD expuestas, subdominios