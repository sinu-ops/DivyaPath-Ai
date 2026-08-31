# app/module3/roadmap_generator.py

def generate_roadmap(student_profile, resume_profile):
    """
    student_profile = {
        "grade": "C",
        "risk": "Medium",
        "study_hours": 12,
        "attendance": 68
    }

    resume_profile = {
        "role": "Data Scientist",
        "matched_skills": ["python", "pandas"],
        "missing_skills": ["sql", "machine learning", "power bi", "deep learning"]
    }
    """

    role = resume_profile.get("role", "Your Target Role")
    missing = resume_profile.get("missing_skills", [])
    risk = student_profile.get("risk", "Medium")
    study_hours = student_profile.get("study_hours", 10)

    intensity = "normal"
    if risk in ["High", "Very High"] or study_hours < 10:
        intensity = "slow"
    elif risk in ["Low", "Very Low"] and study_hours >= 20:
        intensity = "fast"

    def split_skills(skills, n):
        return [skills[i:i+n] for i in range(0, len(skills), n)]

    skill_chunks = split_skills(missing, 2)

    roadmap_3 = []
    roadmap_6 = []
    roadmap_12 = []

    # 3 Month Plan – Foundation
    roadmap_3.append(f"Understand the basics of {role} and career path.")
    if skill_chunks:
        roadmap_3.append(f"Learn: {', '.join(skill_chunks[0])}")
    roadmap_3.append("Study 1–2 hours daily.")
    roadmap_3.append("Build 1 small project.")
    roadmap_3.append("Improve attendance and consistency.")

    # 6 Month Plan – Skill Building
    roadmap_6.append("Start intermediate-level topics.")
    if len(skill_chunks) > 1:
        roadmap_6.append(f"Learn: {', '.join(skill_chunks[1])}")
    roadmap_6.append("Build 2 real-world projects.")
    roadmap_6.append("Create a strong resume.")
    roadmap_6.append("Start sharing work on GitHub and LinkedIn.")

    # 12 Month Plan – Career Ready
    roadmap_12.append("Master advanced concepts.")
    if len(skill_chunks) > 2:
        roadmap_12.append(f"Learn: {', '.join(sum(skill_chunks[2:], []))}")
    roadmap_12.append("Build a capstone project.")
    roadmap_12.append("Prepare for interviews.")
    roadmap_12.append("Apply for internships or jobs.")

    if intensity == "slow":
        roadmap_3.insert(0, "Focus on discipline and habits before speed.")
        roadmap_6.insert(0, "Increase daily study time gradually.")
    elif intensity == "fast":
        roadmap_3.insert(0, "You can move faster than average students.")
        roadmap_6.insert(0, "Start internships earlier than planned.")

    return {
        "intensity": intensity,
        "3_month": roadmap_3,
        "6_month": roadmap_6,
        "12_month": roadmap_12
    }
