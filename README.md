# ascon_ui
## Descripcion
Herramienta para estudiar y probar ASCON. Ascon es una familia de algoritmos de cifrado autenticado y de hashing diseñado para ser "lightweight" y facil de implementar
Mas informacion en https://ascon.iaik.tugraz.at/specification.html 


## Indicaciones para correr en local 
### 1) Crear un ambiente local virtual 

Make sure you are running the commands INSIDE source code directory
Virtualenv modules installation (Unix based systems)
```
$ virtualenv env
$ source env/bin/activate
```
 (Windows based systems)
 ```
$ # virtualenv env
$ # .\env\Scripts\activate
$
```
(Mac based systems)
```
$# python3 -m venv venv
$# source venv/bin/activate
```

### 2) Instalar dependencias (paquetes requeridos para el proyecto y sus versiones)
```
pip3 install -r requirements.txt 
```