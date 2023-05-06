import discord, asyncio
from discord.ext import commands

PREFIX = '.'

client = commands.Bot(command_prefix=PREFIX)

GUILD = client.get_guild(1103015850325331970)

@client.command()
async def ticket(ctx):
    embed = discord.Embed(
        title='Ticket',
        description="Bitte reagiere mit '📨', um ein Ticket zu erstellen."
    )
    
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('📨')

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) == '📨'

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError: # wenn der user mehr als 60s braucht
        await msg.delete()
    else:
        channel = await GUILD.create_text_channel(f'ticket-{ctx.author}')

        ticket_embed = discord.Embed(
            title=f"{ctx.author.mention}'s Ticket",
            description='Bitte schreibe dein Anliegen, damit unser Team sich drum kümmern kann.'
        )

        await channel.send(embed=ticket_embed)




client.run('token')