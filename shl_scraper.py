from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

# Set up Chrome options
options = Options()
options.add_argument("--headless")  # run in background
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Start URL (page 1 of test solutions)
start_url = "https://www.shl.com/en/assessments/catalog/?page=1"
driver.get(start_url)

all_tests = []

# Iterate over all 32 pages
for page in range(1, 33):
    print(f"Scraping page {page}...")
    driver.get(f"https://www.shl.com/en/assessments/catalog/?page={page}")
    time.sleep(2)

    # Find all rows in the table
    rows = driver.find_elements(By.CSS_SELECTOR, "table tr")[1:]  # skip header row

    for row in rows:
        try:
            link_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) a")
            test_name = link_element.text.strip()
            test_url = link_element.get_attribute("href")

            # Visit individual test link
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(test_url)
            time.sleep(1.5)

            try:
                description = driver.find_element(By.CSS_SELECTOR, ".rich-text-content").text.strip()
            except:
                description = "No description found"

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

            all_tests.append({
                "name": test_name,
                "url": test_url,
                "description": description
            })

        except Exception as e:
            print(f"Failed to extract a row: {e}")
            continue

# Save results to JSON
with open("shl_assessment.json", "w", encoding="utf-8") as f:
    json.dump(all_tests, f, ensure_ascii=False, indent=2)

driver.quit()
print(f"Scraping complete. Total tests scraped: {len(all_tests)}")
