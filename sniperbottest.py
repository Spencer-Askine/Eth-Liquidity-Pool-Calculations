# Import various libraries.
import os, discord, pandas, requests, cryptocompare
from discord import app_commands
from discord.ext import commands, tasks
from itertools import cycle



# Set the token.
DISCORD_TOKEN = os.getenv('')
cryptocompare.cryptocompare._set_api_key_parameter('')
# Define whatever this is.
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='/', intents=intents)


bot_status = cycle([""])


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.tree.command()
@app_commands.describe(
    percent_token_lp='percent token lp',
    eth_lp='eth lp',
    max_buy='max buy'
)



async def snipe(interaction: discord.Interaction, percent_token_lp: float, eth_lp: float, max_buy: float):
    """Prints the estimated snipe table"""
    
    ethprice = cryptocompare.get_price(['ETH'],['USD'])
    ethprice = ethprice['ETH']
    ethprice = ethprice['USD']
    one = 1
    five = 5
    ten = 10
    fifteen = 15
    twenty = 20
    twenfive = 25
    thrity = 30
    thirtyfive = 35
    forty = 40
    fortyfive = 45
    fifty = 50
    fiftyfive = 55
    sixty = 60
    sixtyfive = 65
    seventy = 70
    seventyfive = 75
    eighty = 80
    eightyfive = 85
    ninety = 90
    ninetyfive = 95
    onehundred = 100

    item = f"""
    ```
+----+----------+----------+----------+
|{"Pos":^4}|{"Cost":^10}|{"Cmltv":^10}|{"Mcap":^10}|
+----+----------+----------+----------+
|{one:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,one),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,one),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,one),max_buy,ethprice)):^10}|
|{five:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,five),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,five),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,five),max_buy,ethprice)):^10}|
|{ten:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,ten),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,ten),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,ten),max_buy,ethprice)):^10}|
|{fifteen:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,fifteen),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,fifteen),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,fifteen),max_buy,ethprice)):^10}|
|{twenty:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,twenty),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,twenty),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,twenty),max_buy,ethprice)):^10}|
|{twenfive:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,twenfive),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,twenfive),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,twenfive),max_buy,ethprice)):^10}|
|{thrity:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,thrity),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,thrity),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,thrity),max_buy,ethprice)):^10}|
|{thirtyfive:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,thirtyfive),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,thirtyfive),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,thirtyfive),max_buy,ethprice)):^10}|
|{forty:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,forty),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,forty),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,forty),max_buy,ethprice)):^10}|
|{fortyfive:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,fortyfive),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,fortyfive),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,fortyfive),max_buy,ethprice)):^10}|
|{fifty:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,fifty),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,fifty),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,fifty),max_buy,ethprice)):^10}|
|{fiftyfive:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,fiftyfive),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,fiftyfive),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,fiftyfive),max_buy,ethprice)):^10}|
|{sixty:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,sixty),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,sixty),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,sixty),max_buy,ethprice)):^10}|
|{sixtyfive:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,sixtyfive),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,sixtyfive),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,sixtyfive),max_buy,ethprice)):^10}|
|{seventy:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,seventy),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,seventy),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,seventy),max_buy,ethprice)):^10}|
|{seventyfive:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,seventyfive),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,seventyfive),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,seventyfive),max_buy,ethprice)):^10}|
|{eighty:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,eighty),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,eighty),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,eighty),max_buy,ethprice)):^10}|
|{eightyfive:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,eightyfive),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,eightyfive),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,eightyfive),max_buy,ethprice)):^10}|
|{ninety:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,ninety),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,ninety),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,ninety),max_buy,ethprice)):^10}|
|{ninetyfive:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,ninetyfive),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,ninetyfive),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,ninetyfive),max_buy,ethprice)):^10}|
|{onehundred:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,onehundred),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,onehundred),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,ninetyfive),max_buy,ethprice)):^10}|
+----+----------+----------+----------+
    ```
    """
    embed = discord.Embed(title="__Token LP:__ "  + str(percent_token_lp) + "%" + " | __Eth LP:__ " +str(eth_lp) + " | __Max Buy:__ "  + str(max_buy) + "%",
                          color=discord.Color.red())
    embed.add_field(name="", value = item)
    wiki_image = "https://media.tenor.com/9hd9gB_WFqIAAAAC/sniper-pubg.gif"
    embed.set_thumbnail(url=wiki_image)
    embed.set_footer(text="Made by the worst dev ever")                  
    
    await interaction.response.send_message(embed=embed)

