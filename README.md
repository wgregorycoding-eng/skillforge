# SkillForge 🚀

SkillForge is a full-stack web application built with Python and Django designed to help users track personal skills, organize learning resources, and log study sessions in one central place. 

I built this project to solve a common problem: having bookmarks scattered across browsers, notes in random text files, and no clear way to measure actual time spent learning a new technical stack or hobby.

---

## Features

* **Full CRUD Functionality:** Create, read, update, and delete skills, categorized learning resources (articles, videos, books, courses), and timed study sessions.
* **Relational Database Architecture:** Interconnected models (`User` -> `Skill` -> `Resource` / `StudySession`) using Django's ORM.
* **Responsive UI:** Built with **Bootstrap 5** to ensure it looks clean and readable across mobile and desktop screens.
* **Secure Configuration:** Uses `python-dotenv` to safely manage environment variables (`SECRET_KEY`, `DEBUG`) and protect sensitive settings.
* **Version Control:** Developed iteratively using Git for commit tracking and GitHub for remote backup.

---

## Tech Stack

* **Backend:** Python 3.13, Django 6.1
* **Database:** SQLite (development) / PostgreSQL-ready (`dj-database-url`)
* **Frontend:** HTML5, Bootstrap 5 CSS/JS bundles
* **Utilities:** `python-dotenv`, `gunicorn` (for production deployment)

---

## Local Setup & Installation

If you want to run this project locally on your machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/skillforge.git](https://github.com/your-username/skillforge.git)
   cd skillforge