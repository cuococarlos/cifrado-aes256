# cifrado-aes256

Este proyecto utiliza una libreria de Python para poder hacer el cifrado, la libreria es [PyAesCrypt](https://pypi.org/project/pyAesCrypt/)


## Instrucciones de Uso

### Instalar Dependecias

```bash
pip install -r requirements.txt
```


### Encriptar un archivo

Utilizar el comando:
```bash
python lab2.py encrypt-file --password unpassword --file rutadearchivo
```

En caso de no setear un password,se seteara la contraseña por default
```bash
python lab2.py encrypt-file  --file rutadearchivo
```

### Desencriptar un archivo

Para esto debemos utilizar el comando:
```bash
python lab2.py decrypt-file --password unpassword--path_encrypt rutaArchivo.aes
```