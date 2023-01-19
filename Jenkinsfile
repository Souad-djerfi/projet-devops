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
    
    /*stage('Building image flask-app')
      {
        steps
        {
          script 
          { 
            sh "docker build -t flask-app ./python "
            
          }
        } 
      }

      stage('push image flask-app')
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

      stage('Building image mysql-db')
      {
        steps
        {
          script 
          { 
            sh "docker build -t mysql-db ./database "
            
          }
        } 
      }

      stage('push image mysql-db')
      {
        steps
        {
          script 
          { 
            
            docker.withRegistry( '', registryCredential )
            {
              sh "docker tag mysql-db souaddjerfi/mysql-db:$BUILD_NUMBER"                                  
              sh "docker push souaddjerfi/mysql-db:$BUILD_NUMBER"
             
            }
          }
        } 
      }*/

      stage('run docker-compose')
      {
        steps
        {
           
            
            sh "docker-compose up -d"
             
                     
          
        } 
      }
  } 
}