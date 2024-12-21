# Use the official SonarQube image as a base
FROM sonarqube:latest


# Optionally, you can add custom plugins or extensions
# COPY ./sonar-extensions/* /opt/sonarqube/extensions/

# Expose the port SonarQube will run on
EXPOSE 9000

# Define the default command to run SonarQube
CMD ["bin/sonar.sh", "start"]
