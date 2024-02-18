node('docker-agent-alpine') {
    // Define your Git credentials ID (configured in Jenkins)
    def gitCredentialsId = '94b3e0b8-6217-47a1-815e-bff2fc6c2545'

    stage('Checkout') {
        // Checkout code from Git repository using credentials
        checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[credentialsId: gitCredentialsId , url: 'https://github.com/aman1011/superprof-chris.git']]])
    }

    stage('Build') {
        // Add your build steps here
        // For example, you might use Maven, Gradle, or other build tools
        sh 'ls -a'
    }

    // Add more stages for additional steps (testing, deployment, etc.)

    try {
        // Actions to be performed if the build is successful
        echo 'Build successful!'
    } catch (Exception e) {
        // Actions to be performed if the build fails
        echo 'Build failed!'
    }
}
