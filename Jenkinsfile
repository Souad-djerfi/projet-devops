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
    /*stage('Build') 
      {
          steps 
          {
              echo "Running ${VERSION} on ${env.JENKINS_URL}"
              git branch: "${BRANCH}",  .....
              echo "for brnach ${env.BRANCH_NAME}"
              sh "docker build -t ${NAME} ."
              sh "docker tag ${NAME}:latest ${IMAGE_REPO}/${NAME}:${VERSION}"
          }
      }*/
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
            sh "docker tag flask-app souaddjerfi/flask-app:$BUILD_NUMBER"
            dockerImage="flask-app:$BUILD_NUMBER"
            echo " coucoucoucoucoucou" + dockerImage 
            sh "docker push souaddjerfi/flask-app:$BUILD_NUMBER"
            /*docker.withRegistry( '', registryCredential )
            {
              echo "je suis dans registrycredential"
            dockerImage.push()  
             echo " le push marche "
            }*/
    
          }
        } 
      }
    /*stage('deploye our image')
      {
        steps 
        {
          script
          {
            //
            docker.withRegistry( '', registryCredential )
            {
              //sh "docker image push flask-app "
              dockerImage.push()

            }
          }
        }
      } */
  } 
}