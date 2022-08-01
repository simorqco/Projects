print(""""
                                                                         .   ,l'                                                                      
                                                                        ... ,O0;                                                                      
                                                                       ,xl,;kNd.                                                                      
                                                                     .dXO'..xk'                                                                       
                                                                    ;0WX:   .,..                                                                      
                                                                   ;0MMXc.    .c'                                                                     
                                                                  .oWMMMNk:,. .ok:.                                                                   
                                                                   lNMMMMMWNk' ;KXl.                                                                  
                                                                 .'.oXMMMMMMNl.cXMXc                                                                  
                                                                ,xc .;0WMMMMMXOKMMWo  ..                                                              
                                                               .xNx.  cNMMMMMMMMMMK; .oo.                                                             
                                                               ,0MNx;;xWMMMMMMMMMMXo:xNK,                                                             
                                                               'OMMMWWMMMMMMMMMMMMMWWMWx'..                                                           
                                                              ';c0WMMMMMMMMMMMMMMMMMWKo,od'                                                           
                                                             .ok,'dXMMMMMMMMMMMMMMMXo..lXo.                                                           
                                                            .dNO' .:KMMMMMMMMMMMMMXc. .dNo.                                                           
                                                           .dWMK:..;OWMMMWNNWMMMMM0;. 'kWXc.                                                          
                                                           ;KMMMN00NWWMMM0c,oXMMMMNXOkKWMM0'                                                          
                                                           'OMMMMMWNWMMWW0' .dWMWWMMMMMMMWk.                                                          
                                                            :XMMMM0lkWNdol. .oN0lxWMMNNWXd'                                                           
                                                            .;lxKWk.'x0c.   .:o' cNWOccc,.                                                            
                                                                'dk:..''.       .dXd.                                                                 
                                                                  .'...      .' .,,.                                                                  
                                                                  .'ck0xocloxKO:;c,.                                                                  
                                                                   'd0K0OOXWMMWN0o.  ..                                                               
                                                                     ....'d00ko:.                                                                     
                                                                         ....    
                                     #   #    ##   ###### #                                           
 ##### ##### ##### ##### ##### ##### #  #    #  #  #      #       ##### ##### ##### ##### ##### ##### 
                                     ###    #    # #####  #                                           
 ##### ##### ##### ##### ##### ##### #  #   ###### #      #       ##### ##### ##### ##### ##### ##### 
                                     #   #  #    # #      #                                           
                                     #    # #    # ###### #######    
""")
def addition(x,y):
    return x+y
    def subtract(x,y):
        return x-y
        def multiply(x,y):
            return x*y
            def divide(x,y):
                return x/y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

def cal():
 choice= input("Enter Choice(1/2/3/4")

 tuple_num = ('1','2','3','4')

 if choice in tuple_num:
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))

 if choice =='1':
    print(num1,"+",num2,"=", Addition(num1,num2))
 elif choice == '2':
        print(num1,"-",num2,"=",Subtraction(num1,num2))
 elif choice =='3':
    print(num1,"*",num2,"=",Multiply(num1,num2))
 elif choice == '4':
    print(num1,"/",num2,"=",Divide(num1,num2))
 else:print("Invalid input")     
cal() 

