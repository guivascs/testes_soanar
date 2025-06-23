// Define uma variável global para armazenar a lista de servidores
def servers

pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {

                checkout scm
            }
        }


        stage('Load Server List') {
            steps {
                script {
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
                        echo "Deploying to ${server}"

                    }
                }
            }
        }
    }
}