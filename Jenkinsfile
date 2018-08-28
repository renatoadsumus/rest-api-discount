pipeline {
    agent any 
      
	parameters {
    choice(
        name: 'TipoDeploy',
        choices: "PrimeiroDeploy\nDeployRecorrente",
        description: 'Validacao e Deploy na AWS' 
		)
  	}

	  environment {
		  VERSAO_GIT = '$(git rev-parse HEAD | cut -c 1-10)'

	  }

    stages 
	{ 	

		stage('Build e Analise Codigo') { 
			steps {	
				slackSend (color: '#FFFF00', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")

               	hipchatSend (color: 'YELLOW', notify: true,
            	message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})"
          )			
				echo "Building aplicacao com Gradle"							
                sh "docker run --rm -v /opt/jenkins/workspace/deploy_app/:/codigo_da_aplicacao renatoadsumus/gradle:4.9"
               			  							
			}			
		}

		stage('Analise Log') { 
			steps {

				echo "Analisando Logs em busca de erro 500 e 503"	
			}

		}
		
		
		stage('Build Imagem Docker da Aplicacao') { 
			steps {			
				echo "####################################"
				echo "Gerando a Imagem Docker da Aplicacao"	
				echo "####################################"
                sh "docker build -t renatoadsumus/docker-spring-sample ."				
				echo "####################################"
				echo "SHA commit GITHUB:" + env.VERSAO_GIT
				echo "####################################"
				sh "docker tag renatoadsumus/docker-spring-sample renatoadsumus/docker-spring-sample:$VERSAO_GIT"				
				sh "docker login --username=renatoadsumus --password=${DOCKER_HUB_PASS}"
                echo "### EXECUTANDO PUSH DA IMAGEM GERADA ###"
                sh "docker push renatoadsumus/docker-spring-sample"   
				sh "docker push renatoadsumus/docker-spring-sample:$VERSAO_GIT" 
						
			}			
		}	        

       stage('Deploy - EB AWS') { 
			
			when {
              expression {
                currentBuild.result == null || currentBuild.result == 'SUCCESS' 
              }
            }
			steps {			
				echo "####################################"
				echo "Gerando a Imagem Docker da Aplicacao"	
				echo "####################################"               	
				 sh "docker run --rm -v /opt/jenkins/workspace/deploy_app/eb/:/opt/artefato_deploy -e AWS_ACCESS_KEY_ID='${AWS_ACCESS_KEY_ID}' -e AWS_SECRET_ACCESS_KEY='${AWS_SECRET_ACCESS_KEY}' -e VERSAO='${env.BUILD_ID}' -e OPCAO='${params.TipoDeploy}' renatoadsumus/aws_cli:2.0"
						
			}						
		}  	
	}

	post {
		
		always {
			cleanWs()
		}

		success {
      		slackSend (color: '#00FF00', message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")

      		hipchatSend (color: 'GREEN', notify: true,
          	message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})"
        )

  
    	}
	
		failure {
      		slackSend (color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")

      		hipchatSend (color: 'RED', notify: true,
          	message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})"
        	)     
    	}
	} 	

}