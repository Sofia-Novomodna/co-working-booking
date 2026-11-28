Co-working booking
Co-working booking is made for people, who would like to reserve the room in co-working space. Designed especially for students who need a reliable space to practice, learn, and collaborate on group projects
This website is made to simplify the room reservation process to make planning effortless and stress-free.
Featuring a clean, student-friendly interface, the website allows you to easily browse available spaces complete with helpful descriptions detailing key attributes like quietness levels, capacity limits, and maximum reservation times. Plus, with a built-in link-sharing feature, coordinating schedules and inviting your team members to join your study session has never been easier, ensuring every meeting is a success.



















Co-working
booking
Co-working
booking is made for people, who would like to reserve the room in co-working space.
Mostly it would be made for students, who would like to practice, learn and do
group projects here.
This website
is made to simplify booking process of the room in co-working space. It make
the possibility for people to plan their schedule much easier and be confident
that their meeting or learning will be successful.
The website
have to contain user-friendly interface for student . There have to be short
description for each room, with such attributes, like: quietness, capability of
people, limit of reservation-time . Ability to share the link to booking for
the group is also necessary.











how to start:
cd D:\sn\co-working-booking\co-working-booking\django-coworking
cd /d/sn/study/co-working-booking/co-working-booking/django-coworking
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
$env:Path += ";$HOME\.local\bin;$HOME\.cargo\bin"
uv --version
uv sync
uv run python manage.py runserver




uv run py manage.py makemigrations main
uv run py manage.py migrate 
uv run python manage.py runserver 




git config user.name "Sofia Novomodna"
git config user.email "sofia.novomodna@gmail.com"




admin
sophianovo666


user1
useruser001



Tasks:
- Membership Plans & Credits System: You listed Day Pass, Hot Desk, and Dedicated Deck plans with perks like "2 hours of complimentary meeting room credits". Create a UserProfile model (linked via OneToOneField to User) that stores:
Active subscription tier
Remaining meeting room hours/credits
Automatically deduct credits or calculate the total price (duration * room.hourly_rate) before confirming a booking!
-Export to Calendar (.ics file) or CSV: Add a button on a confirmed booking to "Add to Calendar" by generating a downloadable .ics file in a Django view,





<div class="mb-3">
    <label class="form-label fw-bold text-uppercase small text-secondary">Select Room / Area</label>
    <select name="room" class="form-select bg-light shadow-none" required>
        <option value="" disabled selected>Choose a space...</option>
        {% for room in rooms %}
            <option value="{{ room.id }}" {% if request.POST.room = room.id|stringformat:"s" %}selected{% endif %}>
                {{ room.room_name }}
            </option>
        {% empty %}
            <option value="" disabled>No rooms available in database</option>
        {% endfor %}
    </select>
    {% if errors.room %}
        <div class="text-danger small mt-1">{{ errors.room.0 }}</div>
    {% endif %}
</div>

<div class="mb-3">








from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Start the browser
driver = webdriver.Chrome()

# 2. Open the form page
#driver.get("https://www.selenium.dev/selenium/web/web-form.html")
self.driver.get(self.live_server_url)
title = driver.title
driver.implicitly_wait(0.5)

# 3. Find elements and interact with them
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
time.sleep(10)
text_box.send_keys("Selenium")
time.sleep(1)
submit_button.click()
time.sleep(10)
# 4. Get the result message
message = driver.find_element(by=By.ID, value="message")
text = message.text
print(f"Success message: {text}")


time.sleep(10)
# 5. Close the browser
driver.quit()