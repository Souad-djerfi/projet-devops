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
            sh "docker buildx build -t flask-app --load ./python "
            sh "docker tag flask-app souaddjerfi/flask-app:$BUILD_NUMBER"
            dockerImage="flask-app:$BUILD_NUMBER"
                      
            docker.withRegistry( '', registryCredential )
            {
              sh "docker push souaddjerfi/flask-app:$BUILD_NUMBER"
             
            }
    
          }
        } 
      }
    
  } 
}