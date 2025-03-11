pipeline {
    agent {
        docker { image 'python:3.13.2-alpine3.21' }
    }
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                echo 'Building the Calculator Application'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest'
                echo 'Running tests for the Calculator Application'
            }
        }
        stage('Deploy - Staging') {
            steps {
                echo 'Deploying application to staging environment'
                sh 'python -m build'
                echo 'Running smoke tests on the staging environment'
            }
        }
        stage('Sanity check') {
            steps {
                input "Does the staging environment look ok?"
            }
        }
        stage('Deploy - Production') {
            steps {
                echo 'Deploying application to production environment'
            }
        }
    }
    post {
        always {
            junit allowEmptyResults: true, testResults: 'test-reports/*.xml'
        }
        failure {
            mail to: 'thampygautam@gmail.com',
                 subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                 body: "Build failed: ${env.BUILD_URL}"
        }
    }
}