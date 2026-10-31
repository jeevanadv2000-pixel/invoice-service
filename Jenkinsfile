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
                withCredentials([
   
