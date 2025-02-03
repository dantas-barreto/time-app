pipeline {
    agent any
    environment {
        IMAGE_NAME = 'time-app'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/dantas-barreto/time-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }
        stage('Run Script') {
            steps {
                script {
                    sh 'docker run --rm ${IMAGE_NAME}'
                }
            }

        }
    }
}

