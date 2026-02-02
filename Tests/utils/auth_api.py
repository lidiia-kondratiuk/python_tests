import re
from playwright.sync_api import APIRequestContext


def login_via_api_and_save_state(
    request: APIRequestContext,
    base_url: str,
    email: str,
    password: str,
    state_path: str,
):
    """
    Logs in via API and saves authenticated storage state to file.
    """

    # 1️⃣ Open login page (for CSRF token if needed)
    response = request.get(f"{base_url}/users/sign_in")
    if not response.ok:
        raise RuntimeError(f"Cannot open login page. Status: {response.status}")

    csrf_token = None
    html = response.text()
    match = re.search(r'name="csrf-token"\s+content="([^"]+)"', html)
    if match:
        csrf_token = match.group(1)

    # 2️⃣ Login request
    headers = {}
    if csrf_token:
        headers["x-csrf-token"] = csrf_token

    login_response = request.post(
        f"{base_url}/users/sign_in",
        form={
            "user[email]": email,
            "user[password]": password,
        },
        headers=headers,
    )

    if not login_response.ok:
        raise RuntimeError(
            f"Login failed. Status: {login_response.status}. "
            f"Body: {login_response.text()[:300]}"
        )

    # 3️⃣ Save storage state
    request.storage_state(path=state_path)
