# SkillForge 

[View Live Website](https://skillforge-uwws.onrender.com)

SkillForge is a full-stack web application built using Python and Django. It is designed to act as a centralized personal learning hub where users can track technical skills, organize and evaluate learning resources (such as documentation, courses, and videos), and log timed study sessions to monitor progress over time.


## Table of Contents
1. [UX & UI Design](#ux--ui-design)
2. [User Stories](#user-stories)
3. [Features](#features)
4. [Database Schema & Architecture](#database-schema--architecture)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Troubleshooting & Engineering Fixes Log](#troubleshooting--engineering-fixes-log)
9. [Credits & Acknowledgements](#credits--acknowledgements)


## UX & UI Design

### Project Goals
- Provide a clean, intuitive, and distraction-free interface for learners to organize self-directed education.
- Enable full CRUD (Create, Read, Update, Delete) management of skills, learning resources, and study logs.
- Implement robust user authentication and self-service password recovery to ensure data privacy and security.

### Target Audience
- Students, software developers, and lifelong learners who want a structured way to track what they are learning and measure their study habits.
- Users who prefer a minimalist, responsive web app over complex spreadsheets or scattered bookmark folders.

### Design & Styling Choices
- **Framework:** Built using **Bootstrap 5** to ensure a responsive grid layout that adapts seamlessly to mobile, tablet, and desktop screens.
- **Dynamic Theme Engine:** Integrated dark/light mode toggling with persistent user theme preferences across the platform.
- **Color Palette & Cards:** Dark navigation bar paired with clean card UI elements, contrast-compliant inputs, and subtle drop shadows.
- **Typography:** Clean system sans-serif fonts for optimal legibility across all devices.

### Wireframes
Wireframes were planned prior to development to establish the layout and responsive design across mobile, tablet, and desktop viewports:

- **Complete Responsive Grid Overview:**
  ![All Wireframes Grid](./wireframes/mobile_screen_tablet_view_desktop_screen.png)

- **Login Page:**
  ![Login Wireframe](./wireframes/wireframe_login.png)

- **Dashboard View:**
  ![Dashboard Wireframe](./wireframes/wireframe_dashboard.png)

- **Skill Detail View:**
  ![Skill Detail Wireframe](./wireframes/wireframe_skill_detail.png)


## User Stories

To guide the development of SkillForge, user stories were defined and categorized into target groups:

### First-Time / New Users
- As a new user, I want to easily register or log in so that my personal skills and study logs are secure.
- As a new user, I want a clean dashboard that explains the purpose of the app and prompts me to add my first skill.
- As a new user, I want to request a password reset if I forget my login credentials.

### Returning Users
- As a returning user, I want to view a dashboard of all my tracked skills with status badges (e.g., *In Progress*, *Mastered*) so I can check my progress at a glance.
- As a returning user, I want to click into a specific skill to view its associated resources and study sessions.

### Frequent / Power Users
- As a power user, I want to add new learning resources with URLs and notes directly to a skill detail page.
- As a power user, I want to log study sessions with duration times and reflections.
- As a power user, I want to update or delete skills, resources, and sessions whenever my learning goals change.


## Features

### Authentication & Security
- Secure user login, registration, and logout system powered by Django's built-in auth system.
- Complete self-service password reset workflow (`PasswordResetView`, `PasswordResetDoneView`, `PasswordResetConfirmView`, `PasswordResetCompleteView`).
- Route protection (`@login_required`) ensuring users can only access, view, and modify their own data.
- Environment variable management using `python-dotenv` to safeguard secret keys and database settings.

###  Custom Form Controls & Dynamic Theming
- Custom form subclasses (`CustomPasswordResetForm`) enforcing consistent Bootstrap `form-control` styles and placeholders across auth forms.
- Dark/Light theme toggling mechanism seamlessly styled across navigation, dashboards, and authentication views.

###  Dashboard & Skill Management
- **Dashboard View:** Displays all user-owned skills organized neatly into Bootstrap cards with category and status indicators.
- **Skill Creation & Editing:** Dedicated forms to create new skills or update existing titles, descriptions, and statuses.