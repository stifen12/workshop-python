class Mobil:
    <strong>def __init__(self,nama):
        self.nama = nama;</strong>
 
    def maju(self):
        <strong>print("Mobil "+ self.nama +" saya sedang bergerak maju.")</strong>
 
    def berhenti(self):
        <strong>print("Mobil "+ self.nama +" saya sedang berhenti.")</strong>
    
def main():
    <strong>avanza = Mobil('Avanza')</strong>
    avanza.maju()
    avanza.berhenti()
 
main()