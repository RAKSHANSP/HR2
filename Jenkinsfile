pipeline {
    agent any

    environment {
        SONAR_SCANNER = tool 'sonar-scanner'
    }

    stages {

        // =========================
        // 1. SONARQUBE ANALYSIS
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
                        -Dsonar.login=%SONAR_TOKEN%
                        """
                    }
                }
            }
        }

        // =========================
        // 2. QUALITY GATE CHECK
        // =========================
        stage('Quality Gate Check') {
            steps {
                timeout(time: 2, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        // =========================
        // 3. JUNIT TESTING (ML TESTS)
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
        // 4. BUILD DOCKER IMAGE
        // =========================
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t hr2-app:latest -f docker/Dockerfile .'
            }
        }

        // =========================
        // 5. RUN CONTAINER
        // =========================
        stage('Run Container') {
            steps {
                bat 'docker stop hr2-container || exit 0'
                bat 'docker rm hr2-container || exit 0'
                bat 'docker run -d -p 8501:8501 --name hr2-container hr2-app'
            }
        }

        // =========================
        // 6. GITOPS (ARGOCD TRIGGER)
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

    // =========================
    // POST ACTIONS
    // =========================
    post {
        success {
            echo 'Pipeline completed successfully 🚀'
        }
        failure {
            echo 'Pipeline failed ❌ check logs'
        }
    }
}