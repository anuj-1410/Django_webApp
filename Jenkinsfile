pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('2575e28b-9664-4255-aa2e-2ec05a134947')
        IMAGE_NAME = "anuj1410/studentproject:latest"
        DOCKER_HOST = "unix:///var/run/docker.sock"  // Using mounted Docker socket
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/anuj-1410/Django_webApp.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${env.IMAGE_NAME}", "-f Dockerfile .")
                }
            }
        }
        
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
