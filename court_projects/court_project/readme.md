# 🏛️ Court-Data Fetcher & Mini-Dashboard

A simple, stylish web application that allows users to search for Indian court cases using their CNR number and view important case metadata. Built for the **She Can Foundation Internship (Task 1)**.

---

## 🔍 Objective

This mini-dashboard allows a user to:
- Search a case by its **CNR Number**
- Fetch and display the following:
  - Petitioner & Respondent names
  - Case number and status
  - Filing date and hearing date
- Display the parsed data in a clean, styled interface
- Handle invalid entries gracefully
- Log all search queries to a database for analysis

---

## 🏗️ Tech Stack

| Layer        | Technology |
|--------------|------------|
| Backend      | Python + Django |
| Frontend     | HTML, CSS, Bootstrap 5 |
| Database     | SQLite (default) |
| Scraper      | Requests + BeautifulSoup |
| Hosting      | Localhost (for demo) |

---

## 🧠 Court Selected

I targeted:  
**[eCourts District Portals (India)](https://districts.ecourts.gov.in/)** using **CNR Number** search.

---

## 🔐 CAPTCHA & Scraping Strategy

Most court websites use **JavaScript-based CAPTCHAs** or **view-state tokens**.  
Instead of bypassing the CAPTCHA (which may violate ToS), I:

- Created a **local mock system** that simulates case search using stored/seeded data.
- Ensured the scraper is modular in case real-time scraping is enabled later with tools like **Playwright**, **Selenium**, or AI-based solvers.

> ⚠️ CAPTCHA avoidance was not implemented directly due to ethical and legal concerns. Explained clearly as instructed.

---

## 💻 Features

- ✅ Styled user interface (Bootstrap 5)
- ✅ Navbar and footer (responsive layout)
- ✅ Search form with placeholder + input validation
- ✅ Loading spinner while search is in progress
- ✅ Friendly error messages (invalid CNR, missing case)
- ✅ Template inheritance (`base.html` with `search_form` and `search_result`)
- ✅ Server-side scraping logic (mock/local version)
- ✅ Query logging in SQLite via `QueryLog` model
- ✅ Messages shown via Django’s messages framework

---


## 📄 License

This project is licensed under the MIT License.

---

## 🎥 Demo Video

[Click to watch demo](https://your-demo-link-here.com)






## 🧪 How to Run the Project

```bash
# 1. Clone the repository
git clone https://github.com/moatazbenma/fullstack-projects.git
cd court_projects

# 2. Create and activate virtual environment
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Start the server
python manage.py runserver
