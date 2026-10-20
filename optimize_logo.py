
from pathlib import Path
from PIL import Image

# Keep the original logo unchanged.
logo_path = Path("assets/images/logo/pikop-logo.png")
output_path = Path("assets/images/logo/pikop-logo.webp")

with Image.open(logo_path) as image:
    image = image.convert("RGBA")

    # The logo is displayed at 216 × 72 CSS pixels.
    # Export at 2× size for sharper high-density screens.
    image.thumbnail((432, 144), Image.Resampling.LANCZOS)

    image.save(
        output_path,
        "WEBP",
        quality=85,
        method=6,
    )

print(f"Original logo: {logo_path}")
print(f"Optimized logo: {output_path}")
print(f"New dimensions: {image.size[0]} × {image.size[1]} pixels")
print(f"Optimized file size: {output_path.stat().st_size / 1024:.1f} KiB")
