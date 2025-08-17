import requests
from bs4 import BeautifulSoup
import csv
import os

print("📂 Saving file to:", os.getcwd())

# Ask the user to enter the date
date = input("please put the format data in (m/d/y)")

# Prepare the URL
url = "https://www.yallakora.com/match-center?date="

# Fetch the webpage
try:
    page = requests.get(url + date)
    page.raise_for_status()  # Raise error if request fails
except requests.RequestException as e:
    print(f"❌ Error fetching page: {e}")
    exit()

# Main function to scrape the page
def main(pg):
    src = pg.content
    '''
    print(page.content) this will print a (byte code) a machine readable format to the html content .
    instead do this :we need a parser to read and select content well from the page.
    '''

    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(src, 'lxml')  # to view the page as HTML code (readable to human)

    '''
    Search for tag descendants and look inside and
    return all data that match filters (match my div with the class match card)
    '''
    champ = soup.find_all('div', {'class': 'matchCard'})

    # Optional: print the first part of HTML to inspect
    print(soup.prettify()[:2000])

    # print the number of championships.
    print(len(champ))
    match_details = []

    # Function to extract match info from each championship
    def get_info(chp):
        # here champ has all content related to the matches
        # each div is related to a championship, each div has title, ul each ul has the matches info
        champ_title = chp.contents[1].find('h2').text.strip()
        # print(champ_title)
        matches = chp.contents[3].find_all('div', {'class': 'item'})
        number_of_matches = len(matches)
        # print(matches)
        for i in range(len(matches)):
            # get names
            get_name1 = matches[i].find('div', {'class': 'teamA'}).find('p').text.strip()
            get_name2 = matches[i].find('div', {'class': 'teamB'}).find('p').text.strip()

            # get score
            score_matches = matches[i].find('div', {'class': 'MResult'}).find_all('span', {'class': 'Score'})
            if len(score_matches) == 2:
                score = f"{score_matches[0].text.strip()} - {score_matches[1].text.strip()}"
            else:
                score = "لم تُلعب بعد"  # or "N/A" or anything else you prefer
                print(f"⚠️ Score not found for match {get_name1} vs {get_name2}")

            # get match time
            time_span = matches[i].find('div', {'class': 'MResult'}).find('span', {'class': 'Time'})
            if time_span:
                time = time_span.text.strip()
            else:
                time = "غير محدد"  # Or "N/A", or "موعد غير متوفر"
                print(f"⚠️ Time not found for match {get_name1} vs {get_name2}")

            # add info to the match_details list
            match_details.append({
                'نوع البطوله': champ_title,
                'الفريق الاؤل': get_name1,
                'الفريق الثاني': get_name2,
                'ميعاد المباره': time,
                'النتيجه': score
            })

    # loop through all championships
    for chp in champ:
        get_info(chp)

    return match_details

# ---- MAIN EXECUTION ----
match_details = main(page)

if match_details:
    try:
        # Save CSV in user's Documents folder to avoid permission errors
        output_path = os.path.join(os.path.expanduser("~"), "Documents", "matches.csv")
        keys = match_details[0].keys()
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            f.write("Project: Football Match Scraper\n")
            f.write(f"Date of Data: {date}\n")
            f.write("All times are local to the match location\n\n")
            foutput = csv.DictWriter(f, keys)
            foutput.writeheader()
            foutput.writerows(match_details)
        print(f"✅ File matches.csv created successfully at:\n📂 {output_path}")
    except PermissionError:
        print("❌ Permission denied! Try closing any open matches.csv file or choose a different folder.")
else:
    print("⚠️ لم يتم العثور على أي مباريات في هذا التاريخ.")

print("📂 Full path:", os.path.abspath("matches.csv"))
