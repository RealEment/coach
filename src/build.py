# Builds the standalone PWA into the repo root from src/app-body.html
import pathlib
from PIL import Image, ImageDraw, ImageFont
root=pathlib.Path(__file__).parent; site=root.parent
body=(root/'app-body.html').read_text()
head='''<!doctype html>
<html lang="hu">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#16212c">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Vasnapló">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon-192.png">
<link rel="apple-touch-icon" href="icon-192.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}</style>
<script>window.VASNAPLO_PWA=true</script>
'''
(site/'index.html').write_text(head+body.replace('<div class="wrap">','</head>\n<body>\n<div class="wrap">',1)+'\n</body>\n</html>\n')
(site/'manifest.webmanifest').write_text('''{"name":"Vasnapló","short_name":"Vasnapló","lang":"hu","start_url":"./","scope":"./","display":"standalone","background_color":"#0e1419","theme_color":"#16212c",
"icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png","purpose":"any maskable"}]}
''')
(site/'sw.js').write_text('''const C='vasnaplo-v2';
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(['./','index.html','manifest.webmanifest','icon-192.png','icon-512.png'])));self.skipWaiting()});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==C).map(k=>caches.delete(k)))));self.clients.claim()});
self.addEventListener('fetch',e=>{if(e.request.method!=='GET')return;
  e.respondWith(fetch(e.request).then(r=>{const cp=r.clone();caches.open(C).then(c=>c.put(e.request,cp));return r}).catch(()=>caches.match(e.request).then(m=>m||caches.match('index.html'))))});
''')
for s in (192,512):
    im=Image.new('RGB',(s,s),'#16212c'); d=ImageDraw.Draw(im)
    r=s*0.34; cx=cy=s/2
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill='#c7372c')
    d.ellipse([cx-r*0.78,cy-r*0.78,cx+r*0.78,cy+r*0.78],outline='#e6857d',width=max(2,int(s*0.012)))
    d.ellipse([cx-r*0.2,cy-r*0.2,cx+r*0.2,cy+r*0.2],fill='#16212c')
    im.save(site/f'icon-{s}.png')
print('ok')
