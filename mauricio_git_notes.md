Clase de Git

1. REPOSITORIOS Y BRANCHING.

Lo primero que hay que hacer es verificar que uno no esté parado en una carpeta que sea un repositorio. Para hacerlo dar los comandos:
- git status : para verificar si la carpeta en la que se está parado es un repositorio.
- ls .git : también sirve.

En caso tal que se quiera crear una subcarpeta, crearla con el comando:
- mkdir 'carpeta'
- cd 'carpeta' : para moverse a la carpeta con nombre 'carpeta'.

Creación del repositorio:
- git init : se crea el repositorio en la carpeta donde se está ubicado.
- git remote add 'nombre_asignado' 'dirección' : se vincula el repositorio local a uno global.
- git pull 'nombre asignado' : para hacer pull del repositorio al que uno le dio nombre.

Nota: 'nombre_asignado' es un nombre que da uno (¿opcional?), y la 'dirección' la da el repositorio
que uno esté usando. Esta última se optiene del repositorio en linea. (Github en nuestro caso.)

Branching:
- git branch 'nom_branch': para crear el branch 'nom_branch'.
- git checkout 'nom_branch' : para trasladarse al branch 'nom_branch'.
- git fetch : para actualizar las ramas del repositorio.

Nota: Un branch creado no se verá reflejado en el repositorio hasta que no se haga el primer commit en él.

Convención para hacer commits. Para meter una descripción poner doble espacio.

Resolución de conflictos mediante creación de branches.

Branch merging:
- git merge 'branch to fuse.'
Para hacer esto se puede especificar donde se realiza la fusión, y cual es el branch que se está fusionando.
Sin embargo, lo recomendable es pararse en el branch donde uno quiere que se establezca el merge.

Antes de un merge
  1. No dejar cambios ni en stach ni en changes. Ya sea hacerles commit, discard o stach.
  2. Actualizar con - git fetch.
  3. Cambiarse de rama a la rama en la que va a quedar el merge.
  4. dar el comando: git reset --hard 'nombre repositorio'/'nombre_rama'. (Paso opcional)
  5. git pull (opcional con el nombre del repositorio)
  6. Realizar el merge.
  7. Lidiar con conflictos.
  6. Salvar, stage y commit.

 El paso 4 es complicado, y hay que hacerlo con cuidado, pues es un comando destructivo.

Algunos comandos útiles:
- git --help : para ver la lista de opciones de git.
- cat 'archivo' : para ver los contenidos de 'archivo' sin abrirlo.

2. AMBIENTES VIRTUALES.

Para empezar, se debe crear una carpeta que va a contener el ambiente virutal. Por convenio nosotros usaremos el nombre 'venv'.
La carpeta de venv no se debe compartir, por lo tanto debe estar metida en el archivo de gitignore.

Para instalar un ambiente virtual se debe dar los siguientes comandos:
 1. sudo apt install -y python3-venv # Esto pedirá el password del equipo.
 2. python3 -m venv venv # Él último venv se refiere a la carpeta.
Después se da el siguiente comando para activar el ambiente virtual:
 3. source venv/bin/activate # El primer venv se refiere al nombre del ambiente virtual.

Después de esto se debe crear la carpeta de requerimientos, la cual, por convenio, estamos llamando 'requirements.txt'.
Una vez se agreguen los requerimientos, o se modifique el archivo, se debe dar el comando:
 - pip install -r requirements.txt

Comandos útiles:

- pip freeze : devuelve la lista de paquetes instalados en el ambiente virtual.
