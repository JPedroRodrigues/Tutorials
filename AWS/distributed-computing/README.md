# How-to: Como Configurar um Cluster na AWS: Múltiplas Instâncias de EC2

### Sumário

## First Things First

Ao entrar no ambiente de aprendizado da AWS, vá até a seção de módulos e dirija-se até o botão "Iniciar os laboratórios de aprendizagem da AWS Academy". Ao clicar, você será direcionado ao terminal básico da AWS. Pressione o botão *Start Lab*, no canto superior direito, e espere até o ícone verde à mesma altura, no canto superior esquerdo, mudar a cor para verde.

![home page](./assets/aws-pagina-inicial.png)
![selecionar modulo](./assets/aws-selecionar-modulo.png)
![terminal aws](./assets/aws-terminal-aws.png)

Após isso, basta clicar neste mesmo ícone verde.
![botão-verde](./assets/aws-verde.png)

## Criando Instâncias EC2

### Instância Master

Ao entrar no console da AWS, não perca tempo e vá direto à barra de pesquisa. Busque por EC2 e clique na primeira opção, de mesmo nome, e, no painel, clique em Launch Instance.

![search ec2](./assets/aws-search-ec2.png)
![launch instance](./assets/launch-ec2.png)

Para configurar a instância, basta seguir estas configurações:
- Application and OS Images: Ubuntu

![choose os](./assets/choose-os.png)

- Instance Type: t2.micro

![select instance type](./assets/instance-type.png)

- Key pair (login):
  - Clique em *Create new key pair*
  - Dê um nome para a chave
  - Mantenha RSA e .pem selecionados. Trata-se de uma chave simétrica, em que quem tiver acesso ao arquivo, terá também acesso irrestrito às máquinas. Por este motivo, tome cuidado, guarde o arquivo em um lugar seguro.
  - Após a geração da chave, selecione-a no campo *Key pair name*

![create a .pem key](./assets/pem-key.png)

Antes de concluir essa etapa, abra em uma nova janela o *cloud shell* da AWS, que está situado no canto superior direito (mais para o centro), com um ícone clássico de shell.

![cloud shell icon](./assets/cloud-shell.png)

Após abri-lo, basta ir em: Actions -> Upload File -> Carregue o arquivo `.pem` recém-criado e baixado por você. Este arquivo será fundamental para o estabelecimento da conexão entre as instâncias

- Network Settings: Clique em *Create security group*

Feito isso, basta clicar em *Launch instance*, concluindo, assim, a criação da primeira instância.

### Instâncias Workers

Antes de mais nada, ao voltar à listagem de instâncias, verá a recém-criada instância mestre
