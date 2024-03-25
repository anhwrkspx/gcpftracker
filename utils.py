import requests
from bs4 import BeautifulSoup
from datetime import datetime



skills = [
    "Get Started with TensorFlow on Google Cloud",
    "Build LookML Objects in Looker",
    "Detect Manufacturing Defects using Visual Inspection AI",
    "Analyze Speech and Language with Google APIs",
    "Analyze Images with the Cloud Vision API",
    "Analyze Sentiment with Natural Language API",
    "Predict Soccer Match Outcomes with BigQuery ML",
    "Create and Manage AlloyDB Databases",
    "Manage PostgreSQL Databases on Cloud SQL",
    "Monitor and Manage Google Cloud Resources",
    "Manage Kubernetes in Google Cloud",
    "Automating Infrastructure on Google Cloud with Terraform",
]
bases = [
    "Baseline: Data, ML, AI",
    "Intro to ML: Language Processing",
    "Intro to ML: Image Processing",
    "Generative AI Explorer - Vertex AI",
    "Google Cloud Computing Foundations: Data, ML, and AI in Google Cloud",
    "Managing Machine Learning Projects with Google Cloud",
    "Introduction to AI and Machine Learning on Google Cloud",
    "Applying Machine Learning to your Data with Google Cloud",
    "Production Machine Learning Systems",
    "Smart Analytics, Machine Learning, and AI on Google Cloud",
    "ML Pipelines on Google Cloud",
    "Baseline: Infrastructure",
    "Google Cloud Computing Foundations: Infrastructure in Google Cloud - Locales",
    "Securing your Network with Cloud Armor",
    "Google Cloud Computing Foundations: Networking & Security in Google Cloud",
    "Mitigating Security Vulnerabilities on Google Cloud",
]



def get_badge_info(profileUrl):
    min_date = datetime(year=2024, month=3, day=22)
    badge_info = []
    # Parse the HTML content
    try :
     soup = BeautifulSoup(requests.get(profileUrl).content, "html.parser")
    except ValueError:
        return []
    # Find all badge divs
    badge_divs = soup.find_all("div", class_="profile-badge")
    for badge_div in badge_divs:
    # Get badge name and earned date
      badge_name = badge_div.find("span", class_="ql-title-medium l-mts").text.strip()
      earned_date_str = badge_div.find("span", class_="ql-body-medium l-mbs").text.strip()
      if " " in earned_date_str:
        # Extract full date part with month name
        date_part = earned_date_str.split()[1:4]
        date_part = " ".join(date_part)  # Join the elements back into a string
        date_part = date_part.replace(",", "")
      else:
        date_part = earned_date_str
    # Use conditional formatting based on presence of spaces
      format_string = "%b %d %Y"

    # Attempt parsing and handle potential errors
      try:
        earned_date = datetime.strptime(date_part, format_string)
      except ValueError:
        print(date_part)
        continue  # Skip to the next badge if parsing fails

      if earned_date >= min_date:
        if badge_name in skills:
            badge_info.append(
                {"name": badge_name, "earned_date": earned_date, "type": "skill"}
            )
        if badge_name in bases:
            badge_info.append(
                {"name": badge_name, "earned_date": earned_date, "type": "bases"}
            )
    return badge_info

def get_badge_statistics(badge_info):
    badge_skills = 0
    badge_base = 0
    for badge in badge_info:
        if badge["type"] == "skill":
            badge_skills += 1
        if badge["type"] == "bases":
            badge_base += 1
    badgeCount = badge_base + badge_skills
    return [badgeCount, badge_skills,badge_base]

# def show_badge_date(badge_info):

def categorize_tier(badge_data):
    total = badge_data[0]
    skills= badge_data[1]
    base= badge_data[2]
    print(badge_data)
    tier = "0"
    if(total>=14 and skills>=6 and base>=8):
        tier="2"
    elif(total>=7 and skills>=3 and base>=4):
      tier="1"
      
    return tier
