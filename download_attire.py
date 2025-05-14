from icrawler.builtin import GoogleImageCrawler
import os

# Define attire categories and their search queries
categories = {
    'hausa': 'Hausa traditional attire Nigeria',
    'yoruba': 'Yoruba traditional attire Nigeria',
    'igbo': 'Igbo traditional attire Nigeria',
    'fulani': 'Fulani traditional attire Nigeria'
}

# Download images for each category
for label, query in categories.items():
    folder = f'nigerian_attire/{label}'
    print(f"\n🔄 Downloading images for: {label}")
    
    # Create and start the crawler
    crawler = GoogleImageCrawler(storage={'root_dir': folder})
    crawler.crawl(keyword=query, max_num=200)
    
    # Count the number of downloaded images
    num_images = len([
        f for f in os.listdir(folder)
        if f.lower().endswith(('.jpg', '.jpeg', '.png'))
    ])
    
    print(f"✅ {label} — {num_images} images downloaded.")
