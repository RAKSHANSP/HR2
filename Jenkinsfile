pipeline {
    agent any

    environment {
        SONAR_SCANNER = tool 'sonar-scanner'
    }

    stages {

        // =========================
        // SONARQUBE ANALYSIS
        // =========================
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar-local') {
                    withCredentials([string(credentialsId: 'sonar-token1', variable: 'SONAR_TOKEN')]) {
                        bat """
                        %SONAR_SCANNER%\\bin\\sonar-scanner ^
                        -Dsonar.projectKey=hr2-project ^
                        -Dsonar.sources=. ^
                        -Dsonar.host.url=http://localhost:9000 ^
                        -Dsonar.token=%SONAR_TOKEN%
                        """
                    }
                }
            }
        }

        // =========================
        // QUALITY GATE
        // =========================
        stage('Quality Gate Check') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        // =========================
        // JUNIT TESTING (ML READY)
        // =========================
        stage('JUnit Testing') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'pytest tests/ --junitxml=reports/test-results.xml'
            }

            post {
                always {
                    junit 'reports/test-results.xml'
                }
            }
        }

        // =========================
        // DOCKER BUILD
        // =========================
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t hr2-app:latest -f docker/Dockerfile .'
            }
        }

        // =========================
        // RUN CONTAINER
        // =========================
        stage('Run Container') {
            steps {
                bat 'docker stop hr2-container || exit 0'
                bat 'docker rm hr2-container || exit 0'
                bat 'docker run -d -p 8501:8501 --name hr2-container hr2-app'
            }
        }

        // =========================
        // GITOPS (ARGOCD TRIGGER)
        // =========================
        stage('GitOps - Deploy to Kubernetes Repo') {
            steps {
                bat """
                echo Updating Kubernetes manifests for ArgoCD...

                cd kubernetes

                git add .
                git commit -m "Updated deployment from Jenkins build %BUILD_NUMBER%" || exit 0
                git push origin main
                """
            }
        }
    }

    post {
        success {
            echo "Pipeline Success 🚀"
        }
        failure {
            echo "Pipeline Failed ❌ Check logs"
        }
    }
}