pipeline {
    agent any

    environment {
        SONAR_SCANNER = tool 'sonar-scanner'
    }

    stages {

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar-local') {
                    withCredentials([string(credentialsId: 'sonar-token1', variable: 'SONAR_TOKEN')]) {
                        bat """
                        %SONAR_SCANNER%\\bin\\sonar-scanner ^
                        -Dsonar.projectKey=hr2-project ^
                        -Dsonar.sources=. ^
                        -Dsonar.host.url=http://localhost:9000 ^
                        -Dsonar.login=%SONAR_TOKEN%
                        """
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t hr2-app -f docker/Dockerfile .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker stop hr2-container || exit 0'
                bat 'docker rm hr2-container || exit 0'
                bat 'docker run -d -p 8501:8501 --name hr2-container hr2-app'
            }
        }
    }
}