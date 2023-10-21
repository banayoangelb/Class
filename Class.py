class Phone:
    def set_color(self,color):
        self.color=color
        
    def set_cost(self,cost):
        self.cost=cost
            
    def show_color(self):
                return self.color
            
    def show_cost(self):
                return self.cost
    def make_call(self):
                print("Making a call")
                
p2 = Phone()
p2.set_color('blue')
p2.set_cost(500)
p2.show_color()
