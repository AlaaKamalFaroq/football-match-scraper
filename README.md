
<img width="756" height="608" alt="Screenshot 2025-08-17 225215" src="https://github.com/user-attachments/assets/79d21ef9-c65e-4056-abca-f82a6a53e8a6" />
# ⚽ Football Match Scraper

**Project Overview:**
A Python tool that automatically scrapes football match data from [YallaKora](https://www.yallakora.com/match-center) for any date. Perfect for **sports analysts, content creators, or data enthusiasts**, it transforms raw match info into **clean, structured CSV files** ready for analysis. This project demonstrates **web scraping, data cleaning, and Python automation skills**.

---

**Key Features:**

* ✅ Scrapes multiple championships in a single day.
* ✅ Captures full match details: championship, teams, match time, final score.
* ✅ Skips incomplete or postponed matches for cleaner datasets.
* ✅ Exports data in **CSV format** with Arabic and English headers.
* ✅ Includes a **project header** in the CSV for context.
* ✅ Handles network errors gracefully to avoid interruptions.

---

**Technologies Used:**

* **Python 3.x**
* **Requests** – HTTP requests handling
* **BeautifulSoup4** – HTML parsing
* **lxml** – fast and efficient parsing
* **CSV module** – structured data export

---

**How to Use:**

1. Run the script:

   ```bash
   python web_scraping.py
   ```

2. Enter the date in `m/d/y` format.

3. Check your **Documents** folder for `matches.csv`.

4. Enjoy a CSV with both **Arabic and English headers**—professional and ready for reporting or analysis.

---

**Sample CSV Output:**

| نوع البطولة / Championship | الفريق الأول / Team 1 | الفريق الثاني / Team 2 | ميعاد المباراة / Match Time | النتيجة / Score |
| -------------------------- | --------------------- | ---------------------- | --------------------------- | --------------- |
| الدوري الإنجليزي           | ليفربول               | تشيلسي                 | 8:30 PM                     | 2 - 1           |

---

**Skills & Learnings Demonstrated:**

* Web scraping & HTML parsing
* Handling multilingual content (Arabic + English)
* Data cleaning & validation
* Structured CSV output & automation
* Python best practices: modular code, error handling

---

**Code Readability & Comments:**

* The Python script is **fully commented** to explain each step.
* Every section has **clear notes** describing its purpose—from sending requests to exporting CSV.
* This makes the code **easy to follow and modify** for beginners, clients, or collaborators.
* Example: `# Send request to website and get HTML content`

<img width="886" height="102" alt="Screenshot 2025-08-17 225823" src="https://github.com/user-attachments/assets/25745635-c735-452a-ad14-68dce6f58f54" />

