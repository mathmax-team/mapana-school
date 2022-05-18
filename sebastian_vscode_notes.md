Se pueden abrir varios repositorios simultáneamente. Un proyecto puede estar conformado por varios repositorios. Para esto se usa *File->Add folder to workspace*
Se puede salvar el workspace con *Save workspace as*
Configurar Workspace venv: Abrir el debugger crear json -> workspace. Agregar linea "python.defaultInterpreterPath":camino_del_venv (después de justMyCode:True)
Buena idea: añadir *.code* a .gitignore (para ignorar archivos de configuración de vscode).

Debugger:
Permite correr un script por bloques e inspeccionar el estado de las variables al final de cada bloque.
Convención de vscode: crear una carpeta en la raíz del proyecto llamada .vscode (añadir a .gitignore) y dentro de la carpeta crear un archivo launch.json (se puede hacer automáticamente desde el botón Run and Debug). En la configuración tenemos:
* program: programa para correr el script, con el commando python.
* module: programa para correr el script, con el commando python.
* console: permitir que el debugger use la consola (integratedTerminal)
* args: se puede agregar, es una lista de strings necesarias para correr el script. Por ejemplo con streamlit sería ['run', 'my_app.py']
* python: la ruta para el ambiente virtual

tarea: configurar como este por defecto
    linters: (pycodestyle, flake8)