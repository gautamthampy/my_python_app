pipeline {
    agent {
        docker { image 'python:3.13.2-alpine3.21' }
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install pytest'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'mkdir -p test-reports'
                sh 'python -m pytest --junitxml=test-reports/test-results.xml || true'
            }
        }
    }
    post {
        always {
            junit allowEmptyResults: true, testResults: 'test-reports/*.xml'
        }
        failure {
            mail to: 'gautamsanthanu.thampy@sjsu.edu',
                 subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                 body: "Something is wrong with ${env.BUILD_URL}"
        }
    }
}