class Atm(object):
  """
   blueprint for ATM
  """
  def __init__(self,atm_card_number,pin_number):
    self.atm_card_number=atm_card_number
    self.pin_number=pin_number

  def cashWidthrawal(self):
    print("withdrawing the cash") 

  def balanceEnquiry(self):
    print("balance enquiry...")  

icici = Atm(1234567898,1112223334)     

print(icici.cashWidthrawal())
