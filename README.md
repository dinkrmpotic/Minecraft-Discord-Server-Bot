🛡️ Discord Server Management Bot
This is a Discord bot built with Python and discord.py that helps manage server roles, verification, rules, applications, info panels, and suggestion tracking.
It uses persistent views, custom menus, and admin commands to streamline server interactions.

✨ Features
✅ Verification System — Easy access gating with a checkmark
⚙️ Role Menus — Let users choose what they want to be pinged for
📜 Rules Embed — Auto-send server rules with detailed sections
📝 Staff Applications — Share links to helper/builder application forms
ℹ️ Server Info — Provide essential server details and key links
💡 Suggestions Channel — Allow users to submit suggestions with voting reactions
🔒 Admin Commands — Only users with the Admin role can trigger key embeds

🚀 Getting Started
Prerequisites
Python 3.8+

discord.py (pip install discord.py)

Discord bot token

.env file or environment variables set:

API_TOKEN — your bot token

MY_GUILD — your Discord server ID

SUGGESTIONS_CHANNEL — the channel ID where suggestions are sent

🏗️ Installation

1️⃣ Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

3️⃣ Set environment variables (or create a .env file)
bash
Copy
Edit
export API_TOKEN=your_bot_token
export MY_GUILD=your_guild_id
export SUGGESTIONS_CHANNEL=your_channel_id

4️⃣ Run the bot
bash
Copy
Edit
python main.py
📂 Project Structure
cpp
Copy
Edit
.
├── main.py
├── views.py
├── requirements.txt
├── README.md
└── (optional) keep_alive.py
main.py — main bot logic and commands

views.py — defines custom persistent views (button handlers)

keep_alive.py — optional file to keep bot running on some platforms

⚙️ Commands Overview
Command	Description	Permissions
/verify_menu	Sends verification embed with check button	Admin only
/rules_menu	Sends rules embed	Admin only
/applications_menu	Sends staff applications embed	Admin only
/info_menu	Sends server info embed	Admin only
/role_menu	Sends role selector embed with buttons	Admin only
/embed	Sends a custom embed (template)	Admin only
/suggest	Allows users to submit suggestions	Everyone

🛠️ Customization
Embeds & fields: Edit the embed sections in main.py to customize titles, descriptions, and links.

Views & buttons: Modify or extend the VerificationMenu and RolesMenu in views.py to add more buttons or role interactions.

Permissions: The bot uses role checks (@commands.has_role("Admin")) — adjust as needed.

🧩 Dependencies
discord.py

Python standard library (os, typing)

📄 License
This project is open-source and available under the MIT License.

💬 Contact
Feel free to open an issue or submit a pull request if you want to contribute!
For questions, DM the server admin or file a GitHub issue.
