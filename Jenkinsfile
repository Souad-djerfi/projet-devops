pipeline 
{
  environment 
  {
    //githup = "./python"
    registry = "souaddjerfi/flask-app"
    registryCredential = "dockerhub-id"
    dockerImage = ''
  }
  agent any
  stages 
  {
    stage('Building image')
     {
      steps
      {
        script 
        { 
          
          //sh "docker tag flask-app:$BUILD_NUMBER" 
                   
          //dockerImage = docker.build registry + ":$BUILD_NUMBER"
          //dockerImage=docker.build registry + ":$BUILD_NUMBER"
          sh "docker build -t flask-app ./python "
          dockerImage="flask-app:$BUILD_NUMBER"
          docker.withRegistry( '', registryCredential )
          {
           dockerImage.push()  
          }
   
        }
      } 
    }
    /*stage('deploye our image'){
      steps {
        script{
          //
          docker.withRegistry( '', registryCredential ){
            //sh "docker image push flask-app "
            dockerImage.push()

          }
          
        }
      }
    }*/
  } 
}