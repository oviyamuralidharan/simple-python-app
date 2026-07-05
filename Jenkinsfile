pipeline {
    agent any

    tools {
        sonarRunner 'sonar-scanner'
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
                    bat 'sonar-scanner -Dsonar.login=%SONAR_TOKEN%'
                }
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
