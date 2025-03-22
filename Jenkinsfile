pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "anuj1410/studentproject:latest"
        DJANGO_SETTINGS_MODULE = "core.settings"
    }

    stages {
        stage('Setup Environment') {
            steps {
                script {
                    sh '''
                        python --version
                        python -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Migrations') {
            steps {
                script {
                    sh '''
                        . venv/bin/activate
                        python manage.py makemigrations
                        python manage.py migrate
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '''
                        . venv/bin/activate
                        python manage.py test
                    '''
                }
            }
        }

        stage('Collect Static Files') {
            steps {
                script {
                    sh '''
                        . venv/bin/activate
                        python manage.py collectstatic --noinput
                    '''
                }
            }
        }

        stage('Build and Push') {
            steps {
                script {
                    sh '''
                        echo "Anujagr1410#?" | docker login -u "anuj1410" --password-stdin
                        docker build -t ${DOCKER_IMAGE} .
                        docker push ${DOCKER_IMAGE}
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded! Docker image pushed to registry.'
        }
        failure {
            echo 'Pipeline failed! Check logs for details.'
        }
    }
}
