pipeline {
    environment {
        registry = 'afarizahalim'
        imageFlask = 'flask-app'
        imageDB = 'mysql-db'
        registryCredential = 'dockerhub_id'
        dockerImage = ''
    }
    agent any
    stages {
        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarqubeScanner'
                    withSonarQubeEnv() {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }
        stage('Building our image') {
            steps {
                script {
                    sh "docker build -t $imageFlask ./python "
                    sh "docker build -t $imageDB ./database "
                }
            }
        }
        stage('Deploy our image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
    
                        sh "docker tag $imageFlask $registry/$imageFlask:$BUILD_NUMBER" 
                        sh "docker tag $imageFlask $registry/$imageFlask:latest"                               
                        sh "docker push $registry/$imageFlask:$BUILD_NUMBER"
                        sh "docker push $registry/$imageFlask:latest"

                        sh "docker tag $imageDB $registry/$imageDB:$BUILD_NUMBER" 
                        sh "docker tag $imageDB $registry/$imageDB:latest"                               
                        sh "docker push $registry/$imageDB:$BUILD_NUMBER"
                        sh "docker push $registry/$imageDB:latest"

                    }
                }
            }
        }
        stage('Run docker-compose') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        sh "docker-compose build -d"
                    }
                }
            }
        }
        // stage('Cleaning up') {
        //     steps {
        //         sh "docker rmi $registry/$imageFlask:$BUILD_NUMBER"
        //         //sh "docker rmi $registry/$imageFlask:latest"
        //     }
        // }
    }
}