---

# Playwright Automation Script Documentation

## Overview

This script automates the process of logging into the [HostnPlay](https://hostnplay.com/) website, creating a new game, uploading an image, configuring game details, and scheduling the event. The script uses the Playwright Python library to simulate the actions of a real user from signing in to scheduling a new game event.

---

## What the Script Does

From start to finish, the script:
1. Opens HostnPlay in a Chromium browser.
2. Logs into an existing account using provided credentials.
3. Initiates the process to create a new game.
4. Uploads an avatar image for the game.
5. Selects suggested AI-generated game ideas.
6. Sets date and time for the game.
7. Schedules and finalizes the creation of the game, then closes the browser.

---

## Step-by-Step Explanation

### 1. Open Browser and Navigate to Website
- **What:** Opens a Chromium browser (Chrome channel), and navigates to HostnPlay homepage.
- **Element:** Website (`https://hostnplay.com/`)
- **Expected result:** HostnPlay homepage loads.

### 2. Click "Sign in"
- **What:** Clicks the "Sign in" link.
- **Element:** Link with name "Sign in".
- **Expected result:** Login form appears.

### 3. Enter Email Address
- **What:** Clicks and fills in the email textbox.
- **Element:** Textbox labeled "Email".
- **Text being entered:** `demo@hostnplay.com`
- **Why:** To input the login email address for authentication.
- **Expected result:** Email field is populated.

### 4. Enter Password
- **What:** Clicks and fills in the password textbox.
- **Element:** Textbox labeled "Password".
- **Text being entered:** `Demo12.`
- **Why:** To input the login password for authentication.
- **Expected result:** Password field is populated.

### 5. Click "Sign in"
- **What:** Clicks the "Sign in" button.
- **Element:** Button named "Sign in".
- **Expected result:** User is logged in, redirected to user dashboard.

### 6. Click "Create Game"
- **What:** Clicks the "Create Game" button.
- **Element:** Button named "Create Game".
- **Expected result:** Game creation popup/modal is opened.

### 7. Close the Modal
- **What:** Clicks the 'x' close button.
- **Element:** Text 'x'.
- **Expected result:** Closes the current popup/modal (if any).

### 8. Click "Create New Game"
- **What:** Clicks the "Create New Game" option.
- **Element:** Text "Create New Game".
- **Expected result:** Opens the new game creation form.

### 9. Initiate Image Upload
- **What:** Clicks on image upload area.
- **Element:** Text starting with "Upload Your ImageClick to".
- **Expected result:** Opens file selector.

### 10. Upload Image
- **What:** Uploads image file.
- **Element:** File input in page body.
- **Text being entered:** `no-avatar.jpg`
- **Why:** To provide an avatar or cover image for the new game.
- **Expected result:** Image is uploaded and previewed.

### 11. Open AI Assistance
- **What:** Clicks "Open AI" button.
- **Element:** Button named "Open AI".
- **Expected result:** Lists of AI-generated game ideas appear.

### 12. Select AI-generated Game Idea
- **What:** Selects a suggested game idea.
- **Element:** 6th occurrence of div containing text "Create a competitive Warzone".
- **Expected result:** Game details are filled with suggested content.

### 13. Proceed to Next Step(s) in Creation
- **What:** Clicks a button (general button, third instance).
- **Element:** Third button on the page.
- **Expected result:** Advances to the next stage in creation.

### 14. Click "Next"
- **What:** Clicks the "Next" button.
- **Element:** Button named "Next".
- **Expected result:** Moves to the summary or scheduling step.

### 15. Click "Submit"
- **What:** Clicks the "Submit" button.
- **Element:** Button named "Submit".
- **Expected result:** Proceeds to scheduling.

### 16. Select Day (28)
- **What:** Clicks on text "28".
- **Element:** Text "28".
- **Expected result:** Picks the 28th day of the calendar (date selection).

### 17. Set Time
- **What:** Clicks and fills in the time input.
- **Element:** Input of type `"time"`.
- **Text being entered:** `20:30`
- **Why:** Specifies the start time for the scheduled game (8:30 PM).
- **Expected result:** The time is set for the game event.

### 18. Click "Generate"
- **What:** Clicks the "Generate" button.
- **Element:** Button named "Generate".
- **Expected result:** Finalizes date/time generation for the event.

### 19. Click "Schedule"
- **What:** Clicks the "Schedule" button.
- **Element:** Button named "Schedule".
- **Expected result:** Schedules the game; confirmation or success dialog expected.

### 20. Close Page and Browser
- **What:** Closes the current page, context, and browser session.
- **Expected result:** Automation process completes and exits cleanly.

---

## Text Inputs Explained

| Text Value         | Where Entered                              | What It Represents              | Why It Is Needed                         |
|--------------------|--------------------------------------------|----------------------------------|------------------------------------------|
| demo@hostnplay.com | Email textbox (login form)                 | User email address               | For authentication purposes              |
| Demo12.            | Password textbox (login form)              | User password                    | For authentication purposes              |
| no-avatar.jpg      | File input (game image upload section)     | Avatar/game cover image filename | Personalizes the game to be created      |
| 20:30              | Time input field (scheduling form)         | Scheduled time                   | Specifies when the game will take place  |

---

## Selectors Used

| Selector/Method                                                      | Target Element                                                                                                  |
|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| `page.get_by_role("link", name="Sign in")`                           | "Sign in" link                                                                                                  |
| `page.get_by_role("textbox", name="Email")`                          | Textbox named "Email"                                                                                            |
| `page.get_by_role("textbox", name="Password")`                       | Textbox named "Password"                                                                                         |
| `page.get_by_role("button", name="Sign in")`                         | "Sign in" button                                                                                                 |
| `page.get_by_role("button", name="Create Game")`                     | "Create Game" button                                                                                             |
| `page.get_by_text("x", exact=True)`                                  | Exact "x" text (usually modal close button)                                                                      |
| `page.get_by_text("Create New Game")`                                | "Create New Game" text (option/button)                                                                           |
| `page.get_by_text("Upload Your ImageClick to")`                      | Upload area/button to upload game image                                                                          |
| `page.locator("body").set_input_files("no-avatar.jpg")`              | File upload field in the body                                                                                    |
| `page.get_by_role("button", name="Open AI")`                         | "Open AI" button for AI game idea suggestions                                                                    |
| `page.locator("div").filter(has_text="Create a competitive Warzone").nth(5)` | 6th div with the text "Create a competitive Warzone" (AI-suggested idea)                                 |
| `page.get_by_role("button").nth(2)`                                 | Third button on the page (pagination/order not clear)                                                            |
| `page.get_by_role("button", name="Next")`                            | "Next" button                                                                                                    |
| `page.get_by_role("button", name="Submit")`                          | "Submit" button                                                                                                  |
| `page.get_by_text("28")`                                             | Text "28" (usually a day on a calendar date picker)                                                              |
| `page.locator("input[type=\"time\"]")`                               | Time input field                                                                                                 |
| `page.get_by_role("button", name="Generate")`                        | "Generate" button                                                                                                |
| `page.get_by_role("button", name="Schedule")`                        | "Schedule" button                                                                                                |

---

## How to Run the Script

Make sure Playwright and its Python package are installed (`pip install playwright`) and the `no-avatar.jpg` file is present in your working directory.

**To run:**
```bash
python CreateGame.py
```

---

## Improvements

### 1. Better Selectors
- Use **specific IDs, data-* attributes, or unique class names** instead of button positions or repeated text to prevent flakiness due to UI changes.
- For example: `page.get_by_test_id("schedule-button")` if available, or CSS selectors with unique values.

### 2. Error Handling
- Add try/except blocks around key actions.
- Use Playwright's assertions or `expect` statements to validate intermediate results (e.g., check for successful login).

### 3. Wait Conditions
- Add explicit waits or use `expect` to **ensure elements are visible and interactable** before clicking or filling.
- For example: `page.wait_for_selector("selector")` or `expect(page.get_by_role("button", name="Next")).to_be_enabled()`.

### 4. Security Improvements
- Do **not hard-code credentials** in plain text. Use **environment variables** or a secrets manager.
- Do not upload sensitive files (hardcoded filenames can reveal paths or leak info).

### 5. Code Organization
- Parameterize variables (email, password, image path).
- Extract repeated actions (like login) into separate functions.
- Add comments for maintainability.

### 6. Reporting and Logging
- Integrate logging of steps and outcomes.
- Capture screenshots on failure for debugging.

---

**End of Documentation**