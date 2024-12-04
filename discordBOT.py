import os
from dhooks import Webhook, Embed, File

image2_path = 'cs-dmat-nova-obavestenja.png'

WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN'), os.getenv('WEBHOOK_OTHER1')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[CS link](https://cs.elfak.ni.ac.rs/nastava/)**",
        color=0x3498DB
    )

    embed.set_image(url="attachment://cs-dmat-nova-obavestenja.png")
    file = File(image2_path, name="cs-dmat-nova-obavestenja.png")
    hook.send("**@everyone 📢 Diskretna**", embed=embed, file=file)
