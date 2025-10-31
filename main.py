from datetime import date
from datetime import datetime

from Funcionario import Funcionario
from Cargo import Cargo
from Ocorrencia import Ocorrencia
from Dependente import Dependente


# def salarioLiquido(func, dia, mes):
#     bruto = func.getCargo().getSalario_bruto()
#     ocorrencias = [p for p in func.getOcorrencias() if p.getDataOcorrencia().day() == dia and p.getOcorrencia().month == mes]
#     dependentes_menores = [p for p in func.getDependentes() if p.nascimento.year() > date.today().year - 18]
#     return bruto + ocorrencias + dependentes_menores

func = Funcionario()
c1 = Cargo(id = 1,funcao="Zelador", salario_bruto=4000)
oc1 = Ocorrencia(id = 2, data_ocorrencia=date(day=1, month=1, year=2025), valor_acrescimo=300, valor_desconto=500, descricao_ocorrencia="Impostos", funcionario=func)
dep = Dependente(parentesco="Filho", nascimento=date(day=15, month=12, year=2010))
dep2 = Dependente(parentesco="Filha", nascimento=date(day=15, month=12, year=2008))
dep.setNome("Cleiton")
dep2.setNome("Raissa")

func.setNome("Rafael")
func.setEndereco("Av. Brasil, 45")
func.setTelefone(32123456789)
func.setEmail("email@gmail.com")
func.setCargo(c1)
func.addOcorrencia(oc1)
func.addDependente(dep)
func.addDependente(dep2)

dia = date(day=10, month=5, year=2025)

dataOcorrencia = oc1.getDataOcorrencia().strftime("%d/%m/%Y")
print("Questão 1")
print(f"Salário {func.getNome()} - R${func.salarioLiquido(ano=2025, mes=1)}")
print("-"*30)

print("Questão 2")
func.listarDependentes()


