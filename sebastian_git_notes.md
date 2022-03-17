Crear un repositorio:
- crear una carpeta y pararse en ella
- cmd git init

Como saber si algo es un repositorio: git status

Buena idea revisar la configuracion: cat .git/config

Ayuda! git --help

Añadir repositorio a repositorio existente: git remote add nombre_que_quiero git@github.com:...

Cambiar de branch: git checkout nombre_de_rama

Cambiar de repositorio en vscode: abrir nueva ventana

Hacer commit de lineas: seleccionar las lineas --> click derecho --> stage selected

Crear rama: git branch nombre_de_rama

Push de nueva rama: git push --set-upstream nombre_de_nube nombre_de_rama

Hacer merge: pararse en el branch que va a permanecer y luego git merge otro_branch
- Antes de merge: * Limpiar git (nada de cambios, hacer commit, discard o stash)
                  * actualizar ramas: git fetch
                  * hacer checkout a la rama que va a permanecer
                  * git reset --hard nombre_repo/nombre_rama
                  * git pull nombre_repo (opcional el nombre del repo)
                  * git merge nombre_rama
