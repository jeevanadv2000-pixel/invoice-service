pipeline {
    agent any

    tools {
        maven 'maven3'
    }

    environment {
        APP_NAME = 'invoice-service'
    }

    options {
        timeout(time: 15, unit: 'MINUTES')
    }

    parameters {
        string(
            name: 'RELEASE_NOTES',
            defaultValue: 'Initial Release',
            description: 'Release Notes'
        )
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Application: ${APP_NAME}"
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean compile'
            }
        }

        stage('Test') {
            steps {
                sh 'mvn test'
            }

            post {
                always {
                    junit '**/target/surefire-reports/*.xml'
                }
            }
        }

        stage('Package') {
            when {
                branch 'main'
            }

            steps {
                echo "Release Notes: ${params.RELEASE_NOTES}"
                sh 'mvn package'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }

        failure {
            echo 'Pipeline failed'
        }
    }
}
