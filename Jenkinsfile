pipeline {
  environment {
    //githup = "./python"
    registry = "souadDJERFI/nextcloud_dockerfile"
    registryCredential = "dockerhub-id"
    dockerImage = ''
}
  agent any
  stages {
    stage('Building image') {
      steps{
        script { 
          //dockerImage = sh "docker build -t flask-app ./python" 
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
          //dockerImage=docker.build("flask-app","./python/")  registry + ":$BUILD_NUMBER"

            /*docker.withRegistry( '', registryCredential ){
            dockerImage=docker.build("flask-app:$BUILD_NUMBER","./python")
            dockerImage.push()  

          }*/
   
        }
      } 
    }
    stage('deploye our image'){
      steps {
        script{
          //sh "docker tag flask-app $registry"
          docker.withRegistry( '', registryCredential ){
            //sh "docker image push flask-app "
            dockerImage.push()

          }
          
        }
      }
    }
  } 
}