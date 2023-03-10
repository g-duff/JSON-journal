@Library('pipeline-lib') _

pipeline {
	
	agent { label 'python' }
	
	stages {
		stage('Install dependencies') {
			steps {
				sh "make dev_dependencies"
			}
		}
		stage('Lint') {
			steps {
				script {
					try {
						sh "make lint"
					} catch (error) {
						unstable(message: "${STAGE_NAME} is unstable")
					}
				}
			}
		}
		stage('Test') { 
			steps {
				script {
					try {
						sh "make test"
					} catch (error) {
						unstable(message: "${STAGE_NAME} is unstable")
					}
				}
			}
		}
	}

	post {

		always {
			sh "make clean"
		}

		success {
			script {
				notifyGitHubBuildStatus("JSON-journal", "success")
			}
		}

		unstable {
			script {
				notifyGitHubBuildStatus("JSON-journal", "failure")
			}
		}

		failure {
			script {
				notifyGitHubBuildStatus("JSON-journal", "error")
			}
		}

	}
}
