---

# Playwright Python Script Documentation

## Overview

This automation script uses **Playwright** to simulate a user logging into the [hostnplay.com](https://hostnplay.com/) website, then clicking the "Create Game" button after signing in. The purpose is to automate the login and navigation process for testing or demonstration purposes.

---

## What the Script Does

- Opens the Chrome browser.
- Navigates to the HostnPlay website.
- Simulates a user clicking the "Sign in" link.
- Fills in the email and password fields with demo credentials.
- Clicks the "Sign in" button to attempt login.
- After logging in, clicks the "Create Game" button.
- Closes the browser.

---

## Step-by-step Explanation

Below is a detailed breakdown of every action, including WHY it is performed and the expected result.

### Step 1: Open Browser and New Page
**What:** The script launches the Chrome browser (not in headless mode), creates a new context, and a new page.  
**Element:** Not applicable  
**Text:** None  
**Why:** This sets up a fresh, isolated browsing environment for the automation.  
**Expected Result:** Chrome opens with a blank tab.

---

### Step 2: Go to Website
**What:** The script navigates to https://hostnplay.com/  
**Element:** Browser address bar  
**Text:** None  
**Why:** This loads the HostnPlay homepage as the starting point.  
**Expected Result:** Homepage is visible in the browser tab.

---

### Step 3: Click "Sign in" Link
**What:** Clicks the "Sign in" link on the homepage.  
**Element:** The link with accessible name "Sign in"  
**Text:** None  
**Why:** To navigate to the login form.  
**Expected Result:** Login form is shown.

---

### Step 4: Click Email Input Textbox
**What:** Clicks the "Email" textbox in the login form.  
**Element:** The textbox with accessible name "Email"  
**Text:** None  
**Why:** Focuses the email input field to prepare for input.  
**Expected Result:** Email textbox is focused.

---

### Step 5: Enter Email Address
**What:** Enters **email@example.com** into the "Email" textbox.  
**Element:** The textbox with accessible name "Email"  
**Text:** `email@example.com`  
**Why:** Provides the email address for logging in with demo credentials.  
**Expected Result:** The email is shown as typed in the textbox.

---

### Step 6: Click Password Input Textbox
**What:** Clicks the "Password" textbox in the login form.  
**Element:** The textbox with accessible name "Password"  
**Text:** None  
**Why:** Focuses the password input field to prepare for input.  
**Expected Result:** Password textbox is focused.

---

### Step 7: Enter Password
**What:** Enters **password.** into the "Password" textbox.  
**Element:** The textbox with accessible name "Password"  
**Text:** `password.`  
**Why:** Provides the password for the demo account.  
**Expected Result:** The password is shown as entered in the textbox (will be masked).

---

### Step 8: Click "Sign in" Button
**What:** Clicks the "Sign in" button to submit the login form.  
**Element:** The button with accessible name "Sign in"  
**Text:** None  
**Why:** Submits the login form to attempt authentication.  
**Expected Result:** The user is logged in and redirected to their dashboard or home page.

---

### Step 9: Click "Create Game" Button
**What:** Clicks the "Create Game" button.  
**Element:** The button with accessible name "Create Game"  
**Text:** None  
**Why:** Simulates navigating to the game creation workflow after login.  
**Expected Result:** Game creation interface is loaded (if login was successful).

---

### Step 10: Close Page and Browser
**What:** Closes the active page, browser context, and browser itself.  
**Element:** Browser window  
**Text:** None  
**Why:** Cleans up after script execution.  
**Expected Result:** All browser windows are closed.

---

## Text Inputs Explained

| Text Value            | Where Entered                    | What It Represents                | Why It Is Needed                 |
|-----------------------|----------------------------------|-----------------------------------|----------------------------------|
| `email@example.com`  | "Email" textbox                  | Demo user email address           | Needed for logging in as a demo user |
| `password.`             | "Password" textbox               | Demo user password                | Needed for demo user authentication  |

---

## Selectors Used

| Selector (API Call)                              | Targets...                                                                         |
|--------------------------------------------------|-------------------------------------------------------------------------------------|
| `page.get_by_role("link", name="Sign in")`       | The "Sign in" link (navigates to the login form)                                   |
| `page.get_by_role("textbox", name="Email")`      | The input box for the user's email address                                         |
| `page.get_by_role("textbox", name="Password")`   | The input box for the user's password                                              |
| `page.get_by_role("button", name="Sign in")`     | The button to submit the login form                                                |
| `page.get_by_role("button", name="Create Game")` | The button to initiate the game creation process (after login)                     |

These selectors use Playwright's **ARIA role** queries, which match elements based on web accessibility roles and their accessible names.

---

## How to Run the Script

1. Make sure [Playwright for Python](https://playwright.dev/python/docs/intro) is installed.
2. Save the script as `login1.py`.
3. Run the script in your terminal using:

```bash
python login1.py
```

---

## Improvements

### Better Selectors
- Use more **stable and unique selectors**, e.g.:
  - Data attributes (`data-testid`, `data-qa`)
  - Element `id` or `name`
  - CSS or XPath as a last resort

### Error Handling
- **Add try/except blocks** around actions to handle connection failures or missing elements.
- Log descriptive errors if steps fail.

### Wait Conditions
- Use **explicit waits** like `page.wait_for_selector(...)` or `expect` before clicking or typing to ensure elements are loaded.
  - Example: `page.wait_for_selector('input[name="email"]')`
- Wait for navigation after "Sign in" before clicking "Create Game" to ensure the page has fully loaded.

### Security Improvements
- **Never hard-code credentials in code**! Use environment variables, secrets managers, or input prompts.
- Example with `os.environ.get("EMAIL")` and `os.environ.get("PASSWORD")`.

### Additional Recommendations
- **Add assertions** to confirm login was successful before proceeding (e.g., checking for user-specific content).
- Include **logging** for step-by-step results and errors.
- Consider running in **headless mode** for CI environments.

---

**End of Documentation**