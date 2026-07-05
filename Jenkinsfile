pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'python --version'
                bat 'python app.py'
            }
        }

        stage('Test') {
            steps {
                bat 'python test.py'
            }
        }
    }
}
