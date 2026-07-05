pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat '"C:\\Users\\Oviya\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" --version'
                bat '"C:\\Users\\Oviya\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                bat '"C:\\Users\\Oviya\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" test.py'
            }
        }
    }
}
