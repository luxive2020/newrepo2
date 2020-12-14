
class CGPA:
    def __init__(self,unit=None,load=None):
        self.unit=unit
        self.load=load
        Total_units=0

    def prompt_init():
        return dict(
        Bio101=input("Bio101: "),
        Bio103=input("Bio103: "),
        CHE101=input("CHE101: "),
        CHE103=input("CHE103: "),
        CSC101=input("CSC101: "),
        GNS101=input("GNS101: "),
        GNS103=input("GNS103: "),
        MEE101=input("MEE101: "),
        MTS101=input("MTS101: "),
        PHY101=input("PHY101: "),
        PHY103=input("PHY103: "))
      
        
    prompt_init = staticmethod(prompt_init)
Total_Load=0
scores=CGPA.prompt_init()
Units={"Bio101":3,"Bio103":1,"CHE101":3,"CHE103":1,"CSC101":2,"GNS101":2,
       "GNS103":1,"MEE101":3,"MTS101":3,"PHY101":3,"PHY103":1}
for score in scores:
    for unit in Units:
        if int(scores[score])>=70 and score is unit:
            Unit=5*int(Units[unit])
            Total_Load+=Unit
        elif int(scores[score])>=60 and score is unit:
          Unit=4*int(Units[unit])
          Total_Load+=Unit
        elif int(scores[score])>=50 and score is unit:
            Unit=3*int(Units[unit])
            Total_Load+=Unit
        elif int(scores[score])>=45 and score is unit:
            Unit=2*int(Units[unit])
        elif int(scores[score])<=44 and score is unit:
            Unit=0*int(Units[unit])
            Total_Load+=Unit
            Total_Load+=Unit
Total_units=sum(Units.values())
GP=Total_Load/Total_units
print(GP)
