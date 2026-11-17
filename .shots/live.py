import os
from playwright.sync_api import sync_playwright
url='https://memory-of-a-nation.vercel.app/';O='out/';os.makedirs(O,exist_ok=True)
scenes=[
 ('01-ar-tawq-dark','ar','dark','tawq',['من قتل في أزقة مكة القديمة؟','ما علاقة الحمام بالقصة؟','من هي عزة؟']),
 ('02-ar-gebelawi-dark','ar','dark','gebelawi',['ما الفكرة الأساسية في الرواية؟','من هو الجبلاوي؟']),
 ('03-en-war-dark','en','dark','war',['What is the big idea of this novel?','Who is the most important character?']),
 ('04-ar-tawq-light','ar','light','tawq',['من قتل في أزقة مكة القديمة؟','ما علاقة الحمام بالقصة؟']),
 ('05-en-macbeth-light','en','light','macbeth',['What drives Macbeth to murder?','Is Lady Macbeth to blame?']),
]
with sync_playwright() as p:
    b=p.chromium.launch()
    for name,lang,theme,k,qs in scenes:
        try:
            pg=b.new_page(viewport={'width':1440,'height':900},device_scale_factor=2)
            pg.add_init_script(f"localStorage.setItem('bayan-lang','{lang}');localStorage.setItem('bayan-theme','{theme}')")
            pg.goto(url,wait_until='networkidle');pg.wait_for_timeout(2500)
            if theme=='light' and pg.evaluate("document.documentElement.getAttribute('data-bayan')")!='light': pg.click('#theme');pg.wait_for_timeout(600)
            pg.evaluate(f"document.querySelector('#rail .rb[data-k={k}]').click()");pg.wait_for_timeout(3000)
            for q in qs:
                pg.fill('#cvQ',q);pg.keyboard.press('Enter');pg.wait_for_timeout(5000)
            pg.screenshot(path=O+name+'.png')
            if name.startswith('01'):
                pg.evaluate(f"bayanListen.open('{k}')");pg.wait_for_timeout(2000)
                pg.screenshot(path=O+'06-ar-tawq-listen-fullscreen.png')
            pg.close()
        except Exception as e: print(name,e)
    b.close()
