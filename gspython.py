
# Sistema para recomendar carreiras
# Amom RM 565718
# Fernando 562549


class Competencia:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota


class Perfil:
    def __init__(self, nome):
        self.nome = nome
        self.competencias = []

    def adicionar_competencia(self, nome, nota):
        nova = Competencia(nome, nota)
        self.competencias.append(nova)

    def obter_notas(self):
        return {c.nome: c.nota for c in self.competencias}


class Carreira:
    def __init__(self, nome, competencias_necessarias):
        self.nome = nome
        self.competencias_necessarias = competencias_necessarias

    def calcular_pontuacao(self, competencias_usuario):
        pontuacao = 0

        # Quanto mais o usuário se aproxima do que é exigido, mais pontos el e ganha
        for nome, minimo in self.competencias_necessarias.items():
            if nome in competencias_usuario:
                pontuacao += competencias_usuario[nome] - minimo

        return pontuacao


class SistemaOrientacao:
    def __init__(self):
        self.perfil = None
        self.carreiras = []
        self.carregar_carreiras()

        # Colocamos mais competências técnicas
        self.lista_competencias = [
            "lógica",
            "criatividade",
            "colaboração",
            "adaptabilidade",
            "comunicação",
            "resolução de problemas",
            "pensamento crítico",
            "gestão de tempo"
        ]

    def carregar_carreiras(self):

        # Carreiras que foram usadas como exemplo no arquivo

        self.carreiras.append(Carreira("Programador", {
            "lógica": 7,
            "criatividade": 4,
            "adaptabilidade": 6
        }))

        self.carreiras.append(Carreira("Designer", {
            "criatividade": 7,
            "colaboração": 6,
            "comunicação": 6
        }))

        self.carreiras.append(Carreira("Cientista de Dados", {
            "lógica": 8,
            "adaptabilidade": 7,
            "pensamento crítico": 8
        }))

        self.carreiras.append(Carreira("Gestor de Projetos", {
            "colaboração": 8,
            "adaptabilidade": 6,
            "comunicação": 8,
            "gestão de tempo": 7
        }))


        # Novas carreiras que colocamos


        # 1) Analista de Sistemas
        self.carreiras.append(Carreira("Analista de Sistemas", {
            "lógica": 7,
            "comunicação": 7,
            "resolução de problemas": 8
        }))

        # 2) Engenheiro de Software
        self.carreiras.append(Carreira("Engenheiro de Software", {
            "lógica": 9,
            "pensamento crítico": 8,
            "resolução de problemas": 8,
            "gestão de tempo": 6
        }))

        # 3) Especialista UX/UI
        self.carreiras.append(Carreira("Especialista UX/UI", {
            "criatividade": 8,
            "colaboração": 7,
            "comunicação": 6
        }))

        # 4) Analista de Dados
        self.carreiras.append(Carreira("Analista de Dados", {
            "pensamento crítico": 8,
            "lógica": 7,
            "resolução de problemas": 7
        }))

        # 5) Professor / Educador
        self.carreiras.append(Carreira("Professor / Educador", {
            "comunicação": 9,
            "colaboração": 7,
            "pensamento crítico": 6
        }))

        # 6) Marketing Digital
        self.carreiras.append(Carreira("Marketing Digital", {
            "criatividade": 8,
            "comunicação": 7,
            "adaptabilidade": 6
        }))

        # 7) Segurança da Informação
        self.carreiras.append(Carreira("Cybersecurity / Segurança da Informação", {
            "pensamento crítico": 8,
            "lógica": 8,
            "resolução de problemas": 8
        }))

    def criar_perfil(self):
        nome = input("\nDigite seu nome: ")
        self.perfil = Perfil(nome)
        print("Perfil criado com sucesso!\n")

    def cadastrar_competencias(self):
        if not self.perfil:
            print("Crie um perfil primeiro!\n")
            return

        print("\nCadastro de Competências técnicas")
        print("Digite notas de 0 a 10.")

        for comp in self.lista_competencias:
            nota = int(input(f"Nota para {comp}: "))
            self.perfil.adicionar_competencia(comp, nota)

        print("Competências técnicas cadastradas\n")

    def recomendar_carreira(self):
        if not self.perfil:
            print("Crie o seu perfil e cadastre suas competências técnicas\n")
            return

        notas = self.perfil.obter_notas()

        print("\nCarreiras recomendadas")

        melhor_carreira = None
        melhor_pontuacao = -999

        for carreira in self.carreiras:
            pontuacao = carreira.calcular_pontuacao(notas)
            print(f"Carreira: {carreira.nome} | Pontuação: {pontuacao}")

            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_carreira = carreira

        print("\nCarreira mais indicada:")
        print(f" {melhor_carreira.nome}\n")

    def menu(self):
        while True:
            print("Sistema de recomendação de carreira")
            print("1 - Crie um perfil")
            print("2 - Cadastrar Competências")
            print("3 - Gerar carreiras recomendadas")
            print("0 - Sair do programa")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.criar_perfil()
            elif opcao == "2":
                self.cadastrar_competencias()
            elif opcao == "3":
                self.recomendar_carreira()
            elif opcao == "0":
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida\n")


# Código main (principal)
if __name__ == "__main__":
    sistema = SistemaOrientacao()
    sistema.menu()
