import discord 
class VerificationMenu(discord.ui.View):
    def __init__(self,guild):
        super().__init__(timeout=None)
        self.value = None
        self.guild = guild
        self.generate_roles()
    def generate_roles(self):
        self.verified = discord.utils.get(self.guild.roles, name="Verified")

    @discord.ui.button(label="Verify", style=discord.ButtonStyle.green,emoji="✅",  custom_id='persistent_view:verify')
    async def verify_menu(self, interaction:discord.Interaction, button:discord.ui.Button,):
        await interaction.user.add_roles(self.verified)
        await interaction.response.send_message("You have been verified", delete_after=3, silent=True)

class RolesMenu(discord.ui.View):
    def __init__(self,guild):
        super().__init__(timeout=None)
        self.value = None
        self.guild = guild
        self.generate_roles()
    def generate_roles(self):
        self.updates_role = discord.utils.get(self.guild.roles, name="Updates")
        self.events_role = discord.utils.get(self.guild.roles, name="Events")
        self.giveaway_role = discord.utils.get(self.guild.roles, name="Giveaways")
        self.polls_role = discord.utils.get(self.guild.roles, name="Polls")
        

    @discord.ui.button(label="Updates", style=discord.ButtonStyle.gray,emoji="🔧",  custom_id='roles_menu:updates')
    async def updates_button(self, interaction:discord.Interaction, button:discord.ui.Button,):
        if self.updates_role in interaction.user.roles:
            await interaction.user.remove_roles(self.updates_role)
            await interaction.response.send_message(f"{interaction.user.display_name} removed a role: Updates", delete_after=3, silent=True)
        else:  
            await interaction.user.add_roles(self.updates_role)
            await interaction.response.send_message(f"{interaction.user.display_name} now has a role: Updates", delete_after=3, silent=True)
    
    
    @discord.ui.button(label="Events", style=discord.ButtonStyle.red,emoji="🏆",  custom_id='roles_menu:events')
    async def events_button(self, interaction:discord.Interaction, button:discord.ui.Button,):
        if self.events_role in interaction.user.roles:
            await interaction.user.remove_roles(self.events_role)
            await interaction.response.send_message(f"{interaction.user.display_name} removed a role: Events", delete_after=3, silent=True)
        else:  
            await interaction.user.add_roles(self.events_role)
            await interaction.response.send_message(f"{interaction.user.display_name} now has a role: Events", delete_after=3, silent=True)


    @discord.ui.button(label="Polls", style=discord.ButtonStyle.green,emoji="📊",  custom_id='roles_menu:polls')
    async def polls_button(self, interaction:discord.Interaction, button:discord.ui.Button,):
        if self.polls_role in interaction.user.roles:
            await interaction.user.remove_roles(self.polls_role)
            await interaction.response.send_message(f"{interaction.user.display_name} removed a role: Polls", delete_after=3, silent=True)
        else:  
            await interaction.user.add_roles(self.polls_role)
            await interaction.response.send_message(f"{interaction.user.display_name} now has a role: Polls", delete_after=3, silent=True)