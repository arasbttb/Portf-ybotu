import discord
from discord.ext import commands
from discord import ui, ButtonStyle, TextStyle
from config import TOKEN

# Modal tanımı
class TestModal(ui.Modal, title='Test başlık'):
    field_1 = ui.TextInput(label='Kısa metin')
    field_2 = ui.TextInput(label='Uzun metin', style=TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        # Modal verilerini interaction üzerinden gönder
        await interaction.response.send_message(
            f"✅ Modal gönderildi!\nKısa metin: {self.field_1.value}\nUzun metin: {self.field_2.value}",
            ephemeral=True
        )

# Buton tanımı
class TestButton(ui.Button):
    def __init__(self, label="Test etiketi", style=ButtonStyle.blurple, row=0):
        super().__init__(label=label, style=style, row=row)

    async def callback(self, interaction: discord.Interaction):
        # Modal'ı ilk yanıt olarak aç
        await interaction.response.send_modal(TestModal())

        # DM denemesi (modal açıldıktan sonra)
        try:
            await interaction.user.send("Bir butona bastınız")
        except discord.Forbidden:
            print("DM gönderilemedi: Kullanıcı engellemiş olabilir.")

        # Kanal mesajı (isteğe bağlı)
        await interaction.channel.send(f"{interaction.user.mention} butona bastı.")

# View tanımı
class TestView(ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(TestButton())

# Bot yapılandırması
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı')

@bot.command()
async def test(ctx):
    await ctx.send("Aşağıdaki butona tıklayın:", view=TestView())

bot.run(TOKEN)
