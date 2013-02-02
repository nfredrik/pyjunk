class AInput:  # We can't use input as it is a existent function name, so we use AInput for Advance Input
   ''' This class will create a object with a simpler coding interface to retrieve console input'''
   def __init__(self, msg="", req=0):
      ''' This will create a instance of ainput object'''
      self.data = ""  # Initialize a empty data variable
      if not msg == "":
         self.ask(msg, req)
 
   def ask(self, msg= "", req=0):
      ''' This will display the prompt and retrieve the user input.'''
      if req == 0:
         self.data = raw_input(msg)  # Save the user input to a local object variable
      else:
         self.data = raw_input(msg + " (Require)")
 
      # Verify that the information was entered and its not empty. This will accept a space character. Better Validation needed
      if req == 1 and self.data == "":
         self.ask(msg, req)
 
   def getString(self):
      ''' Returns the user input as String'''
      return self.data
 
   def getInteger(self):
      ''' Returns the user input as a Integer'''
      return int(self.data)
 
   def getNumber(self):
      ''' Returns the user input as a Float number'''
      return float(self.data)
 
def main():
        name = AInput("Please enter your first name: ").getString()
        age = AInput("Now enter your age: ").getInteger()
        wage = AInput("And your hourly wage: ").getNumber()
        print(name, age, wage)
 
if __name__ == '__main__':
        main()