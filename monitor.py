# Import Playwright for browser automation
from playwright.sync_api import sync_playwright

# Import datetime to display timestamps in logs and alerts
from datetime import datetime

# Import requests to send Discord webhook notifications
import requests

# Import time to create delays between checks
import time

# Amazon Ottawa jobs page being monitored
URL = "https://hiring.amazon.ca/app#/jobSearch?query=&postal=k2b7s9&locale=en-CA"

# Time interval (in seconds) between each website check
CHECK_EVERY_SECONDS = 30

# Discord webhook URL used for sending notifications
WEBHOOK_URL = ""


def send_discord_alert():
    """
    Sends a notification to Discord when a potential job posting is detected.
    """

    message = f"""
🚨 **AMAZON OTTAWA JOB DETECTED**

📍 Location: Ottawa area
🔎 Source: Amazon Hiring
⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Apply/check here:
{URL}
"""

    requests.post(
        WEBHOOK_URL,
        json={"content": message}
    )


def check_page(page):
    """
    Opens the Amazon jobs page and analyzes its content.

    Returns:
        True  -> Potential job posting detected
        False -> No jobs available
    """

    # Navigate to Amazon jobs page
    page.goto(URL, wait_until="networkidle", timeout=60000)

    # Give page additional time to fully load dynamic content
    time.sleep(5)

    # Extract all visible page text and convert to lowercase
    text = page.inner_text("body").lower()

    # Phrases commonly shown when no jobs are available
    no_job_phrases = [
        "there are no jobs available",
        "no jobs available",
        "no jobs found",
        "no results found",
        "sorry, there are no jobs"
    ]

    # If any "no jobs" phrase is found, return False
    for phrase in no_job_phrases:
        if phrase in text:
            return False

    # Keywords that may indicate a valid job posting
    job_keywords = [
        "fulfillment center",
        "warehouse associate",
        "sortation center",
        "delivery station",
        "amazon fulfillment",
        "hourly opportunities"
    ]

    # If any job-related keyword is found, return True
    for keyword in job_keywords:
        if keyword in text:
            return True

    # Default to False if no known indicators are found
    return False


def main():
    """
    Main monitoring loop.

    Continuously checks the Amazon jobs page and sends
    a Discord alert when a job is detected.
    """

    # Prevents duplicate alerts for the same posting
    already_alerted = False

    # Start Playwright browser session
    with sync_playwright() as p:

        # Launch Chromium browser
        browser = p.chromium.launch(headless=False)

        # Open a new browser tab
        page = browser.new_page()

        # Continuous monitoring loop
        while True:
            try:
                # Check page for job postings
                found = check_page(page)

                # Send alert only once per detected posting
                if found and not already_alerted:

                    print(
                        f"[{datetime.now().strftime('%H:%M:%S')}] JOB DETECTED"
                    )

                    send_discord_alert()

                    already_alerted = True

                # Reset alert status when no jobs are available
                elif not found:

                    print(
                        f"[{datetime.now().strftime('%H:%M:%S')}] No jobs detected"
                    )

                    already_alerted = False

            except Exception as e:
                # Display any unexpected errors
                print("Error:", e)

            # Wait before checking again
            time.sleep(CHECK_EVERY_SECONDS)


# Program entry point
if __name__ == "__main__":
    main()