pipeline {
  environment {
    githup = "Souad-djerfi/"
    registry = "souaddjerfi/flask-app"
    registryCredential = 'dockerhub-id'
    dockerImage = ''
}
  agent any
  stages {
    stage('Building image') {
      steps{
        script { 
          sh "docker build -t testflask ./python"
          //dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      } 
    }
    stage('deploye our image'){
      steps {
        script{
          docker
        }
      }
    }
  } 
}