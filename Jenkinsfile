pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "anuj1410/studentproject:latest"
        DJANGO_SETTINGS_MODULE = "core.settings"
        CONDA_PATH = "C:/Softwares/ANNA"
    }

    stages {
        stage('Setup Environment') {
            steps {
                sh '''
                    source $CONDA_PATH/Scripts/activate base
                    python --version
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                sh '''
                    source $CONDA_PATH/Scripts/activate base
                    python manage.py makemigrations
                    python manage.py migrate
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source $CONDA_PATH/Scripts/activate base
                    python manage.py test
                '''
            }
        }

        stage('Collect Static Files') {
            steps {
                sh '''
                    source $CONDA_PATH/Scripts/activate base
                    python manage.py collectstatic --noinput
                '''
            }
        }

        stage('Build and Push') {
            steps {
                script {
                    sh '''
                        echo "$Anujagr1410#?" | docker login -u "$anuj1410" --password-stdin
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


