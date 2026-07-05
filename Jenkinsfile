pipeline {
    agent any

    environment {
        IMAGE_NAME = "oviyamuralidharan/simple-python-app:latest"
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
                    bat 'mvn clean verify sonar:sonar'
                }
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([string(credentialsId: 'docker-token', variable: 'DOCKER_PASS')]) {
                    bat 'docker login -u oviyamuralidharan -p %DOCKER_PASS%'
                    bat 'docker push %IMAGE_NAME%'
                }
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker rm -f simple-python-app || exit 0'
                bat 'docker run -d --name simple-python-app -p 5000:5000 %IMAGE_NAME%'
            }
        }
    }
}
