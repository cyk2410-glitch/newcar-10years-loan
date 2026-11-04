from pathlib import Path
from urllib.parse import urlparse
from xml.sax.saxutils import escape
import sys, re, html, json
if len(sys.argv) != 2:
    raise SystemExit('Usage: python prepare_domain.py https://your-project.pages.dev')
base=sys.argv[1].rstrip('/')
p=urlparse(base)
if p.scheme!='https' or not p.netloc or p.path or p.query or p.fragment:
    raise SystemExit('Provide only a public HTTPS origin (no path)')
root=Path(__file__).resolve().parent
file=root/'index.html'; content=file.read_text(encoding='utf-8')
content=re.sub(r'<link\s+rel="canonical"[^>]*>', '', content)
content=re.sub(r'<meta\s+property="og:url"[^>]*>', '', content)
content=content.replace('</head>', f'<link rel="canonical" href="{html.escape(base)}/"/><meta property="og:url" content="{html.escape(base)}/"/></head>',1)
for key in ('og:image','twitter:image'):
    content=re.sub(r'(<meta\s+(?:property|name)="'+re.escape(key)+r'"\s+content=")[^"]*(")',lambda m:m.group(1)+html.escape(base)+'/assets/brand.jpg'+m.group(2),content)
content=content.replace('"image": "assets/brand.jpg"','"image": "'+base+'/assets/brand.jpg"')
content=re.sub(r'"image": "https://[^" ]+/assets/brand.jpg"','"image": "'+base+'/assets/brand.jpg"',content)
file.write_text(content,encoding='utf-8')
(root/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n',encoding='utf-8')
(root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>'+escape(base)+'/</loc></url></urlset>\n',encoding='utf-8')
print('Prepared canonical, OG, Twitter, structured image, robots, sitemap for',base)
