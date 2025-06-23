pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Fazer checkout do código do repositório
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Comandos para construir o projeto
                sh 'echo "Building the project"'
                // Exemplo: sh 'mvn clean package'
            }
        }

        stage('Test') {
            steps {
                // Comandos para executar testes
                sh 'echo "Running tests"'
                // Exemplo: sh 'mvn test'
            }
        }

        stage('Deploy') {
            steps {
                // Comandos para implantar o projeto
                sh 'echo "Deploying the project"'
                // Exemplo: sh 'docker build -t myapp .'
                // Exemplo: sh 'docker push myapp:latest'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executado com sucesso!'
        }
        failure {
            echo 'Pipeline falhou.'
        }
    }
}
