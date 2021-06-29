from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ran')
def ran():
    return render_template("ran.html")

@app.route('/E-brochure')
def pdf():
    return render_template("pdf.html")

@app.route('/stu1')
def stu1():
    return render_template("stu1.html")
"""
@app.route('/klz')
def klz():
    import re
    import time
    import requests
    import base64
    from PIL import Image
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    
    path1='100.png'
    path2='100.png'
    times=0
    
    def processing_vcode():
        img = Image.open(path1)
        #img.show()
        img=img.crop((638,460,752,504))
        img = img.convert("L")  
        pixdata = img.load()
        w, h = img.size
        threshold = 160
        for y in range(h):
            for x in range(w):
                if pixdata[x, y] < threshold:
                    pixdata[x, y] = 0
                else:
                    pixdata[x, y] = 255

        data = img.getdata()
        w, h = img.size
        black_point = 0
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                mid_pixel = data[w * y + x]  
                if mid_pixel < 50:  
                    top_pixel = data[w * (y - 1) + x]
                    left_pixel = data[w * y + (x - 1)]
                    down_pixel = data[w * (y + 1) + x]
                    right_pixel = data[w * y + (x + 1)]

                    if top_pixel < 10:
                        black_point += 1
                    if left_pixel < 10:
                        black_point += 1
                    if down_pixel < 10:
                        black_point += 1
                    if right_pixel < 10:
                        black_point += 1
                    if black_point < 1:
                        img.putpixel((x, y), 255)
                    black_point = 0
        img.save(path2)
        
    def get_str():
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
        with open(path2, 'rb') as fg:
            img = base64.b64encode(fg.read())

        params = {"image":img}
        access_token = '24.7a74726b0ac3a604ba7bae5349de880a.2592000.1613989155.282335-19384325'
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)

        if response:
            data0=response.json()
            #print (data0)
            if data0['words_result_num']:
                data=data0['words_result'][0]['words'].replace('s','5').replace('S','5').replace('A','4').replace('·','-')
                data=re.sub(r'[^\d|+|-|*]','',data)
                #print (data)
                data=re.findall(r'[0-9][+|-|*][0-9]',data)
                if len(data)==0:
                    return 'error'
                else:
                    data=data[0]
                    return data
            else:
                return 'error'

    def code(vcode):
        a=int(vcode[0])
        b=int(vcode[2])
        if vcode[1]=='+':
            return a+b
        elif vcode[1]=='-':
            return a-b
        else:
            return a*b
        
    def get_vcode():
        while True:
            browser.find_element_by_xpath("//*[@id='tbLoginImg']").click()
            time.sleep(1)
            browser.get_screenshot_as_file(path1)
            
            processing_vcode()
            vcode=get_str()
            if vcode!='error':
                break
            print (vcode)
        return vcode
    
    browser = webdriver.PhantomJS()
    browser.get('https://www.lezhuan.com/login.html')
    browser.set_window_size(1680,959)
    time.sleep(2)
    
    browser.find_element_by_xpath("//*[@id='account']").send_keys("15362330731")
    browser.find_element_by_xpath("//*[@id='password']").send_keys("123qwe")
    browser.find_element_by_xpath("//*[@id='code']").click()
    time.sleep(1)

    while True:
        browser.find_element_by_xpath("//*[@id='code']").clear()
        vcode=get_vcode()
        browser.find_element_by_xpath("//*[@id='code']").send_keys(code(vcode))
        browser.find_element_by_xpath("//*[@class='zc_btn']").click()
        time.sleep(1)
        try:
            text=browser.find_element_by_xpath("//*[@class='login_msg']").text
        except NoSuchElementException:
            break
        else:
            if text=='':
                break
    
    lebi0=browser.find_element_by_xpath("//*[@class='lebi-number']").text
    lebi0=re.sub(r'\D','',lebi0)
    browser.find_element_by_xpath("//*[@id='snindex']").click()
    time.sleep(0.8)
    signinTimes=browser.find_element_by_xpath("//*[@id='signinTimes']").text
    lebi=browser.find_element_by_xpath("//*[@id='addAll']").text
    browser.refresh()
    time.sleep(1.5)
    lebi1=browser.find_element_by_xpath("//*[@class='lebi-number']").text
    lebi1=re.sub(r'\D','',lebi1)
    
    browser.get('https://www.lezhuan.com/lzbao/details.php')
    time.sleep(1.5)
    lzbao=browser.find_element_by_xpath("//div[@class='shouyi_box user_wealth']").text
    lzbao=re.findall(r'昨日收益\n[\d]+',lzbao)[0]
    lzbao=re.sub(r'\D','',lzbao)
    
    end_time=time.time()
    
    with open('lebidata.txt','a+') as f:
        f.write(time.strftime("\n%Y-%m-%d %H:%M:%S\t",time.localtime(time.time())))
        #f.write('签到前乐币：'+lebi0)
        f.write('签到后乐币：'+lebi1)
        f.write('\t乐赚宝昨日收益：'+lzbao)
        f.write('\t签到乐币：'+str(lebi))
        f.write('\t连签天数：'+str(signinTimes))
        f.write('\t尝试次数：'+str(times))
        f.write('\t用时：'+str(int(end_time-start_time))+'s')

    browser.quit()
    return render_template("klz.html")
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
