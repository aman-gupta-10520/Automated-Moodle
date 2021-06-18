import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from prettytable import PrettyTable

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from prettytable import PrettyTable

class Moodle():

    def __init__(self,teacher_name,user_name,password,student_name):
        self.val=teacher_name.title()
        self.username = user_name
        self.password = password
        self.name = student_name.upper()
        self.ele = self.username + " " + self.name


    def login(self):
        s = Service("C:\\Users\\aman gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        #driver = webdriver.Chrome(ChromeDriverManager.install(self))
        driver.maximize_window()
        driver.get("http://moodle.mitsgwalior.in/login/index.php")
        driver.implicitly_wait(15)
        enrollment = driver.find_element("name", "username")
        enrollment.send_keys(self.username)
        password = driver.find_element("id", "password")
        password.send_keys(self.password)
        login = driver.find_element("id", "loginbtn")
        login.submit()

    def logout(self):
        s = Service("C:\\Users\\aman gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
        driver.get("http://moodle.mitsgwalior.in/my/")
        driver.implicitly_wait(15)
        try:
            driver.find_element(By.XPATH,f"//span[text()='{self.ele}']").click()
        except:
            print("You are already Log Out from your account!")
        else:
            driver.find_element(By.XPATH,"//a[@data-title='logout,moodle']").click()


    def Assignment(self,file_name,no_of_assignment=0,extension=".pdf"):
        op=Options()
        op.headless=True
        file_address="C:\\Users\\aman gupta\\Documents\\MoodleAssignments\\"+file_name+extension
        s = Service("C:\\Users\\aman gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=s,options=op)
        driver.maximize_window()
        driver.get("http://moodle.mitsgwalior.in/login/index.php")
        driver.implicitly_wait(30)
        enrollment = driver.find_element("name", "username")
        enrollment.send_keys(self.username)
        password = driver.find_element("id", "password")
        password.send_keys(self.password)
        login = driver.find_element("id", "loginbtn")
        login.submit()
        #time.sleep(5)
        teacher_module = driver.find_element(By.XPATH, f'//span[contains(text(),"{self.val}") and @class="multiline"]')
        teacher_module.click()
        assignment=driver.find_elements(By.XPATH,'//span[contains(text(),"Assignment") and @class="instancename"]')
        assignment[no_of_assignment-1].click()
        driver.find_element(By.XPATH, "//button[text()='Edit submission']")
        try:
            submission=driver.find_element(By.XPATH,"//button[text()='Edit submission']")
            submission.click()
        except:
            print("Submission is not open")
            time.sleep(2)
            driver.quit()
            return
        #file=driver.find_element(By.XPATH,'//a[contains(@title,"Add...")]')
        #time.sleep(3)
        try:
            file=driver.find_element(By.XPATH,'//a[@class="btn btn-secondary btn-sm"]')
            file.click()
            #time.sleep(3)
            driver.find_element(By.XPATH,'//input[@type="file"]').send_keys(file_address)
            driver.find_element(By.XPATH,'//input[@name="title"]').send_keys(self.username)
            driver.find_element(By.XPATH,'//button[text()="Upload this file"]').click()
            time.sleep(5)
            driver.find_element(By.XPATH,'//input[@value="Save changes"]').click()
            #time.sleep(5)
            print("Assignment has been submitted succesfully!")
        except:
            print("Unable to submit the assignment. Some error occured!")

    def Attendance(self,no_of_attendance=1):
        opt=Options()
        opt.headless=True
        s = Service("C:\\Users\\aman gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=s,options=opt)
        driver.maximize_window()
        driver.get("http://moodle.mitsgwalior.in/login/index.php")
        driver.implicitly_wait(20)
        enrollment = driver.find_element("name", "username")
        enrollment.send_keys(self.username)
        password = driver.find_element("id", "password")
        password.send_keys(self.password)
        login = driver.find_element("id", "loginbtn")
        login.submit()
        #time.sleep(3)
        teacher_module=driver.find_element(By.XPATH,f'//span[contains(text(),"{self.val}") and @class="multiline"]')
        teacher_module.click()
        attendance=driver.find_elements(By.XPATH,'//span[contains(text(),"Attendance") and @class="instancename"]')
        attendance[no_of_attendance-1].click()
        try:
            driver.find_element("link text",'Submit attendance').click()
        except:
            driver.quit()
            print("Attendance is not open yet")
            return

        try:
            present=driver.find_element(By.XPATH,'//span[contains(text(),"Present")]')
            present.click()
            submit_attendence=driver.find_element(By.XPATH,'//input[@value="Save changes"]')
            submit_attendence.submit()
            print("Attendance has been submitted succesfully!")
        except:
            print("Unable to submit attendance! Some error occured")

    def Remove_Assignment(self,no_of_assignment=0):
        s = Service("C:\\Users\\aman gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
        driver.get("http://moodle.mitsgwalior.in/login/index.php")
        driver.implicitly_wait(20)
        enrollment = driver.find_element("name", "username")
        enrollment.send_keys(self.username)
        password = driver.find_element("id", "password")
        password.send_keys(self.password)
        login = driver.find_element("id", "loginbtn")
        login.submit()
        #time.sleep(5)
        teacher_module = driver.find_element(By.XPATH, f'//span[contains(text(),"{self.val}") and @class="multiline"]')
        teacher_module.click()
        assignment=driver.find_elements(By.XPATH,'//span[contains(text(),"Assignment") and @class="instancename"]')
        assignment[no_of_assignment-1].click()
        try:
            driver.find_element(By.XPATH, "//button[text()='Remove submission']").click()
        except:
            print("Assignment is not submitted yet")
        driver.find_element(By.XPATH,'//button[text()="Continue"]').click()
        print("Successfully removed the assignment")
    def Information(self):
        op = Options()
        op.headless = True
        s = Service("C:\\Users\\aman gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=s,options=op)
        driver.maximize_window()
        driver.get("http://moodle.mitsgwalior.in/")
        driver.implicitly_wait(20)
        headers=driver.find_elements(By.XPATH,'//article/div/div/header/div/h3')
        dates=driver.find_elements(By.XPATH,'//article/div/div/header/div/div/time')
        links=driver.find_elements(By.XPATH,'//article/div/div/div/div/div/div/a[@href]')
        main_info=[]
        date_info=[]
        link_info=[]
        for head in headers:
            main_info.append(head.text)
        for date in dates:
            date_info.append(date.text)
        for link in links:
            link_info.append(link.get_attribute("href"))
        count=1
        for i,j,k in zip(main_info,link_info,date_info):
            print(count,end=". ")
            print(i,j,k,sep="\n")
            print("*"*50)
            count+=1
    def Upcoming_Activity(self):
        op = Options()
        op.headless = True
        s = Service("C:\\Users\\aman gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=s,options=op)
        #driver = webdriver.Chrome(executable_path=ChromeDriverManager.install())
        driver.maximize_window()
        driver.get("http://moodle.mitsgwalior.in/login/index.php")
        driver.implicitly_wait(20)
        enrollment = driver.find_element("name", "username")
        enrollment.send_keys(self.username)
        password = driver.find_element("id", "password")
        password.send_keys(self.password)
        login = driver.find_element("id", "loginbtn")
        login.submit()
        activity_date=[]
        activity_type=[]
        activity_info=[]
        Activities=driver.find_elements(By.XPATH,"//div[@class='tab-content']/div/div/div/div/div/div/div/div/h5")
        type=driver.find_elements(By.XPATH,'//div[@class="tab-content"]/div/div/div/div/div/div/div/div/div/div/div/div/img')
        info=driver.find_elements(By.XPATH,"//div[@class='tab-content']/div/div/div/div/div/div/div/div/div/div/div/div/a")
        for act in Activities:
            activity_date.append(act.text)
        for img in type:
            link=img.get_attribute("src")
            if("quiz" in link):
                activity_type.append("One Quiz is due on")
            elif("feedback" in link):
                activity_type.append("One Feedback is due on")
            elif ("assign" in link):
                activity_type.append("One Assignment is due on")
        for teach in info:
            activity_info.append(teach.get_attribute("aria-label"))
        c=1
        for i,j,k in zip(activity_type,activity_date,activity_info):
            print(c,".",sep="",end=" ")
            print(i,j,":-",k)
            c+=1
    def Messages(self):
        #op = Options()
        #op.headless = True ,options=op
        s = Service("C:\\Users\\aman gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
        driver.get("http://moodle.mitsgwalior.in/login/index.php")
        driver.implicitly_wait(30)
        enrollment = driver.find_element("name", "username")
        enrollment.send_keys(self.username)
        password = driver.find_element("id", "password")
        password.send_keys(self.password)
        login = driver.find_element("id", "loginbtn")
        login.submit()
        driver.find_element(By.XPATH,f"//span[text()='{self.ele}']").click()
        driver.find_element(By.XPATH,"//a[@data-title='messages,message']").click()
        driver.find_element(By.XPATH,'//div[@id="view-overview-messages-toggle"]/button').click()
        #time.sleep(5)
        name_teacher=driver.find_elements(By.XPATH,'//div[@class="list-group"]/a/div/div/strong')
        msgs_teacher=driver.find_elements(By.XPATH,'//div[@class="list-group"]/a/div/p/span')
        date_teacher=driver.find_elements(By.XPATH,'//div[@data-region="last-message-date"]')
        driver.find_element(By.XPATH,'//div[@id="view-overview-messages-toggle"]/button').click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@id='view-overview-group-messages-toggle']/button").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//a[@data-conversation-id=22504]").click()
        time.sleep(5)
        msg_dates=driver.find_elements(By.XPATH,'//div[@data-region="day-container"]/h6')
        student_names=driver.find_elements(By.XPATH,'//div[@data-region="day-container"]/div/div/div/div/h6')
        messages=driver.find_elements(By.XPATH,'//div[@data-region="day-container"]/div/div/div/p')

        dates=[]
        names=[]
        msgs=[]
        for i in msg_dates:
            dates.append(i.text)
        for j in student_names:
            names.append(j.text)
        for k in messages:
            msgs.append(k.text)
        teachers=[]
        messg=[]
        messg_dates=[]
        for x in name_teacher:
            teachers.append(x.get_property("innerHTML").strip())
        for y in msgs_teacher:
            messg.append(y.get_property("innerHTML").strip())
        for z in date_teacher:
            messg_dates.append(z.get_property("innerHTML").strip())
        print("Group Messages----")
        for b,c in zip(names,msgs):
            print(b)
            print("Message :--",c,'\n')

        print("\nPrivate Messages----")
        for a1,b1,c1 in zip(messg_dates,teachers,messg):
            print(a1," ",b1)
            print("Message :--",c1,'\n')
    def Grades(self):
        s = Service("C:\\Users\\aman gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
        driver.get("http://moodle.mitsgwalior.in/login/index.php")
        driver.implicitly_wait(30)
        enrollment = driver.find_element("name", "username")
        enrollment.send_keys(self.username)
        password = driver.find_element("id", "password")
        password.send_keys(self.password)
        login = driver.find_element("id", "loginbtn")
        login.submit()
        driver.find_element(By.XPATH,f"//span[text()='{self.ele}']").click()
        driver.find_element(By.XPATH,"//a[@data-title='grades,grades']").click()
        driver.find_element(By.XPATH,f'//tr/td/a[contains(text(),"{self.val}")]').click()
        types=driver.find_elements(By.XPATH,'//tr/th/a')
        grades=driver.find_elements(By.XPATH,"//tr/td[contains(@class,'column-grade')]")
        prcnt=driver.find_elements(By.XPATH,"//tr/td[contains(@class,'column-percentage')]")
        li_types=[]
        li_grades=[]
        li_prcnt=[]
        for a in types:
            li_types.append(a.get_attribute("title")[8:])
        for b in grades:
            if(b.text!='-'):
                li_grades.append(b.text)
        for c in prcnt:
            if(c.text!="-"):
                li_prcnt.append(c.text)
        tab=PrettyTable(["Type of Exam","Grades","Percentage"])
        for i,j,k in zip(li_types,li_grades,li_prcnt):
            tab.add_row([i,j,k])
        print(tab)
#first=Moodle("Prof. Vishwas Shrivastava")
first=Moodle("Ravindra","0901EC","password","Aman Gupta")
#first.Assignment("file")
first.Upcoming_Activity()
#first.login()
#first.Messages()
#first.Attendance()
#first.Assignment("file")
#first=Moodle("Ravindra")
#first.Grades()

























"""Moodle object takes one argument of teacher name(can be only first name in any case). Moodle class has three methods 
Asssignment(takes one compulsary parameter of file name want to submit and two optional arguments one is for no. of assignment 
in teacher module by default last and another is for extension which type of file want to submit by default it is .pdf)
another method is Attendance which takes one optional argument(by default first attendamce option) which shows no of attendance
 in module and another method is Remove_Assignment used for remove the current submission takes one optional argument which shows the no of 
 assignment in module."""
