import requests
import os

# تنظیمات
USERNAME = "wahidalawy" # یوزرنیم خودت را اینجا بنویس
SVG_TEMPLATE_PATH = "template.svg"
SVG_OUTPUT_PATH = "status.svg"

def get_total_commits():
    # استفاده از API جستجوی گیت‌هاب برای شمارش کامیت‌ها
    url = f"https://api.github.com/search/commits?q=author:{USERNAME}"
    response = requests.get(url)
    if response.status_code == 200: # <--- این خط اصلاح شد
        return response.json().get('total_count', 0)
    return "N/A"

def update_svg(count):
    with open(SVG_TEMPLATE_PATH, "r") as f:
        content = f.read()
    
    # جایگذاری مقدار جدید در قالب
    new_content = content.replace("{{COMMIT_COUNT}}", str(count))
    
    with open(SVG_OUTPUT_PATH, "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    commits = get_total_commits()
    update_svg(commits)
    print(f"Stats updated: {commits} commits")