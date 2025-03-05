from PIL import Image, ImageFilter

# Carregar a imagem original
image_path = "" #coloque o caminho da sua imagem aqui
image = Image.open(image_path).convert("RGBA")

# Definir o tamanho expandido para criar espaço entre a imagem e o contorno
border_size = 30  # Distância entre a imagem e o contorno
expanded_size = (image.width + 2 * border_size, image.height + 2 * border_size)

# Criar uma nova imagem maior e colar a imagem original no centro
expanded_image = Image.new("RGBA", expanded_size, (0, 0, 0, 0))
expanded_image.paste(image, (border_size, border_size))

# Criar uma máscara da imagem expandida para o contorno
expanded_alpha = expanded_image.split()[3]
outline = expanded_alpha.filter(ImageFilter.MaxFilter(29))  # Criar um efeito de contorno

# Criar uma nova imagem para o contorno preto
outline_image = Image.new("RGBA", expanded_size, (0, 0, 0, 0))
for y in range(expanded_size[1]):
    for x in range(expanded_size[0]):
        if outline.getpixel((x, y)) > 0:
            outline_image.putpixel((x, y), (0, 0, 0, 255))  # Define a cor do contorno como preto

# Remover a imagem original da área central para manter o espaço entre o contorno e a imagem
cutout_alpha = expanded_alpha.filter(ImageFilter.MaxFilter(17))  # Expande a máscara para "apagar" o centro
for y in range(expanded_size[1]):
    for x in range(expanded_size[0]):
        if cutout_alpha.getpixel((x, y)) > 0:
            outline_image.putpixel((x, y), (0, 0, 0, 0))  # Define a área central como transparente

# Combinar o contorno e a imagem original
final_image = Image.alpha_composite(outline_image, expanded_image)

# Salvar a nova imagem
output_path_final_updated = "" #coloque o caminho de sua imagem vai ser salva e o nome que irá salvar
final_image.save(output_path_final_updated)

print(f"Imagem processada salva em: {output_path_final_updated}")
