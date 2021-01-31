from selenium import webdriver

firefox = webdriver.Firefox(executable_path="./geckodriver")


def vue(j):
    follow_button = firefox.find_elements_by_xpath("//span[@class='user-following-container js-form-toggle-container']")
    for i in range(0, follow+1-j):
        if i == len(follow_button):
            next_page = firefox.find_elements_by_xpath("//a[@class='btn btn-outline BtnGroup-item']")
            next_page[len(next_page)-1].click()
            j += i
            vue(j)
        else:
            follow_button[i].click()
            print(i+j+1, " accounts followed")
    print("Followed successfully !!!")


firefox.get("https://github.com/login")
enter = input("Log-in to your Github account and after that press Enter button")
follow = int(input("Number of following : "))
firefox.get("https://github.com/vuejs/vue/stargazers")
vue(0)
