# Simulador de formas de alocação de blocos lógicos
Criar uma simulador (aplicação computacional) que simule as estratégias para alocação de
blocos lógicos num sistema de arquivos. O objetivo é demonstrar o funcionamento dos três
principais mecanismos de alocação:
- Contígua
- Encadeada
- Indexada

O simulador deve ser informado o tamanho do disco, em relação ao número de blocos lógicos.
Pode-se determinar o tamanho máximo e mínimo suportado pelo simulador. Em seguida, o usuário
do simulador deve selecionar o mecanismo de alocação a ser utilizado. O simulador deve mostrar
visualmente os blocos lógicos como livres no disco.

Em seguida, permitir que o usuário do simulador crie e apague arquivos no disco. Na criação,
deve-se especificar o nome do arquivo e a quantidade de blocos lógicos que ele ocupa. Mostrar
visualmente no espaço dos blocos lógicos do disco os utilizados por cada arquivo. Cada arquivo
deve ter uma visualização diferenciada dos demais. Mostrar ainda a Tabela de alocação, contendo as
informações relevantes para cada mecanismo de alocação. No momento da exclusão de um arquivo,
o usuário deve informar o nome do arquivo. A cada inclusão ou alteração, a visualização dos blocos
no disco e a Tabela de alocação devem ser atualizadas.

Na visualização dos blocos lógicos com encadeamento ou indexação, pode-se optar por
selecionar um dos arquivos na Tabela para visualização com indicação dos blocos lógicos que
compõem o arquivo.

O simulador pode ser criado para ser executado em uma máquina, com sistema operacional
Linux de 64 bits. Pode-se ainda criar o simulador com interface Web, devendo-se criar uma página
para colocá-lo em funcionamento. O simulador deve vir acompanhado de uma instrução para seu
uso.
