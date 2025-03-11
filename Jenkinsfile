/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.11-alpine' } }
    
    stages {
        stage('Setup') {
            steps {
                sh 'python --version'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Lint') {
            steps {
                sh 'flake8 my_app tests'
            }
        }
        
        stage('Test') {
            steps {
                sh 'pytest --junitxml=test-reports/junit.xml --cov=my_app --cov-report=xml tests/'
            }
        }
        
        stage('Build') {
            steps {
                sh 'python -m build'
            }
        }
    }
    
    post {
        always {
            // Create the test-reports directory if it doesn't exist
            sh 'mkdir -p test-reports'
            
            // Archive the test reports and coverage data
            junit allowEmptyResults: true, testResults: 'test-reports/*.xml'
            
            // Only run if we have the Coverage plugin installed
            script {
                if (fileExists('coverage.xml')) {
                    echo 'Publishing coverage report...'
                    // You'll need the "Coverage" plugin installed for this to work
                    // publishCoverage adapters: [cobertura('coverage.xml')]
                }
            }
            
            // Archive the built packages
            archiveArtifacts artifacts: 'dist/*', allowEmptyArchive: true
        }
        success {
            echo 'Success! The pipeline has completed successfully.'
        }
        failure {
            echo 'Failed! The pipeline has encountered an error.'
        }
    }
}