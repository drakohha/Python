class Player():
    money=500
    bordplase=0
    koloda=['none']
    def __init__(self,name=None,money=None,bordplase=None,koloda=None):
        self.name=name
        self.money=money
        self.bordplase=bordplase
        self.koloda=koloda
    def __str__(self):
        return(self.name)

    
class Zamer_gr():
    model_razmer_x=0
    model_razmer_y=0
    def __init__(self,model_razmer_x=None,model_razmer_y=None):
        self.model_razmer_x=model_razmer_x
        self.model_razmer_y=model_razmer_y
    def razmer_gr_x(self,x):
        self.model_razmer_x=x
    def razmer_gr_y(self,y):
        self.model_razmer_y=y
