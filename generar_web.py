# generar_web.py
from perfiles import miembros

# Plantilla básica de HTML con algo de CSS (estilos)
html_inicio = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Equipo DevOps - Taller</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #1e1e2e; color: #cdd6f4; padding: 20px; }
        h1 { text-align: center; color: #89b4fa; }
        .contenedor { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; }
        .tarjeta { background-color: #313244; padding: 20px; border-radius: 10px; width: 250px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); border-top: 4px solid #f38ba8; }
        .tarjeta h2 { margin-top: 0; color: #f38ba8; font-size: 1.2rem;}
        .tarjeta p { margin: 5px 0; font-size: 0.9rem; }
    </style>
</head>
<body>
    <h1>🚀 Equipo del Taller DevOps 🚀</h1>
    <div class="contenedor">
"""

html_fin = """
    </div>
    <footer>
        <p>Track DevOps estuvo aquí</p>
    </footer>
</body>
</html>
"""

# Generamos las tarjetas para cada miembro
tarjetas_html = ""
for miembro in miembros:
    tarjetas_html += f"""
        <div class="tarjeta">
            <h2>{miembro.get('nombre', 'Anónimo')}</h2>
            <p><strong>🛠️ Rol:</strong> {miembro.get('rol', 'Por definir')}</p>
            <p><strong>✨ Habilidad:</strong> {miembro.get('habilidad', 'Misterio')}</p>
        </div>
    """

# Unimos todo y creamos el archivo
html_completo = html_inicio + tarjetas_html + html_fin

with open("index.html", "w", encoding="utf-8") as archivo:
    archivo.write(html_completo)

print("✅ ¡Éxito! Se ha generado el archivo 'index.html'. Ábrelo en tu navegador para ver el resultado.")
