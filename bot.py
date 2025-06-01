from typing import Optional
import discord
from discord.ext import commands
import os
from views import VerificationMenu, RolesMenu
#from keep_alive import keep_alive

class PersistentViewBot(commands.Bot):

  def __init__(self):
    intents = intents = discord.Intents.all()
    intents.message_content = True
    super().__init__(command_prefix='/', intents=intents)

  async def setup_hook(self) -> None:
    # Register the persistent view for listening here.
    # Note that this does not send the view to any message.
    # In order to do this you need to first send a message with the View, which is shown below.
    # If you have the message_id you can also pass it as a keyword argument, but for this example
    # we don't have one.
    print("setting up hooks")
    for server in self.guilds:
      print(server)
    guild = await self.fetch_guild(os.environ['MY_GUILD'])
    print(f"guild: {guild}")
    self.add_view(view=VerificationMenu(guild))
    self.add_view(RolesMenu(guild))


TOKEN = os.environ['API_TOKEN']
SUGGESTIONS_CHANNEL = os.environ['SUGGESTIONS_CHANNEL']


def run_discord_bot():
  TOKEN = os.environ['API_TOKEN']
  #bot = commands.Bot(intents=discord.Intents.all(), command_prefix="/")
  bot = PersistentViewBot()

  @bot.event
  async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('play.example.org'))

  @bot.command()
  @commands.has_role("Admin")
  async def verify_menu(ctx):
    #send embed message
    channel = bot.get_channel(ctx.channel.id)
    embed = discord.Embed(title="HOW TO GAIN ACCESS OUR SERVER?",
                          description=f"""*To gain access to the rest of the discord server, click the check mark below!\nAfter reacting to the check mark below, you should have access to the rest of the server*
        """,
                          color=discord.Color.purple())
    #embed.add_field(name = chr(173), value = chr(173))
    embed.add_field(
        name="",
        value="",
        inline=False)
    embed.add_field(
        name="",
        value="",
        inline=False)
    embed.add_field(
        name="ENCOUNTERING ISSUES?",
        value=
        f"*If you are having any issues, Please DM any of the staff here or in-game!*",
        inline=False)
    #embed.add_field(name = "", value=f"*If you are having any issues, Please DM any of the staff here or in-game!*",inline=False)
    #send buttons
    view = VerificationMenu(await bot.fetch_guild(os.environ['MY_GUILD']))
    await channel.send(embed=embed, view=view)

  @bot.command()
  @commands.has_role("Admin")
  async def rules_menu(ctx):
    #send embed message
    channel = bot.get_channel(ctx.channel.id)
    embed = discord.Embed(title="X | Server Rules",
                          description=f"",
                          color=discord.Color.purple())

    embed.add_field(
        name="",
        value=
        f"",
        inline=False)
    embed.add_field(
        name="",
        value=
        f"",
        inline=False)
    embed.add_field(
        name=":bookmark:**  Here are some less in-depth, more generic, Discord-specific rules:**",
        value=
        f"",
        inline=False)
    embed.add_field(
        name="",
        value=
        f"",
        inline=False)
    embed.add_field(
        name="",
        value=
        f"**[1]** No spam or self-promotion (server invites, advertisements, etc..) without permission from a staff member. This ESPECIALLY includes DMing fellow members",
        inline=False)
    embed.add_field(
        name="",
        value=
        f"**[2]** Treat everyone with respect. Absolutely no harassment, witch hunting, sexism, racism, homophobia or any kind of hate speech",
        inline=False)
    embed.add_field(
        name="",
        value=
        f"**[3]** No NSFW or obscene content. This includes text, images, or links featuring nudity, sex, hard violence, or other graphically disturbing content.",
        inline=False)
    embed.add_field(
        name="",
        value=
        f"**[4]** Do not attempt to mention @everyone, @here, or attempt to mass mention. You may mention staff in case of an emergency.",
        inline=False)
    embed.add_field(
        name="",
        value=
        f"**[5]** Do not talk about sensitive topics such as suicide, drugs, politics etc...",
        inline=False)
    embed.add_field(
        name="",
        value=
        f"**[6]** If you encourage anything related to suicide, even as a joke you will be punished heavily without warning.",
        inline=False)
    embed.add_field(
        name="",
        value=
        f"**[7]** Do not play excessively loud videos with the music bots and keep the music bot in the radio channel.",
        inline=False)
    embed.add_field(
        name="",
        value=
        f"**[8]** Sending/linking any harmful material such as viruses, IP grabbers etc.. will result in a permanent ban. Any attempts to DDOX anyone (sending private/personal information) will result in the same punishment.",
        inline=False)
    embed.add_field(
        name="",
        value=
        f"**[9]** Keep it family friendly. The whole goal of X is to provide a safe, family friendly environment for everyone. Please help us keep it that way.",
        inline=False)
    embed.add_field(
        name="",
        value=
        f"**[10]** If you see something against the rules or something that makes you feel unsafe, let staff know! We want this server to be a safe and welcoming space!",
        inline=False)
    await channel.send(embed=embed)
    embed.add_field(
        name="",
        value=
        f"*Please be sure to check out the rules! Remember, not knowing the rules is not an excuse for breaking them, thank you!*",
        inline=False)
    await channel.send(embed=embed)

  @bot.command()
  @commands.has_role("Admin")
  async def applications_menu(ctx):
    #send embed message
    channel = bot.get_channel(ctx.channel.id)
    embed = discord.Embed(title="Staff Applications",
                          description=f"""**__Click the links below to apply for staff!__**""",
                          color=discord.Color.purple())
    #embed.add_field(name = chr(173), value = chr(173))
    embed.add_field(
        name="",
        value="",
        inline=False)
    embed.add_field(
        name="**__Helper Applications__**",
        value=
        f"example link",
        inline=False)
    embed.add_field(
        name="",
        value="",
        inline=False)
    embed.add_field(
        name="**__Builder Applications__**",
        value=
        f"example link",
        inline=False)
    embed.add_field(
        name="",
        value="",
        inline=False)
    embed.add_field(
        name="",
        value=
        f"*Please note, staff applications take time to review. Please do not spam staff about your application and for them to review it, this will cause in an instant denial of your app. A decision for your application will be made with-in **7 days**. If your app has been denied, you may re-apply in **14 days**. Best of luck!*",
        inline=False)
    #embed.add_field(name = "", value=f"*If you are having any issues, Please DM any of the staff here or in-game!*",inline=False)
    #send buttons
    await channel.send(embed=embed)

  @bot.command()
  @commands.has_role("Admin")
  async def info_menu(ctx):
    #send embed message
    channel = bot.get_channel(ctx.channel.id)
    embed = discord.Embed(title="Information",
                          description=f"""""",
                          color=discord.Color.purple())
    #embed.add_field(name = chr(173), value = chr(173))
    embed.add_field(
        name="",
        value="",
        inline=False)
    embed.add_field(
        name="",
        value=
        f"X is a small friendly survival server that aims to provide your classic minecraft survival experience. The server offers a player-driven economy, which gives everyone a chance to buy/sell items independently.",
        inline=False)
    embed.add_field(
        name="",
        value=
        f"For extra comfort and safety of our players we offer grief protection so our players can protect their builds, homes and land.",
        inline=False)
    embed.add_field(
        name="",
        value=
        f"We are not a pay to win server. We offer a free to play experience for everyone with vote ranks, extra perks, amazing crate rewards that can all be obtained with votes and in-game currency.",
        inline=False)
    embed.add_field(
        name="",
        value="",
        inline=False)
    embed.add_field(
        name="**__Important Info__**",
        value=
        f"",
        inline=False)
    embed.add_field(
        name="",
        value="Server IP  -  \nBedrock Port  - \nStore - ",
        inline=False)
    #embed.add_field(name = "", value=f"*If you are having any issues, Please DM any of the staff here or in-game!*",inline=False)
    #send buttons
    await channel.send(embed=embed)
    
  @bot.command()
  @commands.has_role("Admin")
  async def role_menu(ctx):
    #send embed message
    channel = bot.get_channel(ctx.channel.id)
    embed = discord.Embed(
        title="Get Pinged for roles",
        description=
        f"""**__Click the button below to select what you want to get pinged for!__**""",
        color=discord.Color.purple())
    embed.add_field(
        name="",
        value="",
        inline=False)
    embed.add_field(
        name=
        " 🔧 | Updates - Get pings about changes that occur in the Discord and Minecraft servers ",
        value=f"",
        inline=False)
    embed.add_field(
        name="",
        value="",
        inline=False)
    embed.add_field(
        name=" 🏆 | Events - Get pinged about upcoming events  ",
        value=f"",
        inline=False)
    embed.add_field(
        name="",
        value="",
        inline=False)
    embed.add_field(
        name="",
        value="",
        inline=False)
    embed.add_field(name=" 📊 | Polls - Get pinged when a poll is released ",
                    value=f"",
                    inline=False)
    #send buttons
    view = RolesMenu(await bot.fetch_guild(os.environ['MY_GUILD']))
    await channel.send(embed=embed, view=view)

  #mozes copy pastea ovo i urediti napravit custom embed
  #isto moras stopat code i ponovo runnat. runnas main.py, NE bot.py
  @bot.command()
  @commands.has_role("Admin")
  async def embed(
      ctx,
      member: discord.Member = None):  #promjeni ovdje embed u ime commanda
    if member == None:
      member = ctx.author
    name = member.display_name  #
    pfp = member.display_avatar
    embed = discord.Embed(title="Embeded title",
                          description="Embed descr",
                          color=discord.Color.red())
    embed.set_author(name=name)  #ak oces ime u coreneru, ak ne stavi # ispred
    embed.set_thumbnail(url=pfp)  #isto za sliku
    embed.add_field(
        name="field 1", value="Field value", inline=False
    )  #ovdje radi novi field, probaj kak je stavit samo name (to je title) i kak je value
    embed.add_field(name="field 2 inline", value="Field value",
                    inline=True)  #inline znaci u istom redu ko gornji field
    #embed.set_footer(text = "embed_footer")  # ak oces prljavi footer
    #posalje embed u isti channel u koji si poslao comman
    await ctx.send(embed=embed)

  @bot.command()
  async def suggest(ctx):
    member = ctx.author
    name = member.display_name
    pfp = member.display_avatar
    embed = discord.Embed(title=f"Suggestion by {name}",
                          description=ctx.message.content[9:],
                          color=discord.Color.red())
    channel = bot.get_channel(int(os.environ['SUGGESTIONS_CHANNEL']))
    sent_channel_message = await channel.send(embed=embed)
    await sent_channel_message.add_reaction("✅")
    await sent_channel_message.add_reaction("❌")

  #keep_alive()
  bot.run(TOKEN)
