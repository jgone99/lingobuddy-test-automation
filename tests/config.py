import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")
TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")

# Protected routes
COURSE_LIST_URL = f"{BASE_URL}/course-list"
CHATBOT_URL = f"{BASE_URL}/chatbot"
SNOWMAN_URL = f"{BASE_URL}/games/snowman"
MATCHING_URL = f"{BASE_URL}/games/matching"
SIGN_IN_URL = f"{BASE_URL}/sign-in"