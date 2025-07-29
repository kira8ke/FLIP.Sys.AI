# 🧠 FLIP.Sys.AI Incident API Health Checker

This is a Python-based DevOps mini project that checks the availability and response time of the FLIP.Sys.AI incident reporting API. It simulates a basic reliability check mechanism for AI-based backend systems like those used by Innovex Solutions.

## 🚀 Project Goals

- Monitor uptime and health of the `https://api.flip-sys.ai/v1/incident-report` endpoint.
- Practice CI/CD automation with GitHub Actions.
- Containerize the app with Docker.
- Learn how API observability works in modern microservice architectures.

---

## 🧩 Tech Stack

- **Python 3.10+**
- **Requests** – for making HTTP calls
- **Docker** – containerization
- **GitHub Actions** – CI pipeline
- **Cloudflare (experimented)** – caching and DNS
- **cPanel / aaPanel** – cloud hosting interfaces (background experience)

---

## ⚙️ Setup Instructions

### 1. Clone the repo


git clone https://github.com/kira8ke/FLIP.Sys.AI.git
cd FLIP.Sys.AI
2. Create a virtual environment

python -m venv fly_sys_checker_env
source fly_sys_checker_env/bin/activate  # On Windows: fly_sys_checker_env\Scripts\activate
3. Install dependencies

pip install -r requirements.txt
4. Run the checker

python checker.py
🐳 Run with Docker

docker build -t flip-sys-checker .
docker run flip-sys-checker
🔁 CI/CD with GitHub Actions
A GitHub Actions workflow is included to:

Install dependencies

Run the script on push

Workflow file: .github/workflows/ci.yml
