project=int(input("enter your project score "))
internal=int(input("enter your internal score "))
external=int(input("enter your external score "))
if(project>50 and internal>50 and external>50):
    total=((70/100)*project)+((10/100)*internal)+((20/100)*external)
    print("total marks",total)
    if(total>90):
        print("A grade")
    elif(80<total<90):
        print("B grade")
    else:
        print("C grade")
else:
    if(external<50):
        print("student failed in external",external)
    if( internal<50 ):
        print("student failed in internal",internal)
    if(project<50):
         print("student failed in project",project)
