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
              sh "docker tag flask-app souaddjerfi/flask-app:$BUILD_NUMBER"                                  
              sh "docker push souaddjerfi/flask-app:$BUILD_NUMBER"
             
            }
             
            
          }
        } 
      }

      stage('run image')
      {
        steps
        {
          script 
          { 
            
           docker.withRegistry( '', registryCredential )
            {
              sh "docker run --name flask-app souaddjerfi/flask-app:$BUILD_NUMBER"
             
            }
            
          }
        } 
      }
  } 
}