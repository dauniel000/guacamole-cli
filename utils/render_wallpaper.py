from PIL import Image, ImageDraw, ImageFont
import os
import settings
import uuid
from PIL import ImageFilter


def render_wallpaper(todos):
    prev_wallpaper = None
    if os.path.exists('settings.txt'):
        with open('settings.txt', 'r') as f:
            prev_wallpaper = f.read().strip()

    user_wallpaper_path = getattr(settings, 'USER_WALLPAPER', None)
    if user_wallpaper_path:
        user_wallpaper_path = os.path.expanduser(user_wallpaper_path)
        if not os.path.isabs(user_wallpaper_path):
            user_wallpaper_path = os.path.join(os.path.dirname(os.path.abspath(settings.__file__)), user_wallpaper_path)
    if user_wallpaper_path and os.path.exists(user_wallpaper_path):
        img = Image.open(user_wallpaper_path).convert('RGB')
        img = img.resize((settings.WIDTH, settings.HEIGHT))
    else:
        img = Image.new("RGB", (settings.WIDTH, settings.HEIGHT), settings.BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    # Box dimensions
    box_width = int(settings.WIDTH * 0.35)
    box_height = int(settings.HEIGHT * 0.7)
    box_x = int(settings.WIDTH * 0.08)
    box_y = int((settings.HEIGHT - box_height) / 2)
    box_radius = 30
    box_color = (30, 30, 30, 220)  

    try:

        box_layer = Image.new('RGBA', img.size, (0, 0, 0, 0))
        box_draw = ImageDraw.Draw(box_layer)
        box_draw.rounded_rectangle(
            [box_x, box_y, box_x + box_width, box_y + box_height],
            radius=box_radius, fill=box_color
        )
        img = Image.alpha_composite(img.convert('RGBA'), box_layer)
        draw = ImageDraw.Draw(img)
    except Exception:
        draw.rectangle([box_x, box_y, box_x + box_width, box_y + box_height], fill=box_color[:3])

    try:
        font = ImageFont.truetype("DejaVuSans.ttf", settings.FONT_SIZE)
        title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", settings.FONT_SIZE + 8)
    except IOError:
        font = ImageFont.load_default()
        title_font = font

    text_x = box_x + 30
    text_y = box_y + 30
    draw.text((text_x, text_y), "To-Do List", fill=settings.TEXT_COLOR, font=title_font)
    text_y += settings.FONT_SIZE + 20

    for i, todo in enumerate(todos, start=1):
        draw.text((text_x, text_y), f"{i}. {todo}", fill=settings.TEXT_COLOR, font=font)
        text_y += settings.FONT_SIZE + 12

    new_wallpaper = f"wallpaper_{uuid.uuid4().hex}.png"
    img = img.convert('RGB')
    img.save(new_wallpaper)

    with open('settings.txt', 'w') as f:
        f.write(new_wallpaper)

    if prev_wallpaper and prev_wallpaper != new_wallpaper and os.path.exists(prev_wallpaper):
        try:
            os.remove(prev_wallpaper)
        except Exception as e:
            print(f"Could not remove previous wallpaper: {e}")
    settings.WALLPAPER_FILE = new_wallpaper
