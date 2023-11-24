import utils.file_utils.get_working_directory
import utils.file_utils.get_time
import utils.file_utils.subs
import utils.file_utils.tool_getters
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from PIL import Image
import subprocess
from datetime import datetime
import time
import os

counter = 0

screenshots = []
text = {}

write_end_time = None

def get_write_time():
    return write_end_time


def write_output(str):
    print(str)
    with open(f"{utils.file_utils.get_working_directory.get_wd()}/report.txt", 'a') as file:
        file.writelines(str + '\n')

def resolve():

    start_time = datetime.now().time()
    time_start = time.time()
    write_output(f"Beginning resolving subdomains at {str(start_time)[:-7]}")


    if utils.file_utils.tool_getters.get_cname():
        command = ["massdns", "-r", utils.file_utils.tool_getters.get_resolvers(), "-t", "A", "-o", "S", f"{utils.file_utils.get_working_directory.get_wd()}/temp/subdomains_temp.txt", "-w", f"{utils.file_utils.get_working_directory.get_wd()}/temp/subdomains.txt"]
        subprocess.run(command)

        with open(f"{utils.file_utils.get_working_directory.get_wd()}/temp/subdomains.txt", 'r') as file:
            lines = [x[:-1] for x in file.readlines()]

            domains = set()

            #domains = set([x[1] for x in utils.file_utils.subs.get_subs()])

            for line in lines:
                l = line.split(' ')
                for i in l:
                    if i.count('.') >= 1:
                        if i[-1] != '.':
                            domains.add(i)
                        else:
                            domains.add(i[:-1])
    else:
        domains = set([x[1] for x in utils.file_utils.subs.get_subs()])

    if utils.file_utils.tool_getters.get_screenshot():
        os.mkdir(f"{utils.file_utils.get_working_directory.get_wd()}/screenshots")

    res_domains = set()
    
    counter = 0

    def resolve_and_screenshot(domain):
        global counter
        options = Options()

        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--headless") 

        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(10)
        
        global text

        try:
            driver.get(f'https://{domain}')
            if utils.file_utils.tool_getters.get_screenshot():
                driver.get_screenshot_as_file(f"{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_{domain}.png")
                screenshots.append(f"{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_{domain}.png")
            response_text = driver.page_source
            text[f"{utils.file_utils.get_working_directory.get_wd()}/screenshots/https_{domain}.png"] = response_text
            driver.quit()
            res_domains.add(domain)
        except:
            try:
                driver.get(f'http://{domain}')
                if utils.file_utils.tool_getters.get_screenshot():
                    driver.get_screenshot_as_file(f"{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_{domain}.png")
                    screenshots.append(f"{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_{domain}.png")
                response_text = driver.page_source
                text[f"{utils.file_utils.get_working_directory.get_wd()}/screenshots/http_{domain}.png"] = response_text
                driver.quit()
                res_domains.add(domain)
            except:
                pass
            pass

    domains = sorted(list(domains))

    total_domains = len(domains)

    num_threads = utils.file_utils.tool_getters.get_screenshot_threads()

    func = resolve_and_screenshot

    domains_to_execute = [func] * total_domains

    def run_function():
        while domains_to_execute:
            function = domains_to_execute.pop()
            seed = domains.pop()
            if function:
                function(seed)
                global counter
                counter += 1
                if counter % 100 == 0:
                    print(f"{counter}/{len(domains) + counter} screenshots taken.")

    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=run_function)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    out = set()
    
    for i in utils.file_utils.subs.get_subs():
        if i[1] in res_domains:
            out.add(i)
    
    utils.file_utils.subs.set_subs(out)

    for i in res_domains:
        if i not in [x[1] for x in utils.file_utils.subs.get_subs()]:
            utils.file_utils.subs.add_sub('cname-resolve', i)

    with open(f"{utils.file_utils.get_working_directory.get_wd()}/subdomains.txt", 'w') as out_file:
        sub_set = [x[1] for x in utils.file_utils.subs.get_subs()]
        sub_set = set(sub_set)
        for i in sub_set:
            out_file.writelines(i + '\n')

    end_time = time.time()

    elapsed_time = end_time - time_start
    
    global write_end_time
    
    write_end_time = elapsed_time

    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)

    write_output(f"Resolving subdomains done at {str(datetime.now().time())[:-7]} in {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")
    utils.file_utils.get_time.add_time(('cname-resolve', hours * 3600 + minutes * 60 + seconds))
    
