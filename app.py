from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        options       = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')

        try:
            self.driver   = webdriver.Chrome(executable_path='./chromedriver')
            self.driver.get('https://web.whatsapp.com')
            print('Waiting 30 seconds for QRCode synchronization')
            time.sleep(30)
        except Exception as e:
            print("Oops!", e)


    def send_by_phone(self, phone, message):
        if( "driver" in self.__dict__ ):
            self.driver.get( f'https://web.whatsapp.com/send?phone=${phone}&text={message}' )
            time.sleep(5)

            try:
                send_button = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                send_button.click()
                print( f"Sent to phone: {phone}")
            except Exception as e:
                print("Oops!", e.__class__, "occurred.")


bot = WhatsappBot()
bot.send_by_phone(5516997659374, "Bot automated message")