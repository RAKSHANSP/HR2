pipeline {
    agent any

    stages {

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