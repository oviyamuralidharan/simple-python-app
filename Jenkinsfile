pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\Oviya\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
        IMAGE_NAME = 'oviyamuralidharan/simple-python-app'
        IMAGE_TAG = 'latest'
    }

    stages {

        stage('Build') {
            steps {
                bat '"%PYTHON%" -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                bat '"%PYTHON%" test.py'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-token', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASS%'
                    bat 'docker push %IMAGE_NAME%:%IMAGE_TAG%'
                }
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker rm -f simple-python-app || exit 0'
                bat 'docker run -d --name simple-python-app -p 5000:5000 %IMAGE_NAME%:%IMAGE_TAG%'
            }
        }
    }
}
    }
}
