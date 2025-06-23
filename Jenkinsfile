// Define uma variável global para armazenar a lista de servidores
def servers

pipeline {
    // Especifica que o pipeline pode ser executado em qualquer agente disponível
    agent any

    stages {
        // Estágio para fazer o checkout do código
        stage('Checkout') {
            steps {
                // Faz o checkout do código do repositório configurado no job
                checkout scm
            }
        }

        // Estágio para carregar a lista de servidores do arquivo JSON
        stage('Load Server List') {
            steps {
                script {
                    // Lê o conteúdo do arquivo servers.json e o converte para um objeto Groovy
                    def serverConfig = readJSON file: 'servers.json'
                    // Atribui a lista de servidores do arquivo JSON à variável global 'servers'
                    servers = serverConfig.servers
                }
            }
        }

        // Estágio para realizar o deploy
        stage('Deploy') {
            steps {
                script {
                    // Itera sobre cada servidor na lista
                    servers.each { server ->
                        // Imprime uma mensagem indicando o servidor atual
                        echo "Deploying to ${server}"
                        // Aqui você adicionaria seus comandos de deploy específicos
                        // Por exemplo:
                        // sh "scp -r app/ user@${server}:/path/to/deploy"
                        // sh "ssh user@${server} 'cd /path/to/deploy && ./restart-service.sh'"
                    }
                }
            }
        }
    }
}