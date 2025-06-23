Contexto do Sistema: MoodTasker

O MoodTasker é um sistema de gerenciamento de tarefas projetado para ajudar os usuários a organizar suas atividades diárias levando em consideração seu estado de humor e nível de energia. A plataforma permite que o usuário cadastre tarefas, defina suas prioridades, estime o tempo de execução e, mais importante, registre seu bem-estar. Com base nesses dados, o sistema oferece um histórico para que o usuário possa analisar a relação entre seu estado emocional/energético e sua produtividade ao longo do tempo. O objetivo é promover um planejamento de tarefas mais consciente e equilibrado, respeitando os limites do usuário e incentivando o autoconhecimento.

Requisitos do Sistema:

1.O sistema não deve permitir o cadastro de um usuário com e-mail duplicado.
(A coluna email na tabela usuario possui a restrição UNIQUE.)


2.O sistema deve garantir que o nível de energia do usuário, ao ser cadastrado, esteja sempre entre 0 e 100.
(A coluna energia na tabela usuario tem a restrição CHECK (energia BETWEEN 0 AND 100).)

3.O sistema deve garantir que a prioridade de uma tarefa seja definida em uma escala de 1 a 5. (antigo requisito 11)
(A coluna prioridade na tabela tarefa tem a restrição CHECK (prioridade BETWEEN 1 AND 5).

4.O sistema não deve permitir o cadastro de tarefas com título inferior a 5 caracteres. (antigo requisito 9)
A coluna titulo na tabela tarefa possui a restrição CHECK (char_length(titulo) >= 5).

5.O sistema não deve permitir registrar tarefas com tempo estimado fora do intervalo de 5 a 240 minutos. (antigo requisito 8)
A coluna tempo_estimado na tabela tarefa tem a restrição CHECK (tempo_estimado BETWEEN 5 AND 240).

6.O sistema deve permitir que o usuário registre o nível de satisfação pós-tarefa em uma escala de 1 a 5.
A coluna nivel_satisfacao_pos_tarefa na tabela tarefa tem a restrição CHECK (nivel_satisfacao_pos_tarefa BETWEEN 1 AND 5).


7.O sistema deve permitir ao usuário classificar tarefas como "motivadoras", "neutras" ou "desgastantes" após sua execução. (antigo requisito 12)
A coluna classificacao_pos_tarefa utiliza um ENUM com exatamente esses três valores (motivadora, neutra, desgastante).

8.O sistema deve permitir ao usuário registrar seu humor diário, escolhendo entre as opções: 'Terrível', 'Ruim', 'Neutro(a)', 'Bom/Boa', 'Ótimo(a)'.
A coluna humor na tabela usuario é do tipo humor_enum, que contém essas opções.

9.O sistema deve permitir que o usuário marque dias específicos como "inativos", informando um motivo. (antigo requisito 15)
Existe uma tabela dia_inativo dedicada para isso, que se relaciona com o usuário e armazena uma data e um motivo.

10.O sistema deve permitir que todas as entidades principais (Usuário, Tarefa, Histórico, Notificação, Dia Inativo, Agenda) sejam criadas (POST), lidas (GET), atualizadas (PUT) e deletadas (DELETE) -> (CRUD).

11.O sistema deve associar cada tarefa criada a um usuário existente.
 A tabela tarefa tem uma chave estrangeira usuario_id que referencia a tabela usuario.

12.O sistema deve registrar a data e hora de início e fim para cada tarefa agendada.
A tabela agenda_tarefa possui os campos data, hora_inicio e hora_fim, todos definidos como NOT NULL.

*Os demais requisitos antigos (1, 2, 3, 4, 5, 6, 9, 12, 13, 15, 16) são mais complexos e não estão implementados no meu código atual desse projeto para a matéria de PAV, e foram substituídos por esse atuais que já estão contemplados no código do projeto
