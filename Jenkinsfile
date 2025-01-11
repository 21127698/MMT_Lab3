pipeline {
    agent any

    stages {
        stage('Git stage') {
            steps {
                git branch: 'main', credentialsId: 'docker-hub', url: 'https://github.com/21127698/MMT_Lab3.git'
                
            }
        }
        stage('Build') {
            steps {
                withDockerRegistry(credentialsId: 'docker-hub', url: 'https://index.docker.io/v1/') {
                    // some block
                    sh 'docker build -t 21127698/lab3 .'
                }
                
            }
        
        }
        
        stage('Push') {
                    steps {
                        withDockerRegistry(credentialsId: 'docker-hub', url: 'https://index.docker.io/v1/') {
                            // some block
                            sh 'docker push-t 21127698/lab3 .'
                        }
                    }
        }   
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 21127698/lab3'
            }
        }
    }
}