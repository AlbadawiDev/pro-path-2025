# pro-path-2025
Ruta anual (SWE + Cloud + Data + Security).

## Objetivo 2025
- Empleabilidad como SWE/Cloud junior con base en Data y prácticas de seguridad.

## Hitos (Q2)
- [ ] API FastAPI con despliegue en cloud
- [ ] ETL simple + dashboard
- [ ] Checklist de seguridad (linters, dependabot, secrets)

## Estructura
- /projects  -> proyectos mayores
- /labs      -> laboratorios/pruebas
- /notes     -> apuntes del día
- /configs   -> configuraciones (pre-commit, linters, etc.)

## Estado verificado (2026-10-07)

Este repositorio contiene laboratorios de aprendizaje, no una aplicación completa. `labs/hello_api.py` responde una API de saludo y `labs/word_freq.py` cuenta palabras Unicode. El contador se puede importar sin pedir entrada por consola.

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-lock.txt
.\.venv\Scripts\python.exe -m pytest -q -W error
.\.venv\Scripts\python.exe -m uvicorn labs.hello_api:app --host 127.0.0.1 --port 8014
```

4 pruebas verificadas en Windows/Python 3.13: respuesta HTTP real de la aplicación ASGI, texto Unicode, entrada vacía y límites. La API también se inició con Uvicorn y respondió HTTP 200 en loopback. Dependencias instaladas y fijadas; `pip-audit` no reportó vulnerabilidades conocidas en el lock el 2026-10-07. Los hitos originales siguen pendientes; no se presentan como productos terminados ni certificaciones obtenidas.
