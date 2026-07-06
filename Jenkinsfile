pipeline {
    agent any

    stages {

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
                    withEnv(["PATH+SONAR=C:\\ProgramData\\Jenkins\\.jenkins\\tools\\hudson.plugins.sonar.SonarRunnerInstallation\\sonar-scanner\\bin"]) {
                        bat '''
                        sonar-scanner ^
                        -Dsonar.host.url=http://3.110.203.101 ^
                        -Dsonar.login=%SONAR_AUTH_TOKEN%
                        '''
                    }
                }
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t simple-python-app .'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker rm -f simple-python-app || exit 0'
                bat 'docker run -d --name simple-python-app -p 5000:5000 simple-python-app'
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
