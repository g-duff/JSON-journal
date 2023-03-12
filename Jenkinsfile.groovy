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
			withCredentials([string(credentialsId: 'GitHubStatusToken', variable: 'TOKEN')]) {
				sh '''curl -L \
					-X POST \
					-H "Accept: application/vnd.github+json" \
					-H "X-GitHub-Api-Version: 2022-11-28" \
					"https://api.github.com/repos/g-duff/JSON-journal/statuses/$GIT_COMMIT" \
					-H "Authorization: Bearer $TOKEN"\
					-d '{\
						"state": "success", \
						"context": "continuous-integration/jenkins", \
						"target_url": "https://github.com/g-duff/Jenkins" \
					}'
					'''
			}
		}

		unstable {
				sh '''curl -L \
					-X POST \
					-H "Accept: application/vnd.github+json" \
					-H "X-GitHub-Api-Version: 2022-11-28" \
					"https://api.github.com/repos/g-duff/JSON-journal/statuses/$GIT_COMMIT" \
					-H "Authorization: Bearer $TOKEN"\
					-d '{\
						"state": "error", \
						"context": "continuous-integration/jenkins", \
						"target_url": "https://github.com/g-duff/Jenkins" \
					}'
					'''
		}

		failure {
			withCredentials([string(credentialsId: 'GitHubStatusToken', variable: 'TOKEN')]) {
				sh '''curl -L \
					-X POST \
					-H "Accept: application/vnd.github+json" \
					-H "X-GitHub-Api-Version: 2022-11-28" \
					"https://api.github.com/repos/g-duff/JSON-journal/statuses/$GIT_COMMIT" \
					-H "Authorization: Bearer $TOKEN"\
					-d '{\
						"state": "failure", \
						"context": "continuous-integration/jenkins", \
						"target_url": "https://github.com/g-duff/Jenkins" \
					}'
					'''
			}
		}

	}
}
