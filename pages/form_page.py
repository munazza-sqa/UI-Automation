class FormPage: 
    
   
    def __init__(self, page):
            self.page=page
            
            self.username=page.locator("#userName")
            self.password=page.locator("#password")
            self.button=page.get_by_role("button", name="Login")
            
    def navigate(self):
            self.page.goto("https://demoqa.com/login")

    def login_username(self, username):
            self.username.fill(username)
            
    def login_password(self, password):
            self.password.fill(password)
        
    def login_button(self):
            self.button.click()