similar_images = {}

def get_screenshots():
    global screenshots
    return screenshots

def get_similar_screenshots():
    global similar_images
    return similar_images

def compare_screenshots(screenshots):
    
    start_time = datetime.now().time()
    time_start = time.time()
    write_output(f"Initiating screenshot comparison at {str(start_time)[:-7]}")
    
    time_count = 0
    
    global similar_images
    for screenshot1 in screenshots:
        time_count += 1
        if time_count % 100 == 0:
            print(f'Screenshots compared: {time_count}')
        image1 = Image.open(screenshot1)
        for screenshot2 in screenshots:
            image2 = Image.open(screenshot2)
            count = 0
            
            for x in range(0, 400, 10):
                for y in range(0, 300, 10):
                    
                    pixel_color1 = image1.getpixel((x, y))
                    pixel_color2 = image2.getpixel((x, y))
                    
                    if pixel_color1 != pixel_color2:
                        count += 1
                        
            ok = True
                        
            for i in similar_images.keys():
                for ii in similar_images[i]:
                    if ii == screenshot2:
                        ok = False
                        
            if ok:
                if count < 100:
                    if screenshot1 in similar_images:
                        similar_images[screenshot1] = similar_images[screenshot1] + [screenshot2]
                    else:
                        similar_images[screenshot1] = [screenshot1]
                        similar_images[screenshot1] = similar_images[screenshot1] + [screenshot2]
                        
    end_time = time.time()

    elapsed_time = end_time - time_start

    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    write_output(f"Screenshot comparison done at {str(datetime.now().time())[:-7]} in {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")
            
                        
                        

def compare_subdomains():
    start_time = datetime.now().time()
    time_start = time.time()
    write_output(f"Initiating subdomain comparison at {str(start_time)[:-7]}")

    global text
    global similar_images
    for text1 in text:
        ct1 = text[text1]
        for text2 in text:
            ct2 = text[text2]
            count = 0
            
            treshold = 100
            if len(ct1) < 200:
                treshold = 11
            
            for i in range(len(ct1)):
                try:
                    if ct1[i] != ct2[i]:
                        count += 1
                except:
                    break
                    pass
            
            ok = True
                        
            for i in similar_images.keys():
                for ii in similar_images[i]:
                    if ii == text2:
                        ok = False
                        
            if ok:
                if count < treshold:
                    if text1 in similar_images:
                        similar_images[text1] = similar_images[text1] + [text2]
                    else:
                        similar_images[text1] = [text1]
                        similar_images[text1] = similar_images[text1] + [text2]
                else:
                    image1 = Image.open(text1)
                    image2 = Image.open(text2)
                    count = 0
                    
                    for x in range(0, 400, 10):
                        for y in range(0, 300, 10):
                            
                            pixel_color1 = image1.getpixel((x, y))
                            pixel_color2 = image2.getpixel((x, y))
                            
                            if pixel_color1 != pixel_color2:
                                count += 1
                                
                    ok = True
                        
                    for i in similar_images.keys():
                        for ii in similar_images[i]:
                            if ii == text2:
                                ok = False
                                            
                    if ok:
                        if count < treshold:
                            if text1 in similar_images:
                                similar_images[text1] = similar_images[text1] + [text2]
                            else:
                                similar_images[text1] = [text1]
                                similar_images[text1] = similar_images[text1] + [text2]
                                
                    
                        
    end_time = time.time()

    elapsed_time = end_time - time_start

    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    write_output(f"Subdomain comparison done at {str(datetime.now().time())[:-7]} in {'0' if len(str(int(hours))) == 1 else ''}{str(int(hours))}:{'0' if len(str(int(minutes))) == 1 else ''}{str(int(minutes))}:{'0' if len(str(int(seconds))) == 1 else ''}{str(int(seconds))}")
            
    

                        
                        
                        
                        
                        
    
