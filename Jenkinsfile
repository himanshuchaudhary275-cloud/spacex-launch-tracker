pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/himanshuchaudhary275-cloud/spacex-launch-tracker.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t spacex-launch-tracker .'
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                docker rm -f spacex-launch || true
                docker run -d \
                    --restart always \
                    -p 5000:5000 \
                    --name spacex-launch \
                    spacex-launch-tracker
                '''
            }
        }

    }
}