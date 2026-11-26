# Validador e Formatador de Documentos (CPF, RG e PIS)

Script em Python puro desenvolvido para higienizar, validar e formatar números de **CPF**, **RG** e **PIS/PASEP** segundo os padrões oficiais brasileiros, aplicando cálculo matemático de dígitos verificadores (Módulo 11) e bloqueio de entradas inválidas.

## Regras de Validação Implementadas

* **Higienização e Formato:**
  * Remoção automática de espaços em branco nas extremidades com `.strip()`.
  * Verificação estrita de caracteres numéricos com `.isdigit()` e tamanho exato (`11` dígitos para CPF/PIS e `9` dígitos para RG).
  * Bloqueio de sequências repetidas inválidas (ex: `11111111111`, `00000000000`).
* **Cálculo Matemático (Módulo 11):**
  * **CPF:** Validação independente do 10º e 11º dígitos verificadores com pesos decrescentes de `10` a `2` e de `11` a `2`.
  * **PIS/PASEP:** Validação do 11º dígito verificador segundo a regra da Caixa Econômica Federal, aplicando os pesos `[3, 2, 9, 8, 7, 6, 5, 4, 3, 2]`.
* **Formatação de Saída:**
  * **CPF:** `XXX.XXX.XXX-XX`
  * **RG:** `XX.XXX.XXX-X`
  * **PIS:** `XXX.XXXXX.XX-X`

## Massa de Dados Fictícios para Teste (QA)

| Documento | Entrada de Teste | Resultado Esperado | Motivo |
| :--- | :--- | :--- | :--- |
| **PIS** | `12312345120` | Válido (`123.12345.12-0`) | Dígito verificador `0` compatível com o cálculo Módulo 11 |
| **PIS** | `17033259504` | Válido (`170.33259.50-4`) | Dígito verificador `4` compatível com o cálculo Módulo 11 |
| **PIS** | `12312345121` | **Inválido (Bloqueado)** | Dígito verificador incorreto (esperado `0`, informado `1`) |
| **CPF** | `11111111111` | **Inválido (Bloqueado)** | Sequência de dígitos repetidos rejeitada pela regra de borda |
| **RG** | `463669083` | Válido (`46.366.908-3`) | Formato numérico de 9 dígitos válido |

## Como Executar

1. Certifique-se de ter o **Python 3** instalado.
2. Execute o ficheiro pelo terminal:

```bash
python validador_docs.py
