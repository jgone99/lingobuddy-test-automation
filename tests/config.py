import os
from dotenv import load_dotenv

load_dotenv()

collect_ignore = ["tests/auth_setup.py"]

TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

# Page Urls
BASE_URL = os.getenv("BASE_URL", "http://localhost:3000")
HOMEPAGE_URL = f"{BASE_URL}/home-page"

# Protected routes
COURSE_LIST_URL = f"{BASE_URL}/course-list"
CHATBOT_URL = f"{BASE_URL}/chatbot"
SNOWMAN_URL = f"{BASE_URL}/games/snowman"
MATCHING_URL = f"{BASE_URL}/games/matching"
SIGN_IN_URL = f"{BASE_URL}/sign-in"

# API Endpoints
OPENAI_API_URL = f"{BASE_URL}/api/openai"