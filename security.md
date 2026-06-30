# 🔒 Security Policy / Política de Seguridad

> **Última actualización:** 2025-01-01
> **Versión del proyecto:** 0.1.0-alpha

---

## ⚠️ Aviso Legal y Uso Responsable

**OSINT SaaS Platform** es una herramienta diseñada para profesionales de ciberseguridad y recursos humanos. Su uso está sujeto a las siguientes condiciones innegociables:

### ✅ Uso Autorizado
- Auditorías de seguridad con **consentimiento escrito** del propietario del sistema objetivo.
- Programas de Bug Bounty con alcance (scope) definido.
- Investigaciones de talento (Talent Sourcing) en cumplimiento con GDPR, CCPA y normativas locales de protección de datos.
- Pentesting autorizado bajo contrato (Rules of Engagement).

### ❌ Uso Prohibido
- Acceso no autorizado a sistemas informáticos.
- Explotación de vulnerabilidades descubiertas sin consentimiento.
- Acoso, doxxing o vigilancia no consentida de individuos.
- Recolección de datos personales sin base legal legítima.
- Uso en jurisdicciones donde la herramienta viole leyes locales.

> **El desarrollador no se hace responsable del uso indebido de esta plataforma.**

---

## 🛡️ Medidas de Seguridad Implementadas

### 1. Seguridad de Datos en Reposo
| Componente | Medida |
|-----------|--------|
| Base de Datos | Autenticación SQL Server con SA_PASSWORD en variables de entorno |
| Credenciales Descubiertas | Almacenamiento **siempre enmascarado** (`AKIA...XXXX`) en tabla `Credentials_Exposed` |
| Archivos .env | Incluídos en `.gitignore`, nunca versionados |
| Reports Generados | Almacenados con permisos restringidos en el contenedor |

### 2. Seguridad de Datos en Tránsito
| Componente | Medida |
|-----------|--------|
| Agente ↔ Sync Server | Comunicación interna en red Docker aislada |
| Salidas a Internet | Exclusivamente a través de proxy Tor SOCKS5 |
| API Sync Server | Puerto 65200 expuesto solo en red interna (no en 0.0.0.0 en producción) |

### 3. OPSEC del Agente
- **Aislamiento de red:** Contenedor en red `tor_network` con `internal: true`
- **Rotación de identidad:** Circuitos Tor rotados con `NEWNYM`
- **JA3 Evasion:** `curl_cffi` para evitar fingerprinting TLS
- **Anti-detección:** Playwright Stealth para capturas web

---

## 🐛 Reportar Vulnerabilidades (Responsible Disclosure)

Si descubres una vulnerabilidad de seguridad en esta plataforma, te pedimos que sigas este protocolo:

### Pasos para Reportar

1. **NO** crees un Issue público en GitHub para vulnerabilidades de seguridad.
2. Envía un correo electrónico a: `security@tudominio.com` *(reemplaza con tu email real)*
3. Incluye en tu reporte:
   - Descripción detallada de la vulnerabilidad
   - Pasos para reproducirla (PoC)
   - Impacto potencial
   - Versión del proyecto afectada
   - Sugerencia de fix (opcional pero apreciada)

### Formato del Reporte
