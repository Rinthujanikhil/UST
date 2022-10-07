#4. Write functions to calculate and display grosssalary and netsalary of an employee after getting input as basicsalary
#Write separate functions for allowances and deductions to calculate them respectively

#netsalary = grosssalary - deductions
#grosssalary = basicsalary + allowances

#allowances = hra(22% of basicsalary) + da(18% of basicsalary) +ta(10% of basicsalary)

#deductions = proftax(if basicsalary > 8000 the 200 else 150) + pf(12% of basicsalary) + insurance(8% of basicsalary)


def allowance():
    basicsal=float(input("Enter the basic salary:RS."))
    hra=basicsal%22
    da=basicsal%18
    ta=basicsal%8
    allowance_emp=hra+da+ta
    print("Allowance of Employee Rs.",allowance_emp)
    def grossalary():
       grossalary_emp=allowance_emp+basicsal
       print("Grossalary of employee is RS.", grossalary_emp)
       def deduction():
           pf=basicsal%12
           insurence=basicsal%8
           if basicsal>8000:
            proftaxs=200
            dedution=proftaxs+pf+insurence
            print("Deduction of employee ",dedution)
           else:
               proftax=150
               dedution=proftax+pf+insurence
               print("Deduction of employee",dedution)
               def netsalary():
                   netsalary_emp=grossalary_emp-dedution
                   print("netsalary of employee Rs.",netsalary_emp)
               netsalary()

       deduction()
    
    grossalary()
allowance()



