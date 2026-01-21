pipeline {
    agent any

    tools {
        maven 'Maven_3'
        jdk 'JDK_17'   // optional but recommended
    }

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'mvn clean install -DskipTests'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'mvn test'
            }
        }
    }
}
