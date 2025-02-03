pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/dantas-barreto/time-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t time-app .'
            }
        }
        stage('Run Script') {
            steps {
                sh 'docker run --rm time-app'
            }
        }
    }
}

