class miniReadability:
    url = ""
    name_file = ""
    def __init__(self, url_address):
        self.url = url_address
        self.name_file = "text.txt"
    def get_url(self):
        return self.url
    def get_name_file(self):
        return self.name_file

    def write_in_file(self, text):
        file = open(self.name_file, mode="w")
        for st in text:
            file.write(st.encode('utf8') + "\n\n")
        file.close()
    
    def get_raw_text(self):
        import requests
        from bs4 import BeautifulSoup
        r = requests.get(self.url).text
        soup = BeautifulSoup(r, 'html.parser')
        #search
        lst = soup.find_all(['h1', 'h2', 'h3', 'p'])
        print(lst)
        self.write_in_file(lst)
        
    def get_readable_text(self, list):
        pass
    
if __name__ == "__main__":
    url_address = "https://life.ru/t/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/1186974/tramp_v_shutku_pozhielal_amierikantsam_ghlobalnogho_potieplieniia"
    mr = miniReadability(url_address)
    mr.get_raw_text()
    #"https://life.ru/t/%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/1186974/tramp_v_shutku_pozhielal_amierikantsam_ghlobalnogho_potieplieniia"