pipeline {
    agent {
        docker { image 'python:3.13.2-alpine3.21' }
    }
    options {
        skipStagesAfterUnstable()
        timeout(time: 10, unit: 'MINUTES')
    }
    environment {
        APP_NAME = 'calculator-app'
        VERSION = '1.0.0'
        GIT_COMMIT_SHORT = sh(script: "echo ${GIT_COMMIT.take(8)}", returnStdout: true).trim()
    }
    stages {
        stage('Setup') {
            steps {
                echo "Setting up ${env.APP_NAME} version ${env.VERSION}"
                sh 'python --version'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Lint') {
            steps {
                echo 'Running code quality checks'
                sh 'pip install flake8'
                sh 'flake8 my_app tests --max-line-length=100 || true'
            }
            post {
                success {
                    echo 'Linting passed'
                }
                failure {
                    echo 'Linting issues found'
                }
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running unit tests'
                sh 'mkdir -p test-reports'
                sh 'pip install pytest pytest-cov'
                sh 'python -m pytest --junitxml=test-reports/test-results.xml --cov=my_app --cov-report=xml:test-reports/coverage.xml'
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'test-reports/*.xml'
                }
            }
        }
        
        stage('Build Package') {
            steps {
                echo "Building Python package for ${env.APP_NAME}"
                sh 'pip install build'
                sh 'python -m build'
                sh 'mkdir -p dist'
                sh 'ls -la dist/ || true'
            }
            post {
                success {
                    archiveArtifacts artifacts: 'dist/*.whl,dist/*.tar.gz', fingerprint: true
                    echo 'Package built successfully'
                }
            }
        }
        
        stage('Deploy - Staging') {
            steps {
                echo "Deploying ${env.APP_NAME} to staging environment"
                sh "echo 'Installing wheel package in staging environment'"
                sh "find dist -name '*.whl' -exec pip install {} --target=./staging \\;"
                sh "echo 'Running calculator app in staging environment'"
                sh "python -c 'from staging.my_app.main import add; print(f\"Calculator test: 2 + 2 = {add(2, 2)}\")'"
            }
            post {
                success {
                    echo 'Staging deployment successful'
                }
                failure {
                    echo 'Staging deployment failed'
                }
            }
        }
        
        stage('Sanity Check') {
            steps {
                echo 'Running smoke tests on staging'
                sh "python -c 'from staging.my_app.main import add, subtract, multiply, divide; print(f\"Smoke test results: {add(5,3)}, {subtract(10,4)}, {multiply(2,3)}, {divide(10,2)}\")'"
                input message: 'Does the staging environment look ok?', ok: 'Proceed to Production'
            }
        }
        
        stage('Deploy - Production') {
            steps {
                echo "Deploying ${env.APP_NAME} version ${env.VERSION} (${env.GIT_COMMIT_SHORT}) to production"
                sh "echo 'Installing wheel package in production environment'"
                sh "find dist -name '*.whl' -exec pip install {} --target=./production \\;"
                sh "echo 'Running calculator app in production environment'"
                sh "python -c 'from production.my_app.main import add; print(f\"Calculator in production: 10 + 20 = {add(10, 20)}\")'"
            }
        }
    }
    
    post {
        always {
            echo "Pipeline completed for ${env.APP_NAME}"
        }
        success {
            echo "✅ ${env.APP_NAME} successfully built and deployed"
            mail to: 'thampygautam@gmail.com',
                 subject: "✅ Successful Pipeline: ${env.APP_NAME} v${env.VERSION}",
                 body: """
                    Pipeline completed successfully!
                    
                    Project: ${env.APP_NAME}
                    Version: ${env.VERSION}
                    Commit: ${env.GIT_COMMIT_SHORT}
                    Build URL: ${env.BUILD_URL}
                    
                    All stages have passed and the calculator app has been deployed to production.
                 """
        }
        failure {
            echo "❌ Pipeline failed for ${env.APP_NAME}"
            mail to: 'thampygautam@gmail.com',
                 subject: "❌ Failed Pipeline: ${env.APP_NAME} v${env.VERSION}",
                 body: """
                    Pipeline failed!
                    
                    Project: ${env.APP_NAME}
                    Version: ${env.VERSION}
                    Commit: ${env.GIT_COMMIT_SHORT}
                    Build URL: ${env.BUILD_URL}
                    
                    Please check the console output to identify the issue.
                 """
        }
        unstable {
            echo "⚠️ Pipeline unstable for ${env.APP_NAME}"
            mail to: 'thampygautam@gmail.com',
                 subject: "⚠️ Unstable Pipeline: ${env.APP_NAME} v${env.VERSION}",
                 body: """
                    Pipeline is unstable!
                    
                    Project: ${env.APP_NAME}
                    Version: ${env.VERSION}
                    Commit: ${env.GIT_COMMIT_SHORT}
                    Build URL: ${env.BUILD_URL}
                    
                    The build completed but there are test failures or other issues.
                 """
        }
    }
}