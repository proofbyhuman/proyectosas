# 🛡️ OSINT SaaS Platform

> **Plataforma de Inteligencia de Fuentes Abiertas de doble vertical: Talent Sourcing y Auditoría de Shadow Assets.**

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker)
![SQL Server](https://img.shields.io/badge/SQL%20Server-2022-CC2927?style=for-the-badge&logo=microsoft-sql-server)
![License](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Alpha-orange?style=for-the-badge)

---

## 📖 Descripción

**OSINT SaaS Platform** es una arquitectura modular diseñada para orquestar dos verticales de investigación automatizada:

| Vertical | Descripción | Público Objetivo |
|----------|------------|------------------|
| 🎯 **Talent Sourcing** | Súper Máquina OSINT para enriquecimiento masivo de perfiles, mapeo de talento y recolección de contactos (inspirada en la metodología de José Kadlec). | Recruiters, Headhunters, RRHH |
| 🔥 **Shadow Assets** | Motor de Google Dorking automatizado para detectar fugas de infraestructura, credenciales en `.env` y bases de datos expuestas (AWS, Firebase). | Red Teams, Pentesters, CISOs |

Ambas verticales comparten un **motor de infraestructura unificado** (proxies Tor, OCR, evasión de anti-bots) pero se presentan como **experiencias de usuario completamente independientes** mediante un sistema de Workspaces.

---

## 🏗️ Arquitectura del Sistema
