from Math import Math

class Private_key:
    pass 

class Public_key:
    pass

class RSA:
    
    def RSA(self):
        self.p, self.q = Math.find_p_and_q()
        
    def encode(self, key : Private_key, message):
        pass 
    
    def decode(self, key: Public_key, message):
        pass