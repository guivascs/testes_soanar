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

        stage('Checkout Aplicação') {
            steps {
                git credentialsId: 'GITHUB', url: 'https://github.com/guivascs/Python-base'
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