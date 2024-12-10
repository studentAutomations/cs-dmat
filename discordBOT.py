import os
from dhooks import Webhook, Embed, File

image2_path = 'cs-dmat-nova-obavestenja.png'

WEBHOOK_URL = [os.getenv('PB')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[DISKRETNA-MAT forum link - click here -](https://cs.elfak.ni.ac.rs/nastava/mod/forum/view.php?id=4587)**",
        color=0x3498DB
    )

    embed.set_image(url="attachment://cs-dmat-nova-obavestenja.png")
    file = File(image2_path, name="cs-dmat-nova-obavestenja.png")
    hook.send("@everyone 📢 Diskretna", embed=embed, file=file)
