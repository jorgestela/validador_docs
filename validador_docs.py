# --- Funções Auxiliares ---


# Função para verificar se todos os dígitos de um número são iguais
def sequencia_repetida(numero: str) -> bool:
    """Retorna True se todos os dígitos forem iguais (ex: '11111111111')."""
    return numero == numero[0] * len(numero)

# Função para validar o primeiro dígito do CPF
def validar_primeiro_digito_cpf(cpf: str) -> bool:
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito = (soma * 10 % 11) % 10
    return digito == int(cpf[9])

# Função para validar o segundo dígito do CPF
def validar_segundo_digito_cpf(cpf: str) -> bool:
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito = (soma * 10 % 11) % 10
    return digito == int(cpf[10])


# --- Funções Principais de Validação ---

# Função principal para validar CPF, RG e PIS
def validar_cpf(cpf: str) -> bool:
    """Valida tamanho, caracteres numéricos, repetição e os 2 dígitos verificadores."""
    if not cpf.isdigit() or len(cpf) != 11 or sequencia_repetida(cpf):
        return False
    return validar_primeiro_digito_cpf(cpf) and validar_segundo_digito_cpf(cpf)

# Função principal para validar RG
def validar_rg(rg: str) -> bool:
    """Valida formato numérico de 9 dígitos e bloqueia sequências repetidas."""
    return rg.isdigit() and len(rg) == 9 and not sequencia_repetida(rg)


# Função principal para validar PIS
def validar_pis(pis: str) -> bool:
    """Valida PIS/PASEP usando os pesos oficiais da Caixa Econômica Federal."""
    if not pis.isdigit() or len(pis) != 11 or sequencia_repetida(pis):
        return False
    
# Calcula o dígito verificador do PIS
    pesos = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(pis[i]) * pesos[i] for i in range(10))
    resto = soma % 11
    digito_esperado = 0 if resto < 2 else 11 - resto
# Verifica se o dígito calculado confere com o último dígito do PIS
    return digito_esperado == int(pis[10])


# --- Fluxo Principal de Entrada e Formatação ---


# --- Entrada de Dados do Usuário ---
cpf = input("Digite o CPF (apenas números): ").strip()
while not validar_cpf(cpf):
    cpf = input("CPF inválido (formato ou dígito verificador incorreto). Digite novamente: ").strip()

# --- Entrada de Dados do Usuário para RG ---
rg = input("Digite o RG (apenas números): ").strip()
while not validar_rg(rg):
    rg = input("RG inválido. Digite apenas números com 9 dígitos: ").strip()

# --- Entrada de Dados do Usuário para PIS ---
pis = input("Digite o PIS (apenas números): ").strip()
while not validar_pis(pis):
    pis = input("PIS inválido (formato ou dígito verificador incorreto). Digite novamente: ").strip()

# Formatação padrão brasileiro
cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
rg_formatado = f"{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8:]}"
pis_formatado = f"{pis[:3]}.{pis[3:8]}.{pis[8:10]}-{pis[10:]}"

# --- Exibição dos Documentos Validados ---
print("\n--- Documentos Validados com Sucesso ---")
print("CPF válido:", cpf_formatado)
print("RG válido:", rg_formatado)
print("PIS válido:", pis_formatado)