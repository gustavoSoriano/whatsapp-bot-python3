from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self, pessoas):
        self.pessoas  = pessoas
        options       = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver   = webdriver.Chrome(executable_path='./chromedriver')
        self.driver.get('https://web.whatsapp.com')
        print('Aguardando 30 segundos para sincronização do QRCode')
        time.sleep(30)


    def envia_nao_contatos(self, telefone, mensagem):
        self.driver.get( f'https://web.whatsapp.com/send?phone=${telefone}&text={mensagem}' )
        time.sleep(5)
        botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        botao_enviar.click()
        print( f"Enviado para telefone: {telefone}")



    def envia_contatos(self, mensagem):
        for pessoa in self.pessoas:
            print( f"Enviando mensagem para {pessoa}" )
            pessoa = self.driver.find_element_by_xpath(f"//span[@title='{pessoa}']")
            pessoa.click()
            time.sleep(2)
            
            chat_box = self.driver.find_element_by_class_name('_13mgZ')
            chat_box.click()
            chat_box.send_keys( mensagem )

            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot( ["Maria"] ) # Set Contact Name in list
bot.envia_contatos(" Mensagem automatizada via Bot ")
bot.envia_nao_contatos(5516997659374, "mensagem de teste")