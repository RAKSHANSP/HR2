pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/RAKSHANSP/HR2.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t hr2-app -f docker/Dockerfile .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 8501:8501 hr2-app || exit 0'
            }
        }
    }
}