import click
import pyAesCrypt
import os

@click.group()
def cli():
    pass

@click.command()
@click.option('--password', default="passwordmuyseguro", help='Palabra clave que vamos a utilizar para encriptar')
@click.option('--file', prompt='Ingrese el archivo',
              help='Ruta donde se encuentra el archivo a encriptar.')

def encrypt_file(password, file):
    """Función para encriptar un archivo AES-256BC"""    
    pyAesCrypt.encryptFile(file, file + ".aes", password)


@click.command()
@click.option('--password', default="passwordmuyseguro", help='Palabra clave que vamos a utilizar para desencriptar')
@click.option('--path_encrypt', prompt='Ingrese la ruta al  archivo',
              help='Ruta donde se encuentra el archivo a desencriptar.')
def decrypt_file(password,path_encrypt):
    """Función para desencriptar un archivo en AES-256BC"""
    filename,aes_extension = os.path.splitext(path_encrypt)
    pyAesCrypt.decryptFile(path_encrypt, filename, password)

cli.add_command(decrypt_file)
cli.add_command(encrypt_file)

if __name__ == '__main__':
    cli()