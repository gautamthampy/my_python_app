pipeline {
    agent {
        docker { image 'python:3.13.2-alpine3.21' }
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'mkdir -p test-reports'
                sh 'pytest --junitxml=test-reports/test-results.xml'
            }
        }
    }
    post {
        always {
            junit allowEmptyResults: true, testResults: 'test-reports/*.xml'
        }
    }
}