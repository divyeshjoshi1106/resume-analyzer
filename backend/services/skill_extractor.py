import re
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # services/
BACKEND_DIR = os.path.dirname(BASE_DIR)  # backend/

skills_path = os.path.join(BACKEND_DIR, "app", "data", "skills.json")

with open(skills_path, "r", encoding="utf-8") as f:
    SKILLS = json.load(f)

UNSAFE_SHORT_ALIASES = {"go", "c", "r", "js", "ts"}

DISPLAY_SKILLS = {
    "python": "Python",
    "java": "Java",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "c": "C",
    "c++": "C++",
    "c#": "C#",
    "go": "Go",
    "rust": "Rust",
    "php": "PHP",
    "ruby": "Ruby",
    "swift": "Swift",
    "kotlin": "Kotlin",
    "scala": "Scala",
    "r": "R",
    "html": "HTML",
    "css": "CSS",
    "sass": "Sass",
    "bootstrap": "Bootstrap",
    "tailwind css": "Tailwind CSS",
    "material ui": "Material UI",
    "jquery": "jQuery",
    "react": "React",
    "next.js": "Next.js",
    "vue.js": "Vue.js",
    "nuxt.js": "Nuxt.js",
    "angular": "Angular",
    "svelte": "Svelte",
    "redux": "Redux",
    "node.js": "Node.js",
    "express.js": "Express.js",
    "nestjs": "NestJS",
    "fastapi": "FastAPI",
    "django": "Django",
    "flask": "Flask",
    "spring boot": "Spring Boot",
    "hibernate": "Hibernate",
    "asp.net": "ASP.NET",
    "laravel": "Laravel",
    "symfony": "Symfony",
    "ruby on rails": "Ruby on Rails",
    "graphql": "GraphQL",
    "rest api": "REST API",
    "sql": "SQL",
    "mysql": "MySQL",
    "postgresql": "PostgreSQL",
    "sqlite": "SQLite",
    "microsoft sql server": "Microsoft SQL Server",
    "oracle database": "Oracle Database",
    "mongodb": "MongoDB",
    "redis": "Redis",
    "cassandra": "Cassandra",
    "dynamodb": "DynamoDB",
    "elasticsearch": "Elasticsearch",
    "firebase": "Firebase",
    "neo4j": "Neo4j",
    "aws": "AWS",
    "azure": "Azure",
    "gcp": "GCP",
    "ec2": "EC2",
    "s3": "S3",
    "lambda": "Lambda",
    "rds": "RDS",
    "cloudwatch": "CloudWatch",
    "iam": "IAM",
    "api gateway": "API Gateway",
    "azure functions": "Azure Functions",
    "azure devops": "Azure DevOps",
    "azure container registry": "Azure Container Registry",
    "azure container instances": "Azure Container Instances",
    "azure kubernetes service": "Azure Kubernetes Service",
    "google kubernetes engine": "Google Kubernetes Engine",
    "cloud run": "Cloud Run",
    "docker": "Docker",
    "docker compose": "Docker Compose",
    "kubernetes": "Kubernetes",
    "helm": "Helm",
    "terraform": "Terraform",
    "ansible": "Ansible",
    "jenkins": "Jenkins",
    "github actions": "GitHub Actions",
    "gitlab ci/cd": "GitLab CI/CD",
    "ci/cd": "CI/CD",
    "linux": "Linux",
    "nginx": "Nginx",
    "apache": "Apache",
    "prometheus": "Prometheus",
    "grafana": "Grafana",
    "elk stack": "ELK Stack",
    "splunk": "Splunk",
    "rabbitmq": "RabbitMQ",
    "kafka": "Kafka",
    "git": "Git",
    "github": "GitHub",
    "gitlab": "GitLab",
    "bitbucket": "Bitbucket",
    "jira": "Jira",
    "confluence": "Confluence",
    "postman": "Postman",
    "swagger": "Swagger",
    "selenium": "Selenium",
    "playwright": "Playwright",
    "cypress": "Cypress",
    "jest": "Jest",
    "pytest": "pytest",
    "junit": "JUnit",
    "maven": "Maven",
    "gradle": "Gradle",
    "npm": "npm",
    "yarn": "Yarn",
    "pnpm": "pnpm",
    "pandas": "Pandas",
    "numpy": "NumPy",
    "scikit-learn": "scikit-learn",
    "tensorflow": "TensorFlow",
    "pytorch": "PyTorch",
    "keras": "Keras",
    "opencv": "OpenCV",
    "nltk": "NLTK",
    "spacy": "spaCy",
    "xgboost": "XGBoost",
    "matplotlib": "Matplotlib",
    "seaborn": "Seaborn",
    "jupyter": "Jupyter",
    "microservices": "Microservices",
    "oop": "OOP",
    "data structures": "Data Structures",
    "algorithms": "Algorithms",
    "design patterns": "Design Patterns",
    "system design": "System Design",
    "agile": "Agile",
    "test automation": "Test Automation",
    "unit testing": "Unit Testing",
    "integration testing": "Integration Testing",
    "tdd": "TDD",
}


def extract_skills(text: str):
    text_lower = text.lower()
    found_skills = []

    for skill, aliases in SKILLS.items():
        for alias in aliases:
            alias_lower = alias.lower()

            if alias_lower in UNSAFE_SHORT_ALIASES:
                continue

            pattern = r"(?<!\w)" + re.escape(alias_lower) + r"(?!\w)"
            if re.search(pattern, text_lower):
                found_skills.append(skill)
                break  # stop checking aliases once matched

    unique_skills = sorted(set(found_skills))
    return [DISPLAY_SKILLS.get(skill, skill) for skill in unique_skills]
