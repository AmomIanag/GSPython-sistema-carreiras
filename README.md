# GSPython-sistema-carreiras

Sistema de Recomendação de Carreiras em python

Projeto em Python orientado a objetos que analisa competências profissionais e recomenda carreiras para o perfil do usuário cadastrado.
O foco é aproximar lógica de programação e desenvolvimento humano, simulando uma ferramenta inteligente de orientação para profissões do futuro.

 Funcionalidades

• Cadastro de perfil
• Cadastro de competências (nota de 0 a 10)
• Análise automática estilo "sistema de recomendação"
• Comparação com diversas carreiras
• Sugestão final da carreira mais compatível
• Interface simples pelo terminal (CLI)
• Código totalmente comentado para iniciantes

 Competências Avaliadas

O usuário deve informar notas de 0 a 10 para cada uma dessas competências técnicas:

• lógica

• criatividade

• colaboração

• adaptabilidade

• comunicação

• resolução de problemas

• pensamento crítico

• gestão de tempo

 Carreiras Disponíveis

O sistema possui um conjunto de carreiras, cada uma com suas competências mais importantes:

• Programador

• Designer

• Cientista de Dados

• Gestor de Projetos

• Analista de Sistemas

• Engenheiro de Software

• Especialista UX/UI

• Analista de Dados

• Professor / Educador

• Marketing Digital

• Cybersecurity / Segurança da Informação

Cada carreira possui um perfil mínimo necessário de competências, e o sistema compara isso com o perfil do usuário para gerar uma pontuação e decidir qual carreira é mais recomaendada.

 Estrutura do Código

O projeto utiliza orientação a objetos com quatro classes:

1. Competencia

Representa uma habilidade do usuário.

2. Perfil

Guarda o nome e a lista de competências cadastradas pelo usuário.

3. Carreira

Define um conjunto de competências importantes para determinada profissão.

4. SistemaOrientacao

Gerencia:

• menu

• cadastro de perfil

• cadastro de competências

• cálculo das recomendações



Estrutura de arquivos

sistema_orientacao.py
README.md

Como Executar

1. Certifique-se de ter Python 3 instalado.

2. Baixe o arquivo gspython.py.

3. Abra o terminal (CMD, PowerShell, bash etc.).

4. Execute:

python gspython.py

Use o menu para navegar:

1 - Crie um perfil
2 - Cadastrar Competências
3 - Gerar carreiras recomendadas
0 - Sair do programa



Exemplo de uso:

 Sistema de recomendação de carreira
1 - Crie um perfil
2 - Cadastrar Competências
3 - Gerar carreiras recomendadas
0 - Sair do programa
Escolha uma opção: 1

Digite seu nome: Amom
Perfil criado com sucesso!

Escolha uma opção: 2
Nota para lógica: 8
Nota para criatividade: 6
Nota para colaboração: 7
Competências técnicas cadastradas

Escolha uma opção: 3
Carreira: Programador | Pontuação: 5
Carreira: Designer | Pontuação: -2
Carreira mais indicada:
 Engenheiro de Software

Conceitos de Programação Utilizados

• Classes e objetos

• Atributos e métodos

• Listas e dicionários

• Loops

• Condicionais

• Funções

• Modularização de código

• Sistema de pontuação simples


Demonstração com prints

