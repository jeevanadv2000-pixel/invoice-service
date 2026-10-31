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
        buildDiscarder(logRotator(numToKeepStr: '10'))
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
        }

        stage('Package') {
            steps {
                echo "Release Notes: ${params.RELEASE_NOTES}"
                sh 'mvn package'
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'target/*.war', fingerprint: true
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                curl --fail \
                -u jenkins:JenkinsTomcat123! \
                --upload-file target/invoice-service.war \
                "http://localhost:9090/manager/text/deploy?path=/invoice-service&update=true"
                '''
            }
        }

        stage('Verify') {
            steps {
                sh '''
                curl --fail http://localhost:9090/invoice-service/
                '''
            }
        }
    }

    post {

        success {
            echo "SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
        }

        failure {
            echo "FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
        }

        fixed {
            echo "FIXED: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
        }
    }
}
