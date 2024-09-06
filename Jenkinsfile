pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'latest' // Имя Docker-образа
        REPO_URL = 'https://github.com/Kovalenkolex/For_Jenkins.git' // URL твоего репозитория
        BRANCH_NAME = 'dev' // Ветка, с которой будем работать
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: "${BRANCH_NAME}", url: "${REPO_URL}"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh '''
                    docker stop myapp || true
                    docker rm myapp || true
                    docker run -d --name myapp -p 80:80 ${DOCKER_IMAGE}
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Очистка рабочей директории после сборки
        }
    }
}
