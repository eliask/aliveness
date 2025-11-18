#!/usr/bin/env python3
"""
Generate SEO files (sitemap.xml, robots.txt) for aliveness.kunnas.com
GitHub Pages static site
"""

import os
from pathlib import Path
from datetime import datetime
import re

# Configuration
BASE_URL = "https://aliveness.kunnas.com"
WEBSITE_DIR = Path(__file__).parent
OUTPUT_SITEMAP = WEBSITE_DIR / "sitemap.xml"
OUTPUT_ROBOTS = WEBSITE_DIR / "robots.txt"

# Priority rules (higher = more important)
PRIORITY_RULES = {
    'index.html': '1.0',
    'articles/index.html': '0.9',
    'articles/axiological-malthusian-trap.html': '0.95',  # Flagship
    'SUMMARIES.md': '0.8',
    'EXECUTIVE_SUMMARY.md': '0.8',
}

# Exclude patterns
EXCLUDE_PATTERNS = [
    '.git',
    '.github',
    'src',
    '.DS_Store',
    '__pycache__',
    '*.pyc',
]

def should_exclude(path):
    """Check if path matches exclude patterns"""
    path_str = str(path)
    for pattern in EXCLUDE_PATTERNS:
        if pattern.startswith('.') and pattern[1:] in path_str:
            return True
        if pattern.startswith('*') and path_str.endswith(pattern[1:]):
            return True
        if pattern in path_str:
            return True
    return False

def get_priority(rel_path):
    """Determine priority based on path"""
    rel_path_str = str(rel_path)

    # Check explicit rules
    if rel_path_str in PRIORITY_RULES:
        return PRIORITY_RULES[rel_path_str]

    # Default priorities by depth and type
    depth = len(rel_path.parts)

    if rel_path_str.endswith('.md'):
        return '0.7'

    if 'articles/' in rel_path_str:
        return '0.8'

    # Root level
    if depth == 1:
        return '0.9'

    # Default
    return '0.7'

def get_changefreq(rel_path):
    """Determine change frequency"""
    rel_path_str = str(rel_path)

    if rel_path_str == 'index.html' or rel_path_str == 'articles/index.html':
        return 'weekly'

    return 'monthly'

def path_to_url(rel_path):
    """Convert file path to URL"""
    url_path = str(rel_path).replace('\\', '/')

    # Remove index.html from URLs
    if url_path == 'index.html':
        return BASE_URL + '/'
    elif url_path.endswith('/index.html'):
        return BASE_URL + '/' + url_path[:-10]
    elif url_path.endswith('.html'):
        return BASE_URL + '/' + url_path[:-5]
    else:
        # Keep .md, .pdf, .txt as-is
        return BASE_URL + '/' + url_path

def find_indexable_files():
    """Find all files that should be in sitemap"""
    indexable = []

    for root, dirs, files in os.walk(WEBSITE_DIR):
        # Filter out excluded directories
        dirs[:] = [d for d in dirs if not should_exclude(Path(d))]

        for file in files:
            full_path = Path(root) / file

            # Skip excluded files
            if should_exclude(full_path):
                continue

            # Only index specific file types
            if file.endswith(('.html', '.pdf', '.txt')):
                # Skip build script itself
                if file in ('build_seo.py', 'llms.txt', 'dialectical.txt', 'robots.txt'):
                    continue

                rel_path = full_path.relative_to(WEBSITE_DIR)
                indexable.append(rel_path)

    return sorted(indexable)

def generate_sitemap():
    """Generate sitemap.xml"""
    files = find_indexable_files()
    today = datetime.now().strftime("%Y-%m-%d")

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    for file_path in files:
        url = path_to_url(file_path)
        priority = get_priority(file_path)
        changefreq = get_changefreq(file_path)

        lines.extend([
            '  <url>',
            f'    <loc>{url}</loc>',
            f'    <lastmod>{today}</lastmod>',
            f'    <changefreq>{changefreq}</changefreq>',
            f'    <priority>{priority}</priority>',
            '  </url>'
        ])

    lines.append('</urlset>')

    OUTPUT_SITEMAP.write_text('\n'.join(lines))
    print(f"✓ Generated sitemap.xml with {len(files)} URLs")
    return len(files)

def generate_robots():
    """Generate robots.txt"""
    content = f"""# robots.txt for aliveness.kunnas.com
User-agent: *
Allow: /

# Unnecessary since repo available anyway
Disallow: /src/
Disallow: /.git/

# Sitemap
Sitemap: {BASE_URL}/sitemap.xml
"""

    OUTPUT_ROBOTS.write_text(content)
    print(f"✓ Generated robots.txt")

def main():
    """Main execution"""
    print(f"Building SEO files for {BASE_URL}")
    print(f"Website directory: {WEBSITE_DIR}")
    print()

    # Generate files
    num_urls = generate_sitemap()
    generate_robots()

    print()
    print(f"Summary: {num_urls} URLs indexed")

if __name__ == '__main__':
    main()
