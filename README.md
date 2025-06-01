# 🛡️ Discord Server Management Bot

A **Discord bot** built with Python and `discord.py` to help manage server roles, verification, rules, applications, info panels, and suggestions.  
It uses **persistent views**, interactive menus, and admin commands to make server management smooth.

---

## ✨ Features

- ✅ **Verification system** — click to unlock server access  
- ⚙️ **Role menus** — users choose ping categories  
- 📜 **Rules embed** — sends detailed server rules  
- 📝 **Staff applications** — share links for helper/builder roles  
- ℹ️ **Server info** — show essential details like IP, store, ports  
- 💡 **Suggestions** — users submit suggestions + voting reactions  
- 🔒 **Admin commands** — only Admin role can trigger embeds

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+  
- `discord.py` (`pip install discord.py`)  
- Discord bot token  
- Set environment variables:
  - `API_TOKEN` — your bot token  
  - `MY_GUILD` — your Discord server ID  
  - `SUGGESTIONS_CHANNEL` — suggestions channel ID

---

### 🏗️ Installation

1️⃣ Clone the repository:
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
2️⃣ Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Set environment variables (choose one method):

Terminal:

bash
Copy
Edit
export API_TOKEN=your_bot_token
export MY_GUILD=your_guild_id
export SUGGESTIONS_CHANNEL=your_channel_id
.env file (create a file called .env):

ini
Copy
Edit
API_TOKEN=your_bot_token
MY_GUILD=your_guild_id
SUGGESTIONS_CHANNEL=your_channel_id
4️⃣ Run the bot:

bash
Copy
Edit
python main.py
📂 Project Structure
bash
Copy
Edit
.
├── main.py               # Main bot code
├── views.py              # Persistent view (buttons/menus)
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── keep_alive.py (opt)   # Optional: keep bot alive on some hosts
⚙️ Commands
Command	Description	Permissions
/verify_menu	Sends verification embed with check button	Admin only
/rules_menu	Sends rules embed	Admin only
/applications_menu	Sends staff applications embed	Admin only
/info_menu	Sends server info embed	Admin only
/role_menu	Sends role selector embed with buttons	Admin only
/embed	Sends a custom embed (template)	Admin only
/suggest	Lets users submit suggestions	Everyone

🧩 Customization
Embeds: Modify titles, fields, and descriptions in main.py

Buttons & roles: Edit VerificationMenu and RolesMenu in views.py

Permissions: Adjust @commands.has_role("Admin") decorators as needed

📦 Dependencies
discord.py

Python os, typing

To install:

bash
Copy
Edit
pip install discord.py
📜 License
Released under the MIT License.

💬 Contributing
Feel free to:

Open issues for bugs or suggestions

Submit pull requests

Fork the project and build your own
