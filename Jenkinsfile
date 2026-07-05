pipeline {
    agent any

    tools {
        // Make sure Python is installed on Jenkins machine
        // If not configured in Jenkins, we are directly calling python path in stages
    }

    environment {
        DOCKER_IMAGE = "oviyamuralidharan/simple-python-app:latest"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/oviyamuralidharan/simple-python-app.git'
            }
        }

        stage('Build') {
            steps {
                bat '"C:\\Users\\Oviya\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                bat '"C:\\Users\\Oviya\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" test.py'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarserver') {
                    withEnv(["SONAR_SCANNER_OPTS=-Dsonar.scanner.skipJreProvisioning=true"]) {
                        bat 'sonar-scanner -X'
                    }
                }
            }
        }

        stage('Docker Build') {
            steps {
                bat "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([string(credentialsId: 'docker-token', variable: 'DOCKER_PASS')]) {
                    bat '''
                        docker login -u oviyamuralidharan -p %DOCKER_PASS%
                        docker push oviyamuralidharan/simple-python-app:latest
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                    docker rm -f simple-python-app || exit 0
                    docker run -d --name simple-python-app -p 5000:5000 oviyamuralidharan/simple-python-app:latest
                '''
            }
        }
    }

    post {
        success {
            echo 'PIPELINE SUCCESS ✅'
        }
        failure {
            echo 'PIPELINE FAILED ❌ Check logs'
        }
    }
}
