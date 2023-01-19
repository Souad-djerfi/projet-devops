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
            sh "docker build -t flask-app ./python "
            sh "docker tag flask-app souaddjerfi/flask-app:$BUILD_NUMBER"
                                  
          }
        } 
      }

      stage('push image')
      {
        steps
        {
          script 
          { 
            
            docker.withRegistry( '', registryCredential )
            {
              sh "docker push souaddjerfi/flask-app:$BUILD_NUMBER"
             
            }
             
            
          }
        } 
      }
  } 
}