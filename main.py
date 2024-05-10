import os
import discord
from discord import app_commands

TOKEN = "YOUR TOKEN HERE"

class aclient(discord.Client):

    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False  #we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:  #check if slash commands have been synced
            await tree.sync(
            )  #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        print(f"We have logged in as {self.user}.")


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(
    name='calc',
    description="Calculate your fish gems or mining gems to bytecoin.")
@app_commands.describe(total_gems="Your total fish gems or mine gems",
                       rate_gems="Rate gems.",
                       rate_bytecoin="Rate bytecoin")
async def create_channels(ctx, total_gems: str, rate_gems: str,
                          rate_bytecoin: str):
    total_gems = float(total_gems)
    rate_gems = float(rate_gems)
    rate_bytecoin = float(rate_bytecoin)
    embed = discord.Embed(
        title="✨Pixel World Bytecoin Calculator ✨",
        description=
        f'The total of `{float(total_gems):,}\U0001F48E` at a rate of `{float(rate_gems)}/{float(rate_bytecoin)}` is `{float(total_gems)/float(rate_gems)*float(rate_bytecoin):,.2f} bytecoin(s) \U0001F4B5.`\n\n> Another rate such as\n> `100/250` | `{float(total_gems)/float(100)*float(250):,.2f} bytecoin(s)`\n> `90/250` | `{float(total_gems)/float(90)*float(250):,.2f} bytecoin(s)` \n> `80/250` | `{float(total_gems)/float(80)*float(250):,.2f} bytecoin(s)`\n> `70/250` | `{float(total_gems)/float(70)*float(250):,.2f} bytecoin(s)`\n> `60/250` | `{float(total_gems)/float(60)*float(250):,.2f} bytecoin(s)`\n> `50/250` | `{float(total_gems)/float(50)*float(250):,.2f} bytecoin(s)`\n> `40/250` | `{float(total_gems)/float(40)*float(250):,.2f} bytecoin(s)`\n> `30/250` | `{float(total_gems)/float(30)*float(250):,.2f} bytecoin(s)`\n> `20/250` | `{float(total_gems)/float(20)*float(250):,.2f} bytecoin(s)`\n> `10/250` | `{float(total_gems)/float(10)*float(250):,.2f} bytecoin(s)`\n\n Bot created by [reimoo06](https://github.com/reimoo06)',
        colour=0x00b0f4)

    embed.set_image(
        url=
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQul1PFrdDsRrlVL37DU3B_mYJrrS5JjpwiT7FQhNxhtHhko6519y_M2GesZZEJ_5y3vA"
    )
    embed.set_footer(text="Thanks for using this bot!")
    await ctx.response.send_message(embed=embed)


client.run(TOKEN)