@client.tree.command()
@app_commands.describe(
    percent_token_lp='percent token lp',
    eth_lp='eth lp',
    max_buy='max buy'
)
async def mobilesnipe(interaction: discord.Interaction, percent_token_lp: float, eth_lp: float, max_buy: float):
    """Prints the estimated snipe table"""
    
    ethprice = cryptocompare.get_price(['ETH'],['USD'])
    ethprice = ethprice['ETH']
    ethprice = ethprice['USD']
    one = 1
    five = 5
    ten = 10
    fifteen = 15
    twenty = 20
    twenfive = 25
    thrity = 30
    thirtyfive = 35
    forty = 40
    fortyfive = 45
    fifty = 50
    fiftyfive = 55
    sixty = 60
    sixtyfive = 65
    seventy = 70
    seventyfive = 75
    eighty = 80
    eightyfive = 85
    ninety = 90
    ninetyfive = 95
    onehundred = 100

    item = f"""
    ```
+---+---------+---------+
|{"Pos":^3}|{"Cost":^9}|{"Mcap":^9}|
+---+---------+---------+
|{one:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,one),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,one),max_buy,ethprice)):^9}|
|{five:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,five),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,five),max_buy,ethprice)):^9}|
|{ten:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,ten),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,ten),max_buy,ethprice)):^9}|
|{fifteen:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,fifteen),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,fifteen),max_buy,ethprice)):^9}|
|{twenty:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,twenty),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,twenty),max_buy,ethprice)):^9}|
|{twenfive:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,twenfive),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,twenfive),max_buy,ethprice)):^9}|
|{thrity:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,thrity),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,thrity),max_buy,ethprice)):^9}|
|{thirtyfive:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,thirtyfive),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,thirtyfive),max_buy,ethprice)):^9}|
|{forty:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,forty),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,forty),max_buy,ethprice)):^9}|
|{fortyfive:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,fortyfive),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,fortyfive),max_buy,ethprice)):^9}|
|{fifty:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,fifty),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,fifty),max_buy,ethprice)):^9}|
|{fiftyfive:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,fiftyfive),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,fiftyfive),max_buy,ethprice)):^9}|
|{sixty:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,sixty),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,sixty),max_buy,ethprice)):^9}|
|{sixtyfive:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,sixtyfive),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,sixtyfive),max_buy,ethprice)):^9}|
|{seventy:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,seventy),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,seventy),max_buy,ethprice)):^9}|
|{seventyfive:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,seventyfive),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,seventyfive),max_buy,ethprice)):^9}|
|{eighty:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,eighty),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,eighty),max_buy,ethprice)):^9}|
|{eightyfive:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,eightyfive),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,eightyfive),max_buy,ethprice)):^9}|
|{ninety:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,ninety),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,ninety),max_buy,ethprice)):^9}|
|{ninetyfive:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,ninetyfive),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,ninetyfive),max_buy,ethprice)):^9}|
|{onehundred:^3}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,onehundred),4):^9}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,ninetyfive),max_buy,ethprice)):^9}|
+---+---------+---------+
    ```
    """
    embed = discord.Embed(title="__Token LP:__ "  + str(percent_token_lp) + "%" + " | __Eth LP:__ " +str(eth_lp) + " | __Max Buy:__ "  + str(max_buy) + "%",
                          color=discord.Color.red())

    embed.add_field(name="", value = item)
    wiki_image = "https://media.tenor.com/9hd9gB_WFqIAAAAC/sniper-pubg.gif"
    
    embed.set_thumbnail(url=wiki_image)
    embed.set_footer(text="Made by the worst dev ever")                  
    
    await interaction.response.send_message(embed=embed)


def buycost(x,y,z,d,f):
    if((f*z) >= x):
        totalcost = 0
    else:
        while (f > d):
            totalcost = ((x*y) / (x - z)) - y
            x = x-z
            y = y + totalcost
            d = d+1
    return totalcost
def totalbuys(x,y,z,d,f):
    totalbuys = 0
    if((f*z) >= x):
        totalbuys = 0
    else:
        while (f > d):
            totalcost = ((x*y) / (x - z)) - y
            x = x-z
            y = y + totalcost
            d = d+1
            totalbuys = totalbuys + totalcost
    return totalbuys


def Mcap(g,h,e):
    #MCAP = cost / max txn * eth price
    mcap = g / (h *0.01) * e
    return mcap

def pcsnipeloop(x,y,z,d,f):
    while((f*z) >= x):
        print(|{one:^4}|{round(buycost(percent_token_lp,eth_lp,max_buy,0,one),4):^10}|{round(totalbuys(percent_token_lp,eth_lp,max_buy,0,one),4):^10}|{round(Mcap(buycost(percent_token_lp,eth_lp,max_buy,0,one),max_buy,ethprice)):^10}|")


@client.event
async def on_ready():
   client.change_presence(status=discord.Status.online)
   print(f'We have logged in as {client.user}')
   change_status.start()
   await client.tree.sync()




client.run('')




