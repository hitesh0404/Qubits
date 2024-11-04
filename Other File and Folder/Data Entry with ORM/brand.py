from yourapp.models import Brand
from datetime import date

# List of 20 electronic brands
brands_data = [
    {"name": "Apple", "tagline": "Think Different", "since": date(1976, 4, 1), "types": "PB", "origin": "Los Altos, California, USA", "logo": "/images/brand/logo/apple.png"},
    {"name": "Samsung", "tagline": "Imagine the Possibilities", "since": date(1938, 3, 1), "types": "PB", "origin": "Seoul, South Korea", "logo": "/images/brand/logo/samsung.png"},
    {"name": "Sony", "tagline": "Make Believe", "since": date(1946, 5, 7), "types": "PB", "origin": "Tokyo, Japan", "logo": "/images/brand/logo/sony.png"},
    {"name": "LG", "tagline": "Life's Good", "since": date(1958, 10, 1), "types": "PB", "origin": "Seoul, South Korea", "logo": "/images/brand/logo/lg.png"},
    {"name": "Dell", "tagline": "Yours is Here", "since": date(1984, 2, 1), "types": "PB", "origin": "Round Rock, Texas, USA", "logo": "/images/brand/logo/dell.png"},
    {"name": "Microsoft", "tagline": "Be What's Next", "since": date(1975, 4, 4), "types": "PB", "origin": "Redmond, Washington, USA", "logo": "/images/brand/logo/microsoft.png"},
    {"name": "HP", "tagline": "Keep Reinventing", "since": date(1939, 1, 1), "types": "PB", "origin": "Palo Alto, California, USA", "logo": "/images/brand/logo/hp.png"},
    {"name": "Lenovo", "tagline": "For Those Who Do", "since": date(1984, 11, 1), "types": "PB", "origin": "Beijing, China", "logo": "/images/brand/logo/lenovo.png"},
    {"name": "Asus", "tagline": "In Search of Incredible", "since": date(1989, 4, 2), "types": "PB", "origin": "Taipei, Taiwan", "logo": "/images/brand/logo/asus.png"},
    {"name": "Acer", "tagline": "Explore Beyond Limits", "since": date(1976, 8, 1), "types": "PB", "origin": "Taipei, Taiwan", "logo": "/images/brand/logo/acer.png"},
    {"name": "Xiaomi", "tagline": "Innovation for Everyone", "since": date(2010, 4, 6), "types": "PB", "origin": "Beijing, China", "logo": "/images/brand/logo/xiaomi.png"},
    {"name": "OnePlus", "tagline": "Never Settle", "since": date(2013, 12, 17), "types": "PB", "origin": "Shenzhen, China", "logo": "/images/brand/logo/oneplus.png"},
    {"name": "Vivo", "tagline": "Camera & Music", "since": date(2009, 11, 1), "types": "PB", "origin": "Dongguan, China", "logo": "/images/brand/logo/vivo.png"},
    {"name": "Oppo", "tagline": "The Art of Technology", "since": date(2004, 10, 1), "types": "PB", "origin": "Dongguan, China", "logo": "/images/brand/logo/oppo.png"},
    {"name": "Huawei", "tagline": "Building a Better Connected World", "since": date(1987, 9, 15), "types": "PB", "origin": "Shenzhen, China", "logo": "/images/brand/logo/huawei.png"},
    {"name": "Google", "tagline": "Do the Right Thing", "since": date(1998, 9, 4), "types": "PB", "origin": "Mountain View, California, USA", "logo": "/images/brand/logo/google.png"},
    {"name": "Amazon", "tagline": "Work Hard. Have Fun. Make History.", "since": date(1994, 7, 5), "types": "PB", "origin": "Seattle, Washington, USA", "logo": "/images/brand/logo/amazon.png"},
    {"name": "Panasonic", "tagline": "A Better Life, A Better World", "since": date(1918, 3, 13), "types": "PB", "origin": "Osaka, Japan", "logo": "/images/brand/logo/panasonic.png"},
    {"name": "Toshiba", "tagline": "Leading Innovation", "since": date(1939, 9, 1), "types": "PB", "origin": "Tokyo, Japan", "logo": "/images/brand/logo/toshiba.png"},
    {"name": "Philips", "tagline": "Innovation and You", "since": date(1891, 5, 15), "types": "PB", "origin": "Amsterdam, Netherlands", "logo": "/images/brand/logo/philips.png"}
]

# Adding brands to the database
for brand in brands_data:
    Brand.objects.create(
        name=brand["name"],
        tagline=brand["tagline"],
        since=brand["since"],
        types=brand["types"],
        origin=brand["origin"],
        logo=brand["logo"]
    )

print("20 electronic brands added successfully!")
