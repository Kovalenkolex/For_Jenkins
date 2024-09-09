pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'justbot_image' // Имя Docker-образа
        REPO_URL = 'https://github.com/Kovalenkolex/For_Jenkins.git' // URL твоего репозитория
        BRANCH_NAME = 'dev' // Ветка, с которой будем работать
        PROJECT_DIR = '/home/ansible/justbot/'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git clone -b "${BRANCH_NAME}" "${REPO_URL}" "${PROJECT_DIR}"//git branch: "${BRANCH_NAME}", url: "${REPO_URL}"
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
                    docker stop justbot || true
                    docker rm justbot || true
                    docker run --restart unless-stopped -d --name justbot -p 80:80 ${DOCKER_IMAGE}
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
