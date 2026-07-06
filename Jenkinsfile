pipeline {
    agent any

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
                    bat '''
                    sonar-scanner ^
                    -Dsonar.host.url=http://3.110.203.101
                    '''
                }
            }
        }

    post {
        success {
            echo "PIPELINE SUCCESS ✅"
        }
        failure {
            echo "PIPELINE FAILED ❌ Check logs"
        }
    }
}
