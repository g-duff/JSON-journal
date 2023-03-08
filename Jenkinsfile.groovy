pipeline {
	
	agent { label 'main' }
	
	stages {
		stage('Build and test project') {
			agent { docker { image 'python:slim-bullseye' } }
			environment { HOME="${env.WORKSPACE}" }
			stages {
				stage('Install dependencies') {
					steps {
						sh "python3 -m pip install --user --no-cache-dir --requirement ./requirements/dev.txt"
					}
				}
				stage('Lint') {
					steps {
						sh "python3 -m pylint ./json_journal/*py ./tests/*py"
					}
				}
				stage('Test') { 
					steps {
						sh "python3 -m unittest discover ./tests/ 'test_*.py'"
					}
				}
			}
		}
	}

	post {

		success {
			withCredentials([string(credentialsId: 'GitHubStatusToken', variable: 'TOKEN')]) {
				sh '''curl -L \
					-X POST \
					-H "Accept: application/vnd.github+json" \
					-H "Authorization: Bearer $TOKEN"\
					-H "X-GitHub-Api-Version: 2022-11-28" \
					"https://api.github.com/repos/g-duff/JSON-journal/statuses/$GIT_COMMIT" \
					-d '{"state":"success","context":"continuous-integration/jenkins"}'
					'''
			}
		}

		failure {
			withCredentials([string(credentialsId: 'GitHubStatusToken', variable: 'TOKEN')]) {
				sh '''curl -L \
					-X POST \
					-H "Accept: application/vnd.github+json" \
					-H "Authorization: Bearer $TOKEN"\
					-H "X-GitHub-Api-Version: 2022-11-28" \
					"https://api.github.com/repos/g-duff/JSON-journal/statuses/$GIT_COMMIT" \
					-d '{"state":"failure","context":"continuous-integration/jenkins"}'
					'''
			}
		}

	}
}
