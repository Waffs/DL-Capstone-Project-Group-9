from icrawler.builtin import GoogleImageCrawler
import os

# Dictionary with each label and multiple related search keywords
attire_keywords = {
    'hausa': [
        'Hausa traditional attire',
        'Hausa native wear Nigeria',
        'Hausa cultural clothes men and women'
    ],
    'yoruba': [
        'Yoruba traditional attire',
        'Yoruba native dress Nigeria',
        'Yoruba agbada and iro buba'
    ],
    'igbo': [
        'Igbo traditional attire',
        'Igbo native dress Nigeria',
        'Igbo cultural clothes for men and women'
    ],
    'fulani': [
        'Fulani traditional attire',
        'Fulani dress Nigeria',
        'Fulani cultural wear'
    ]
}

# Maximum images per keyword (e.g., 40 * 3 = 120 max per label)
max_per_keyword = 40

# Loop through each category and its keywords
for label, keywords in attire_keywords.items():
    target_dir = f'nigerian_attire/{label}'
    os.makedirs(target_dir, exist_ok=True)
    
    print(f"Downloading for category: {label}")
    
    for keyword in keywords:
        print(f"  -> Searching: {keyword}")
        crawler = GoogleImageCrawler(storage={'root_dir': target_dir})
        crawler.crawl(keyword=keyword, max_num=max_per_keyword)
