pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'justbot_image' // Имя Docker-образа
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
                    sh 'docker build -t justbot_image .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh '''
                    docker stop justbot || true
                    docker rm justbot || true
                    docker run --restart unless-stopped -d --name justbot -p 80:80 justbot_image
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
