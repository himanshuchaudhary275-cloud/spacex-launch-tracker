pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t spacex-launch-tracker .
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                # Remove existing container if it exists
                docker rm -f spacex-launch || true

                # Run new container
                docker run -d \
                  --restart unless-stopped \
                  -p 5000:5000 \
                  --name spacex-launch \
                  spacex-launch-tracker
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful!'
        }
        failure {
            echo '❌ Deployment failed. Check logs.'
        }
    }
}