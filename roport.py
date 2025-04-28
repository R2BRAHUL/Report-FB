import requests
import random
import time
import os

# রঙিন প্রিন্ট ফাংশন
def cprint(text, color="default"):
    colors = {
        "default": "\033[0m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m"
    }
    print(f"{colors.get(color, colors['default'])}{text}{colors['default']}")

# ব্যানার
def banner():
    os.system('clear')
    cprint("""
███████╗██████╗ ███████╗██╗  ██╗███████╗
██╔════╝██╔══██╗██╔════╝██║ ██╔╝██╔════╝
███████╗██████╔╝█████╗  █████╔╝ ███████╗
╚════██║██╔═══╝ ██╔══╝  ██╔═██╗ ╚════██║
███████║██║     ███████╗██║  ██╗███████║
╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝
          Extreme Auto Reporter
        Made with E24 from Cyber7F
""", "magenta")

# ইউজার লগিন ইনপুট
def login():
    email = input("[+] Email/Phone: ")
    password = input("[+] Password: ")
    cprint("\n[+] Logging in (Simulated)...", "cyan")
    time.sleep(2)
    # এখানে রিয়েল ফেসবুক লগইন হবে না, কারণ টার্মাক্স বা এইভাবে করলে ফেসবুক লগইন ব্লক করে। এটা শুধু স্ক্রিপ্টের অংশ।
    cprint("[+] Login successful (Simulated)\n", "green")
    return email, password

# লিংক ইনপুট
def get_links():
    links = []
    print("[+] Enter target links (one per line, type 'done' when finished):")
    while True:
        link = input("Link: ")
        if link.lower() == 'done':
            break
        links.append(link)
    return links

# র‍্যান্ডম ইউজার এজেন্ট
def random_user_agent():
    agents = [
        "Mozilla/5.0 (Linux; Android 10; SM-G973F)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (Linux; Android 9; Redmi Note 7)"
    ]
    return random.choice(agents)

# রিপোর্ট ফাংশন (ভান করে রিপোর্ট পাঠানো)
def report(link):
    headers = {
        "User-Agent": random_user_agent()
    }
    fake_data = {
        "reason": "spam",
        "details": "Fake account or abusive page."
    }
    try:
        # বাস্তবে ফেসবুকে রিপোর্ট পাঠানো যাবে না সরাসরি এইভাবে। এটা demo (simulated) রিপোর্ট sending।
        response = requests.post(link, headers=headers, data=fake_data)
        if response.status_code == 200:
            cprint(f"[+] Successfully Reported: {link}", "green")
        else:
            cprint(f"[-] Failed to Report: {link} (Status {response.status_code})", "red")
    except Exception as e:
        cprint(f"[-] Error Reporting {link}: {str(e)}", "red")

# মেইন
def main():
    banner()
    email, password = login()
    links = get_links()
    cprint(f"\n[+] Total Targets: {len(links)}", "yellow")
    cprint("[+] Starting report attacks...\n", "cyan")
    for link in links:
        report(link)
        delay = random.randint(5, 8)
        cprint(f"[i] Sleeping for {delay} seconds...", "blue")
        time.sleep(delay)
    cprint("\n[+] All reports done!", "green")

if __name__ == "__main__":
    main()