from PIL import Image

imagem = Image.open(
    "assets/sprites/player/player.png"
).convert("RGBA")

imagem = imagem.crop((384, 0, 1152, 1024))

imagem.save(
    "assets/sprites/player/player_sheet.png"
)

print("Spritesheet preparada com sucesso!")