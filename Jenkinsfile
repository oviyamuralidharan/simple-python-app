pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'py --version'
                bat 'py app.py'
            }
        }

        stage('Test') {
            steps {
                bat 'py test.py'
            }
        }
    }
}
