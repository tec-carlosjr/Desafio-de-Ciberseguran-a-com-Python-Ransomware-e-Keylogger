# 🛡️ Desafio de Cibersegurança com Python: Ransomware e Keylogger

Este repositório contém o resultado do desafio prático de Cibersegurança, onde foram desenvolvidos scripts em Python para simular o comportamento de malwares (Ransomware e Keylogger) em um **ambiente controlado**.

O objetivo principal deste projeto é educacional: compreender o funcionamento dessas ameaças para melhor desenvolver estratégias de defesa e mitigação.

## 🚀 Sobre o Projeto

O projeto está dividido em duas partes principais:
1. **Ransomware Simulado:** Um script que criptografa arquivos de uma pasta específica e outro que descriptografa usando uma chave gerada.
2. **Keylogger Simulado:** Um script que captura as teclas digitadas pelo usuário e as salva em um arquivo de log.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Biblioteca `cryptography`:** Para implementação da criptografia simétrica (Fernet).
* **Biblioteca `pynput`:** Para monitoramento dos eventos de teclado.

---

## 📂 Estrutura e Funcionalidades

### 1. Ransomware (Simulação)
O script de ransomware foi desenhado para atuar apenas em uma pasta de teste (`test_files`), garantindo a segurança do sistema hospedeiro.

* **`encrypter.py` (ou seu arquivo principal):** Percorre o diretório alvo, gera uma chave de criptografia e encripta os arquivos, tornando-os ilegíveis.
* **`decrypter.py`:** Utiliza a chave gerada (`chave.key`) para reverter o processo e restaurar os arquivos originais.

### 2. Keylogger
O keylogger registra as entradas do teclado em tempo real.

* **Funcionalidade:** Captura teclas alfanuméricas e teclas especiais (Espaço, Enter, Esc).
* **Armazenamento:** Salva os dados capturados em um arquivo local `log.txt`.
* **Tratamento de Erros:** Implementa lógica para lidar com teclas especiais que não possuem representação de caractere direto.

---

## 🛡️ Reflexão: Defesa e Mitigação

Entender o ataque é o primeiro passo para a defesa. Abaixo estão as medidas de prevenção contra as ameaças simuladas neste projeto:

### Contra Ransomwares:
1.  **Backups Regulares:** Manter cópias de segurança (offline ou na nuvem) é a defesa mais eficaz. Se os dados forem sequestrados, basta restaurar o backup.
2.  **Atualizações de Software:** Manter o sistema operacional e softwares atualizados corrige vulnerabilidades que malwares exploram.
3.  **Segmentação de Rede:** Evitar que um computador infectado contamine toda a rede da empresa.
4.  **Princípio do Menor Privilégio:** Usuários comuns não devem ter permissões de administrador, limitando o alcance da encriptação.

### Contra Keyloggers:
1.  **Antivírus e EDR:** Soluções modernas detectam comportamentos suspeitos, como "ganchos" (hooks) no teclado.
2.  **Teclados Virtuais:** Utilizar teclados na tela para digitar senhas bancárias dificulta a captura por keyloggers baseados em hardware ou software simples.
3.  **Autenticação de Dois Fatores (2FA):** Mesmo que o atacante capture a senha, ele não conseguirá acessar a conta sem o segundo fator (token/SMS).
4.  **Cuidado com Phishing:** Não executar anexos suspeitos ou clicar em links desconhecidos, que são as principais portas de entrada.

---

## ⚙️ Como Executar o Projeto

**Pré-requisitos:**
Certifique-se de ter o Python instalado. Instale as dependências necessárias:

```bash
pip install cryptography pynput
