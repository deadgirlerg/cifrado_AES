from cryptography.fernet import Fernet

# Generar una clave aleatoria para AES
clave = Fernet.generate_key()

# Crear un objeto Fernet con la clave
cipher_suite = Fernet(clave)

# Texto a cifrar
texto_original = "Metodo de encriptación AES, generamos una prueba"

# Cifrar el texto
texto_cifrado = cipher_suite.encrypt(texto_original.encode())

# Descifrar el texto
texto_descifrado = cipher_suite.decrypt(texto_cifrado)

# Imprimir los resultados
print("Texto Original:  ", texto_original)
print("Texto Cifrado:   ", texto_cifrado)
print("Texto Descifrado:", texto_descifrado.decode())