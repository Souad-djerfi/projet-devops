pipeline {
    environment {
        registry = 'afarizahalim'
        imageName = 'flask-app'
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
                    sh "docker build -t $imageName ./python "
                }
            }
        }
        stage('Deploy our image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
    
                        sh "docker tag $imageName $registry/$imageName:$BUILD_NUMBER" 
                        sh "docker tag $imageName $registry/$imageName:latest"                               
                        sh "docker push $registry/$imageName:$BUILD_NUMBER"
                        sh "docker push $registry/$imageName:latest"

                    }
                }
            }
        }
        // stage('Run our image') {
        //     steps {
        //         script {
        //             docker.withRegistry('', registryCredential) {
        //                 dockerImage.run()
        //             }
        //         }
        //     }
        // }
        // stage('Cleaning up') {
        //     steps {
        //         sh "docker rmi $registry/$imageName:$BUILD_NUMBER"
        //         //sh "docker rmi $registry/$imageName:latest"
        //     }
        // }
    }
}