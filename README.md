# ⚡ Exercício Relâmpago Surpresa

As linhas do diagrama representam **associações entre classes**.  
As **setas** indicam o **sentido da comunicação**.  
O número **"1"** indica que apenas um objeto está relacionado.  
Você deverá escolher se cada associação será **obrigatória** ou **opcional**.

---

## 📘 Diagrama

<img width="913" height="473" alt="image" src="https://github.com/user-attachments/assets/ab05d8a5-0576-467d-91b7-69732bb1d6e9" />

O diagrama de classes mostra as seguintes entidades:

- **Pessoa**
- **Funcionário**
- **Cargo**
- **Ocorrência**
- **Dependente**

As relações principais incluem:
- Um **Funcionário** é uma **Pessoa**.
- Cada **Funcionário** possui um **Cargo**.
- Cada **Funcionário** pode ter várias **Ocorrências** (acréscimos e descontos).
- Cada **Funcionário** pode ter vários **Dependentes**.
- Cada **Dependente** possui uma data de nascimento.

---

## 🧩 Desafio

Com base no diagrama acima, implemente um sistema que resolva as seguintes questões:

### 1️⃣ Calcular o salário líquido de um funcionário

a. O método deve receber como parâmetros o **mês** e o **ano**.  
b. Buscar o valor do **salário bruto** do cargo do funcionário.  
c. Somar os **acréscimos** e subtrair os **descontos** das ocorrências referentes ao mês e ano informados.  
d. Acrescentar **R$100,00** para cada dependente com **menos de 18 anos** na data do cálculo.  

➡️ Método sugerido:  
```python
calcularSalarioLiquido(mes, ano)
```

---

### 2️⃣ Listar dependentes de um funcionário

a. Exibir o **nome e data de nascimento** de todos os dependentes.  
b. Calcular e exibir a **data do próximo aniversário** de cada dependente e quantos **dias faltam**.  
c. Informar **em qual dia da semana** cairá o próximo aniversário.

➡️ Método sugerido:  
```python
exibirDependentes()
```

---

## 🧮 Trabalhando com Datas

Dica de uso da biblioteca `datetime` para manipular datas:

```python
from datetime import date, datetime, timedelta

# Data atual
data_atual = date.today()
print(data_atual)

# Converter texto em data
d1 = datetime.strptime("01/12/2020", "%d/%m/%Y")
print(d1)

# Calcular diferença de dias
quantidade_dias = (d1.date() - data_atual).days
print(quantidade_dias)

# Incrementar dias
print(data_atual + timedelta(days=45))

# Dia da semana (0 = segunda-feira)
print(data_atual.weekday())
```

---

## 📎 Exemplo de Estrutura de Classes (sugestão)

```python
from datetime import date

class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Cargo:
    def __init__(self, salario_bruto):
        self.salario_bruto = salario_bruto


class Ocorrencia:
    def __init__(self, data_ocorrencia, valor_acrescimo=0, valor_desconto=0, descricao=""):
        self.data_ocorrencia = data_ocorrencia
        self.valor_acrescimo = valor_acrescimo
        self.valor_desconto = valor_desconto
        self.descricao = descricao


class Dependente(Pessoa):
    def __init__(self, nome, data_nascimento):
        super().__init__(nome)
        self.data_nascimento = data_nascimento


class Funcionario(Pessoa):
    def __init__(self, nome, cargo):
        super().__init__(nome)
        self.cargo = cargo
        self.ocorrencias = []
        self.dependentes = []

    def calcularSalarioLiquido(self, mes, ano):
        salario = self.cargo.salario_bruto

        for o in self.ocorrencias:
            if o.data_ocorrencia.month == mes and o.data_ocorrencia.year == ano:
                salario += o.valor_acrescimo
                salario -= o.valor_desconto

        for d in self.dependentes:
            idade = date.today().year - d.data_nascimento.year
            if idade < 18:
                salario += 100

        return salario

    def exibirDependentes(self):
        for d in self.dependentes:
            print(f"{d.nome} - Nascimento: {d.data_nascimento.strftime('%d/%m/%Y')}")
```

---

## ✍️ Tarefa

Implemente o código completo com as classes e:
- Crie instâncias de `Funcionário`, `Cargo`, `Ocorrência` e `Dependente`;
- Teste o cálculo do salário líquido;
- Exiba as informações dos dependentes e seus próximos aniversários.

---

## 🎯 Objetivo

Este exercício serve para **praticar Programação Orientada a Objetos**, **associações entre classes**, e **manipulação de datas** com `datetime` em Python.
