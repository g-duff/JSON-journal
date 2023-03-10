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
				sh "make lint"
			}
		}
		stage('Test') { 
			steps {
				sh "make test"
			}
		}
	}

	post {

		success {
			withCredentials([string(credentialsId: 'GitHubStatusToken', variable: 'TOKEN')]) {
				sh '''curl -L \
					-X POST \
					-H "Accept: application/vnd.github+json" \
					-H "X-GitHub-Api-Version: 2022-11-28" \
					"https://api.github.com/repos/g-duff/JSON-journal/statuses/$GIT_COMMIT" \
					-H "Authorization: Bearer $TOKEN"\
					-d '{"state":"success","context":"continuous-integration/jenkins"}'
					'''
			}
		}

		failure {
			withCredentials([string(credentialsId: 'GitHubStatusToken', variable: 'TOKEN')]) {
				sh '''curl -L \
					-X POST \
					-H "Accept: application/vnd.github+json" \
					-H "X-GitHub-Api-Version: 2022-11-28" \
					"https://api.github.com/repos/g-duff/JSON-journal/statuses/$GIT_COMMIT" \
					-H "Authorization: Bearer $TOKEN"\
					-d '{"state":"failure","context":"continuous-integration/jenkins"}'
					'''
			}
		}

	}
}
