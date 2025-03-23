pipeline {
    agent any

    environment {
        IMAGE_NAME = "anuj1410/studentproject:latest"
        DOCKER_HOST = "unix:///var/run/docker.sock"
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
                    def dockerImage = docker.build("${env.IMAGE_NAME}", "-f Dockerfile .")
                }
            }
        }

        
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-login1410') {
                        def dockerImage = docker.image("${env.IMAGE_NAME}")
                        dockerImage.push()
                    }
                }
            }
        }

    }
}
