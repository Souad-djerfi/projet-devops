pipeline {
  environment {
    githup = "./python"
    registry = "souaddjerfi/flask-app"
    registryCredential = 'dockerhub-id'
    dockerImage = ''
}
  agent any
  stages {
    stage('Building image') {
      steps{
        script { 
          dockerImage = sh "docker build -t flask-app ./python" 
          //dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      } 
    }
    stage('deploye our image'){
      steps {
        script{
          sh "docker tag flask-app $registry"
          sh "docker image push flask-app "
        }
      }
    }
  } 
}