# ⚡ Polymarket BTC 5m Paper Trader

Simulador de paper trading para el mercado de **Bitcoin Up or Down de 5 minutos** en [Polymarket](https://polymarket.com). Empieza con $1,000 ficticios y practica tus predicciones en tiempo real sin arriesgar dinero real.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![HTML](https://img.shields.io/badge/Frontend-HTML%2FJS-orange?logo=html5)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 ¿Qué es?

Una interfaz web local que se conecta a las APIs públicas de Polymarket para mostrarte en tiempo real los precios del mercado BTC de 5 minutos. Tú decides si Bitcoin va **UP** o **DOWN** y el sistema rastrea tu PnL automáticamente.

### Características

- 📈 Precios en vivo del orderbook de Polymarket (actualización cada 8 seg)
- 💰 Saldo simulado de $1,000 USD (persistido en LocalStorage)
- 🎮 Trading manual: elige UP o DOWN con el monto que quieras
- 📊 Tabla de posiciones activas y historial de PnL
- ✅ Resolución automática al cierre del mercado de 5 min
- 🔧 Log de debug en vivo para ver qué hace el bot por detrás
- 🎨 Interfaz glassmorphism premium con diseño dark mode

## 🚀 Instalación

### Requisitos

- **Python 3.9+** (viene preinstalado en macOS)
- Un navegador web (Chrome, Firefox, Safari, etc.)
- No requiere `pip install` ni dependencias externas

### Pasos

1. **Clona el repositorio:**

```bash
git clone https://github.com/FLOPPA42/Polymarket-BTC-5m-Paper-Trader.git
cd Polymarket-BTC-5m-Paper-Trader
```

2. **Inicia el servidor:**

```bash
python3 server.py
```

Verás el siguiente mensaje:

```
╔══════════════════════════════════════════════════╗
║  Polymarket BTC 5m Paper Trader - Servidor Local ║
╠══════════════════════════════════════════════════╣
║  Abre en tu navegador:                           ║
║  👉  http://localhost:8000                       ║
║                                                  ║
║  Presiona Ctrl+C para detener el servidor.       ║
╚══════════════════════════════════════════════════╝
```

3. **Abre tu navegador y ve a:**

```
http://localhost:8000
```

¡Listo! Ya puedes empezar a tradear.

## 🎮 Cómo usar

1. Espera a que el indicador de estado cambie a **🟢 EN VIVO** (se conecta automáticamente al mercado actual de 5 minutos).
2. Ingresa el monto que quieres invertir (por defecto $100).
3. Presiona **COMPRAR UP** si crees que Bitcoin subirá, o **COMPRAR DOWN** si crees que bajará.
4. Cuando el mercado de 5 minutos se cierre, el bot verificará el resultado y actualizará tu saldo automáticamente.
5. Revisa tu historial de PnL en la tabla de abajo.

## 🏗️ Arquitectura

```
┌─────────────┐     ┌──────────────┐     ┌──────────────────────┐
│  Navegador  │────▶│  server.py   │────▶│  Polymarket APIs     │
│  index.html │◀────│  (proxy)     │◀────│  gamma / clob        │
└─────────────┘     └──────────────┘     └──────────────────────┘
```

- **`server.py`** — Servidor local Python que sirve el HTML y actúa como proxy para las APIs de Polymarket (necesario para evitar restricciones CORS del navegador).
- **`index.html`** — Interfaz completa con toda la lógica de trading, estado y visualización.

## ☁️ Deploy en Vercel

También puedes desplegarlo en [Vercel](https://vercel.com) para acceder desde cualquier lugar:

1. Haz fork o sube este repo a tu GitHub.
2. Ve a [vercel.com](https://vercel.com) y crea un nuevo proyecto conectando tu repo.
3. ¡Listo! Vercel usará el `vercel.json` incluido para redirigir las peticiones de API automáticamente.

> **Nota:** En Vercel no necesitas `server.py`. El archivo `vercel.json` configura las redirecciones (rewrites) a las APIs de Polymarket directamente desde el edge de Vercel.

## ⚠️ Disclaimer

Este proyecto es **únicamente para fines educativos y de simulación**. No se realizan transacciones reales. No inviertas dinero real basándote en los resultados de este simulador.

## 📄 Licencia

MIT
