import sys
from playwright.sync_api import sync_playwright
url='https://memory-of-a-nation.vercel.app/';O='out/'
import os;os.makedirs(O,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch()
    def page(lang,theme):
        pg=b.new_page(viewport={'width':1440,'height':900},device_scale_factor=2)
        pg.add_init_script(f"localStorage.getItem('bayan-lang')||localStorage.setItem('bayan-lang','{lang}');localStorage.getItem('bayan-theme')||localStorage.setItem('bayan-theme','{theme}')")
        pg.goto(url,wait_until='networkidle');pg.wait_for_timeout(2500)
        if theme=='light' and pg.evaluate("document.documentElement.getAttribute('data-bayan')")!='light': pg.click('#theme');pg.wait_for_timeout(600)
        return pg
    for l,t in [('ar','dark'),('en','dark'),('ar','light')]:
        h=page(l,t);h.screenshot(path=O+f'00-hero-{l}-{t}.png');h.close()
    # 1-4 Arabic dark: chat with War and Peace
    pg=page('ar','dark')
    pg.evaluate("document.querySelector('#rail .rb[data-k=war]').click()");pg.wait_for_timeout(2800)
    pg.screenshot(path=O+'01-ar-book-chat-open.png')
    pg.fill('#cvQ','ما الفكرة الأساسية في هذه الرواية؟');pg.keyboard.press('Enter');pg.wait_for_timeout(4500)
    pg.fill('#cvQ','من هي أهم شخصية فيها؟');pg.keyboard.press('Enter');pg.wait_for_timeout(4500)
    pg.screenshot(path=O+'02-ar-talking-with-the-book.png')
    pg.click('.cvx-rc.ch >> nth=1');pg.wait_for_timeout(1800);pg.click('#duoSU .su-s');pg.wait_for_timeout(2600)
    pg.fill('#cvQ','ما الذي تخشينه أكثر؟');pg.keyboard.press('Enter');pg.wait_for_timeout(5000)
    pg.screenshot(path=O+'03-ar-character-joins-the-same-conversation.png')
    pg.click('.cvx-tabs [data-t=time]');pg.wait_for_timeout(500);pg.click('.cvx-all');pg.wait_for_timeout(1500)
    pg.screenshot(path=O+'04-ar-story-timeline.png');pg.close()
    # 5-6 English dark
    pg=page('en','dark')
    pg.evaluate("document.querySelector('#rail .rb[data-k=macbeth]').click()");pg.wait_for_timeout(2800)
    pg.fill('#cvQ','What drives Macbeth to murder?');pg.keyboard.press('Enter');pg.wait_for_timeout(4500)
    pg.screenshot(path=O+'05-en-talking-with-macbeth.png')
    pg.click('.cvx-rc.ch >> nth=0');pg.wait_for_timeout(1800);pg.click('#duoSU .su-s');pg.wait_for_timeout(2600)
    pg.click('.cvx-rc.ch >> nth=1');pg.wait_for_timeout(3000)
    pg.fill('#cvQ','Who is really to blame?');pg.keyboard.press('Enter');pg.wait_for_timeout(6500)
    pg.screenshot(path=O+'06-en-duo-in-the-book-conversation.png');pg.close()
    # 7-8 light
    pg=page('ar','light')
    pg.evaluate("document.querySelector('#rail .rb[data-k=nights]').click()");pg.wait_for_timeout(2800)
    pg.fill('#cvQ','لماذا يشعر الحالم بالوحدة؟');pg.keyboard.press('Enter');pg.wait_for_timeout(4500)
    pg.screenshot(path=O+'07-ar-light-book-chat.png');pg.close()
    pg=page('en','light')
    pg.evaluate("document.querySelector('#rail .rb[data-k=othello]').click()");pg.wait_for_timeout(2800)
    pg.fill('#cvQ','Was Iago really the villain?');pg.keyboard.press('Enter');pg.wait_for_timeout(4500)
    pg.screenshot(path=O+'08-en-light-book-chat.png');pg.close()
    b.close()
