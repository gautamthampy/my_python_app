pipeline {
    agent {
        docker { image 'python:3.13.2-alpine3.21' }
    }
    options {
        skipStagesAfterUnstable()
        timeout(time: 5, unit: 'MINUTES')
    }
    environment {
        APP_NAME = 'calculator-app'
        VERSION = '1.0.0'
        // Use a local directory for pip installations
        PIP_TARGET = './pip_packages'
        PYTHONPATH = '$PYTHONPATH:./pip_packages'
    }
    stages {
        stage('Setup') {
            steps {
                echo "Setting up ${env.APP_NAME}"
                sh 'python --version'
                sh 'mkdir -p ${PIP_TARGET}'
                // Install dependencies with --no-cache-dir to save space and --user for permissions
                sh 'pip install --no-cache-dir --user -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running unit tests'
                sh 'mkdir -p test-reports'
                sh 'pip install --no-cache-dir --user pytest'
                sh 'python -m pytest --junitxml=test-reports/test-results.xml'
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'test-reports/*.xml'
                }
            }
        }
        
        stage('Build') {
            steps {
                echo "Building Python package"
                sh 'mkdir -p dist'
                sh 'pip install --no-cache-dir --user build'
                sh 'python -m build || echo "Build step completed with issues"'
            }
        }
        
        stage('Deploy - Staging') {
            steps {
                echo "Deploying to staging environment"
                sh 'python -c "from my_app.main import add; print(f\"2 + 2 = {add(2, 2)}\")"'
            }
        }
        
        stage('Deploy - Production') {
            steps {
                input message: 'Deploy to production?', ok: 'Yes'
                echo "Deploying to production environment"
            }
        }
    }
    
    post {
        always {
            echo "Pipeline completed"
        }
        success {
            mail to: 'thampygautam@gmail.com',
                 subject: "Successful Pipeline: ${env.APP_NAME}",
                 body: "Pipeline completed successfully! Build URL: ${env.BUILD_URL}"
        }
        failure {
            mail to: 'thampygautam@gmail.com',
                 subject: "Failed Pipeline: ${env.APP_NAME}",
                 body: "Pipeline failed! Build URL: ${env.BUILD_URL}"
        }
    }
}