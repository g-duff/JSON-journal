pipeline {
    agent any 
    stages {
        stage('Test') { 
            steps {
                sh "echo hello world"
            }
        }
    }
}
