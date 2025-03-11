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
                sh 'pytest --junitxml=test-results.xml'
            }
        }
    }
    post {
        always {
            junit 'test-results.xml'
        }
        success {
            archiveArtifacts artifacts: 'dist/*.whl', fingerprint: true
            sh 'python -m build'
        }
    }
}