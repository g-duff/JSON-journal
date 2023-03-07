pipeline {
	agent {
		docker { image 'python:slim-bullseye' }
	}
	environment {
		HOME="${env.WORKSPACE}"
	}
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
