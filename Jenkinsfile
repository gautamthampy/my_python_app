pipeline {
    agent {
        docker { image 'python:3.13.2-alpine3.21' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python -c "import platform; print(platform.machine(), platform.system().lower())"'
            }
        }
    }
}