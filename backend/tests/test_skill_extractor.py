from services.skill_extractor import extract_skills


def test_extract_skills():
    job_description = """
    You bring successfully completed projects and several years of experience with Cloud, DevOps, DevSecOps, SRE concepts or DevOps tools and technologies to the table
    You are motivated to constantly develop yourself in the area of DevOps and Cloud, to try out new things and test the latest technologies
    You have knowledge of Continuous Integration & Continuous Deployment (Bamboo, Jira, Confluence, Jenkins, Ansible, Docker, Kubernetes)
    You bring knowledge in Infrastructure as Code (Ansible, Terraform) with you
    Ideally, you are already Cloud/AWS-certified or are interested in obtaining certifications with our support
    javascript
    """

    result = extract_skills(job_description)

    assert "Jenkins" in result
    assert "Docker" in result
    assert "JavaScript" in result

    # negative check
    assert "RandomSkill" not in result
