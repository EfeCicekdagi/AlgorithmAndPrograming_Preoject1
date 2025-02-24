INDUSTRY_S_T_FEE = 305.3828             #S_T_FEE corresponds to Single-time Unit Energy Fee
INDUSTRY_D_P_FEE = 309.1833             #D_P_FEE corresponds to Daytime Period Unit Energy Fee
INDUSTRY_P_P_FEE = 490.9037             #P_P_FEE corresponds to Peak Period Unit Energy Fee
INDUSTRY_N_P_FEE = 162.5171             #N_P_FEE corresponds to Night Period Unit Energy Fee
INDUSTRY_DISTRIBUTION = 64.7998         #DISTRIBUTION corresponds to Unit Distribution Fee
PPO_L_S_T_FEE = 191.2220                #PPO_L corresponds to Public and Private Services Sector and Other (low tariff)
PPO_L_D_P_FEE = 285.8616                
PPO_L_P_P_FEE = 458.8843                
PPO_L_N_P_FEE = 148.1941
PPO_DISTRIBUTION = 87.8175
PPO_H_S_T_FEE = 282.8414                #PPO_H corresponds to Public and Private Services Sector and Other (high tariff)
RESIDENTIAL_L_S_T_FEE = 48.2187         #RESIDENTIAL_L corresponds to Residential (low tariff)
RESIDENTIAL_L_D_P_FEE = 115.7700 
RESIDENTIAL_L_P_P_FEE =208.3645
RESIDENTIAL_L_N_P_FEE = 41.7225 
RESIDENTIAL_DISTRIBUTION = 85.8883
RESIDENTIAL_H_S_T_FEE = 113.2271        #RESIDENTIAL_H corresponds to Residential (high tariff)
RESIDENTIAL_MARTYR_S_T_FEE = 6.1590     #RESIDENTIAL_MARTYR corresponds to Residential (family of martyrs and veterans)
RESIDENTIAL_MARTYR_DISTRIBUTION = 58.2521
AGRI_ACT_S_T_FEE = 165.3096             #AGRI_ACT corresponds to Agricultural Activities
AGRI_ACT_D_P_FEE = 170.4822 
AGRI_ACT_P_P_FEE = 280.0325
AGRI_ACT_N_P_FEE = 77.1882
AGRI_ACT_DISTRIBUTION = 72.1579
LIGHTING_S_T_FEE = 259.5835
LIGHTING_DISTRIBUTION =84.1099 
HIGH_VAT = 0.20                         
HIGH_ECT = 0.05                        
LOW_VAT = 0.10                          
LOW_ECT = 0.01                          
HIGH_CONSUME_ENERGY = 10000             
HIGH_BILL = 100000                      
PPO_LOW_TARIFF = 30                     
RESIDENTIAL_LOW_TARIFF = 8              

consumer_no = 1
num_of_industry = 0             #"Num_of" tells you how many of that user type there are 
multi_num_of_ppo = 0        
single_num_of_ppo = 0
num_of_residential = 0
num_of_agricultural_a = 0
num_of_lighting = 0
total_consume_of_industry = 0           #It shows how many kwh of energy that user type has consumed with what is written after total_consume
total_consume_of_single_ppo = 0         #This variable keeps the amount of electricity consumed by the Public and Private Services Sector and Other customer who selects single-time
total_consume_of_multi_ppo = 0          #This variable keeps the amount of electricity consumed by the Public and Private Services Sector and Other customer who selects multi-time
total_consume_of_residential = 0        
total_consume_of_agricultural_a = 0     
total_consume_of_lighting = 0           
single_time_ppo = 0                 #This variable holds the number of Public and Private Services Sector and Other customer who selects multi-time
multi_time_ppo = 0                  #This variable holds the number of Public and Private Services Sector and Other customer who selects multi-time
total_ect_amounts = 0       #This variable holds the total ect amount
total_vat_amounts = 0       #This variable holds the total vat amount
total_distribution_amount = 0       #This variable holds the total GDZ company's profits
high_industry = 0           #This variable holds the number of industrial users with output over 10000kWh or 100000TL
highest_residential_no = 0
highest_residential_daily_av_energy = -1
highest_residential_total_bill = -1         #These are variables that hold a few data of the user with the highest bill
highest_consumer_no = 0
highest_consumer_daily_av_energy = -1
highest_consumer_total_bill = -1
lose_consumer = 0       #This variable keeps the number of people who do not choose the single timer tariff and incur losses
martyr_number = 0       #This variablestores the number of martyrs or veterans in the family

def consmumer_number():
    while consumer_no < 0:
        consumer_no = int(input("Enter your consumer number: "))
    
def time_type() :       #This function allows the user to enter only multi_time or single-time
    time_type1 = "d"
    while time_type1 not in ["S","s","M","m"] :
        time_type1 = input("Enter the preferred tariff Single-time/Multi-time (S/s/M/m characters) : ")
    return time_type1

def yes_no() :          #This function allows the user to enter only yes/no
    time_type2 = "k"
    while time_type2 not in ["Y","y","N","n"] :
        time_type2 = input("Is there a martyr or veteran in the family (Y, y, N, n): ")
    return time_type2

def daytime():          #This function calculates the energy of daytime 
    p_daytime_meter_value = int(input("Enter previous daytime meter value: "))
    c_daytime_meter_value = int(input("Enter current daytime meter value: "))
    while not (p_daytime_meter_value >= 0 and c_daytime_meter_value >= p_daytime_meter_value) :
        p_daytime_meter_value = int(input("Enter previous daytime meter value: "))
        c_daytime_meter_value = int(input("Enter current daytime meter value: "))
    global daytime_energy_used
    daytime_energy_used = c_daytime_meter_value - p_daytime_meter_value
    return daytime_energy_used

def peak():             #This function calculates the energy of peak
    p_peak_meter_value = int(input("Enter previous peak meter value: "))
    c_peak_meter_value = int(input("Enter current peak meter value: "))
    while not (p_peak_meter_value >= 0 and c_peak_meter_value >= p_peak_meter_value) :
        p_peak_meter_value = int(input("Enter previous peak meter value: "))
        c_peak_meter_value = int(input("Enter current peak meter value: "))
    global peak_energy_used
    peak_energy_used = c_peak_meter_value - p_peak_meter_value
    return peak_energy_used

def night():            #This function calculates the energy of night 
    p_night_meter_value = int(input("Enter previous night meter value: "))
    c_night_meter_value = int(input("Enter current night meter value: "))
    while not (p_night_meter_value >= 0 and c_night_meter_value >= p_night_meter_value) :
        p_night_meter_value = int(input("Enter previous night meter value: "))
        c_night_meter_value = int(input("Enter current night meter value: "))
    global night_energy_used
    night_energy_used = c_night_meter_value - p_night_meter_value
    return night_energy_used

def total_energy():
    daytime()
    peak()
    night()
    global total_energy1
    total_energy1 = daytime_energy_used+peak_energy_used+night_energy_used

def amount_of_day():
    global amount_day
    amount_day = int(input("Enter the number of days between previous and current meter reading dates: "))
    while amount_day <= 0 :
        amount_day = int(input("Enter the number of days between previous and current meter reading dates: "))
    return amount_day

def consume_elec_pre_year():        #This function entered the total amount of electricity consumption in the current year until this period
    global elec_pre_year
    elec_pre_year = int(input("Enter total amount of electricity consumption in the current year until this period: "))
    while elec_pre_year  < 0 :
        elec_pre_year  = int(input("Enter total amount of electricity consumption in the current year until this period: "))

def free_consumer(now_year_total_electric):         #This function finds out the customer's free situation
    if now_year_total_electric > 1000 :
        print("congratulations! You are a free consumer")
    else:
        print("Unfortunately ,you are not a free consumer")

def energy_printer (daytime_energy_used,peak_energy_used,night_energy_used,total_energy1) :         #This function outputs some output to the screen
    print(f"Daytime period electricity consumption amount in this period is: {daytime_energy_used:.2f}kWh")
    print(f"Peak period electricity consumption amount in this period is: {peak_energy_used:.2f}kWh")
    print(f"Night period electricity consumption amount in this period is: {night_energy_used:.2f}kWh")
    print(f"Total electricity consumption amount in this period is: {total_energy1:.2f}kWh")

def all_time_cost(a,b,c):            #This function finds out total electricity consumption fee 
    global multi_cost
    multi_cost = daytime_energy_used*a/100 + peak_energy_used*b/100 + night_energy_used*c/100
    return multi_cost

def all_time_ect_amount(a,b,c,d):    #This function finds out ect amount
    global ect_amount
    ect_amount = all_time_cost(a,b,c)*d
    return ect_amount

def all_time_distribution(e):         #This function finds out revenues generated by distribution
    global cos_distributions
    global distribution_amount 
    cos_distributions = (daytime_energy_used+peak_energy_used+night_energy_used)*e/100
    distribution_amount = multi_cost + cos_distributions 
    return cos_distributions

def all_time_vat_amount(a,b,c,d,e,f):       #This function finds out vat amount
    global total_vat_amount1
    total_vat_amount1 = (all_time_ect_amount(a,b,c,d) + all_time_cost(a,b,c) + all_time_distribution(e)) * f
    return total_vat_amount1

def time_bill(a,b,c,d,e,f):            #his function finds out invoice(bill) amount 
    global time_bills
    time_bills = all_time_vat_amount(a,b,c,d,e,f) + (all_time_ect_amount(a,b,c,d) + all_time_cost(a,b,c) + all_time_distribution(e))
    return time_bills

def no_type(consumer_no,consumer_type):     #This function outputs some output to the screen
    print(f"Your consumer_type number is: {consumer_no}")
    print(f"Your consumer_type type is: {consumer_type} ")

def all_time_outputs(a,b,c,d,e,f):          #This function outputs some output to the screen
    print(f"Total electricity consumption fee for this period is: {all_time_cost(a,b,c):.2f}TL")
    print(f"ECT amount to be transferred to the municipality this period is:{all_time_ect_amount(a,b,c,d):.2f}TL")
    print(f"VAT amount to be transferred to the state this period: {all_time_vat_amount(a,b,c,d,e,f):.2f}TL")
    print(f"Total invoice amount for this period is: {time_bill(a,b,c,d,e,f):.2f}TL")    

def two_stage(a,b,c,d,e,f):             #This function performs a 2-stage exception.
    global ect_rate
    global vat_rate
    global invoice_amount
    global energy_fee
    global distribution_fee                     #The upper limit of the daily average multiplied by the number of days
    if total_energy1 <= (a*amount_day):         #and processed by the total energy we expend
        energy_fee=(b*total_energy1)/100        #This section inquires whether the energy has passed the upper limit. 
    else:   
        energy_fee = (b*(a*amount_day))/100
        energy_fee +=(d* (total_energy1-(a*amount_day)))/100
    distribution_fee= energy_fee +(c* total_energy1)/100
    ect_rate=energy_fee*e
    vat_rate=(distribution_fee + ect_rate)*f
    invoice_amount = distribution_fee + ect_rate + vat_rate
    return invoice_amount

def tax_calculator(distribution,ect,vat):       #This function calculates the total number of ect,vat,distribution
    global total_distribution_amount
    global total_ect_amounts
    global total_vat_amounts
    total_distribution_amount += distribution
    total_ect_amounts += ect
    total_vat_amounts += vat

def loss_profit_situation(profit_loss_amount):      #This function gives a output of whether the tariff chosen is profitable or not and collects the number of loss users
    global lose_consumer
    if profit_loss_amount < 0:
        lose_consumer += 1
        print("You made a loss compared to the other time option")
        print(f"Yours loss amount is: {profit_loss_amount:.2f}TL")
    else: 
        print("You made a profit compared to the other time option")
        print(f"Yours profit amount is: {profit_loss_amount:.2f}TL")

while consumer_no != 0 :
    consumer_no =  int(input("Enter your consumer_type number: "))
    if consumer_no != 0 and consumer_no > 0 :
        consumer_type = "c"
        while consumer_type not in ["I","i","P","p","R","r","A","a","L","l"] :
            consumer_type = input("Enter consumer type(I/i/P/p/R/r/A/a/L/l): ")
        if consumer_type in ["R","r"] :         #Performs inputs_ outputs and counts for residential in this section
            consumer_type = "Residential"
            num_of_residential += 1
            if  yes_no() in ["Y","y"] :     #In this section, inputs and outputs from those who have martyrs or veterans in their family
                total_energy()
                amount_of_day()
                consume_elec_pre_year()
                print("\n")
                no_type(consumer_no,consumer_type)
                energy_printer(daytime_energy_used,peak_energy_used,night_energy_used,total_energy1)
                all_time_outputs(RESIDENTIAL_MARTYR_S_T_FEE,RESIDENTIAL_MARTYR_S_T_FEE,RESIDENTIAL_MARTYR_S_T_FEE,HIGH_ECT,RESIDENTIAL_MARTYR_DISTRIBUTION,LOW_VAT)
                now_year_total_electric = total_energy1 + elec_pre_year
                print(f"Total electricity consumption amount in the current year as of this billing period is {now_year_total_electric}")
                free_consumer(now_year_total_electric)
                martyr_number += 1
                tax_calculator(distribution_amount ,ect_amount  ,total_vat_amount1)
                total_consume_of_residential += total_energy1
            else:
                if time_type() in ["S","s"]:    #In this section, inputs and outputs of residential users who have selected the single-time electricity tariff are presented. 
                    total_energy()
                    amount_of_day()
                    consume_elec_pre_year()
                    two_stage(RESIDENTIAL_LOW_TARIFF,RESIDENTIAL_L_S_T_FEE,RESIDENTIAL_DISTRIBUTION,RESIDENTIAL_H_S_T_FEE,HIGH_ECT,LOW_VAT)
                    print("\n")
                    no_type(consumer_no,consumer_type)
                    energy_printer(daytime_energy_used,peak_energy_used,night_energy_used,total_energy1)
                    print(f"Total electricity consumption fee for this period is: {energy_fee:.2f}TL")
                    print(f"ECT amount to be transferred to the municipality this period is:{ect_rate:.2f}TL")
                    print(f"VAT amount to be transferred to the state this period: {vat_rate:.2f}TL")
                    print(f"Total invoice amount for this period is: {invoice_amount:.2f}TL")    
                    profit_loss_amount =time_bill(RESIDENTIAL_L_D_P_FEE,RESIDENTIAL_L_P_P_FEE,RESIDENTIAL_L_N_P_FEE,HIGH_ECT,RESIDENTIAL_DISTRIBUTION,LOW_VAT) - invoice_amount 
                    loss_profit_situation(profit_loss_amount)       #Profit_loss_amount receives the difference between the tariff consumer did not choose and the tariff consumer did choose.
                    now_year_total_electric = total_energy1 + elec_pre_year
                    print(f"Total electricity consumption amount in the current year as of this billing period is {now_year_total_electric}")
                    free_consumer(now_year_total_electric)
                    total_consume_of_residential += total_energy1
                    tax_calculator(distribution_fee,ect_rate,vat_rate)
                else:           #In this section, inputs and outputs of residential users who have selected the multi-time electricity tariff are presented.
                    total_energy()
                    amount_of_day()
                    consume_elec_pre_year()
                    print("\n")
                    no_type(consumer_no,consumer_type)
                    energy_printer(daytime_energy_used,peak_energy_used,night_energy_used,total_energy1)
                    all_time_outputs(RESIDENTIAL_L_D_P_FEE,RESIDENTIAL_L_P_P_FEE,RESIDENTIAL_L_N_P_FEE,HIGH_ECT,RESIDENTIAL_DISTRIBUTION,LOW_VAT)
                    profit_loss_amount = two_stage(RESIDENTIAL_LOW_TARIFF,RESIDENTIAL_L_S_T_FEE,RESIDENTIAL_DISTRIBUTION,RESIDENTIAL_H_S_T_FEE,HIGH_ECT,LOW_VAT)-time_bills
                    loss_profit_situation(profit_loss_amount)       #Profit_loss_amount receives the difference between the tariff consumer did not choose and the tariff consumer did choose.
                    now_year_total_electric = total_energy1 + elec_pre_year
                    print(f"Total electricity consumption amount in the current year as of this billing period is {now_year_total_electric}")
                    free_consumer(now_year_total_electric)
                    total_consume_of_residential += total_energy1
                    tax_calculator(distribution_amount ,ect_amount  ,total_vat_amount1)
                if highest_residential_daily_av_energy < (total_energy1/amount_day):
                    highest_residential_no = consumer_no
                    highest_residential_daily_av_energy = float(total_energy1/amount_day)
                    highest_residential_total_bill = time_bills
        elif consumer_type in ["P","p"] :       #Performs inputs, outputs and counts for Industry/Public and Private Services Sector and Other in this section
            consumer_type = "Public and Private Services Sector and Other"
            if time_type() in ["S","s"] :       #In this section, inputs and outputs of Industry/Public and Private Services Sector and Other users who have selected the single-time electricity tariff are presented.
                single_num_of_ppo += 1
                total_energy()
                amount_of_day()
                consume_elec_pre_year()
                two_stage(PPO_LOW_TARIFF,PPO_L_S_T_FEE,PPO_DISTRIBUTION,PPO_H_S_T_FEE,HIGH_ECT,HIGH_VAT)
                print("\n")
                no_type(consumer_no,consumer_type)
                energy_printer(daytime_energy_used,peak_energy_used,night_energy_used,total_energy1)
                print(f"Total electricity consumption fee for this period is: {energy_fee:.2f}TL")
                print(f"ECT amount to be transferred to the municipality this period is:{ect_rate:.2f}TL")
                print(f"VAT amount to be transferred to the state this period: {vat_rate:.2f}TL")
                print(f"Total invoice amount for this period is: {invoice_amount:.2f}TL")    
                profit_loss_amount = time_bill(PPO_L_D_P_FEE,PPO_L_P_P_FEE,PPO_L_N_P_FEE,HIGH_ECT,PPO_DISTRIBUTION,HIGH_VAT) - invoice_amount  
                loss_profit_situation(profit_loss_amount)   #Profit_loss_amount receives the difference between the tariff consumer did not choose and the tariff consumer did choose.
                now_year_total_electric = total_energy1 + elec_pre_year
                print(f"Total electricity consumption amount in the current year as of this billing period is {now_year_total_electric}")
                free_consumer(now_year_total_electric)
                total_consume_of_single_ppo += total_energy1
                tax_calculator(distribution_fee,ect_rate,vat_rate)
                if highest_consumer_total_bill < invoice_amount:
                    highest_consumer_no = consumer_no
                    highest_consumer_daily_av_energy = total_energy1/amount_day
                    highest_consumer_total_bill = invoice_amount
                    highest_costumer_type = consumer_type

            else :          #In this section, inputs and outputs of Industry/Public and Private Services Sector and Other users who have selected the multi-time electricity tariff are presented.
                multi_num_of_ppo += 1
                total_energy()
                amount_of_day()
                consume_elec_pre_year()
                print("\n")
                no_type(consumer_no,consumer_type)
                energy_printer(daytime_energy_used,peak_energy_used,night_energy_used,total_energy1)
                all_time_outputs(PPO_L_D_P_FEE,PPO_L_P_P_FEE,PPO_L_N_P_FEE,HIGH_ECT,PPO_DISTRIBUTION,HIGH_VAT)
                profit_loss_amount = two_stage(PPO_LOW_TARIFF,PPO_L_S_T_FEE,PPO_DISTRIBUTION,PPO_H_S_T_FEE,HIGH_ECT,HIGH_VAT)-time_bills
                loss_profit_situation(profit_loss_amount)   #Profit_loss_amount receives the difference between the tariff consumer did not choose and the tariff consumer did choose.
                now_year_total_electric = total_energy1 + elec_pre_year
                print(f"Total electricity consumption amount in the current year as of this billing period is {now_year_total_electric}")
                free_consumer(now_year_total_electric)
                tax_calculator(distribution_amount ,ect_amount  ,total_vat_amount1)
                total_consume_of_multi_ppo += total_energy1
            if highest_consumer_total_bill < time_bills:
                highest_consumer_no = consumer_no
                highest_consumer_daily_av_energy = total_energy1/amount_day
                highest_consumer_total_bill = time_bills
                highest_costumer_type = consumer_type

        elif consumer_type in ["A","a"] :       #Performs inputs,outputs and counts for Agricultural Activities in this section
            consumer_type = "Agricultural Activities"
            num_of_agricultural_a += 1
            if time_type() in["S","s"]:         #In this section, inputs and outputs of Agricultural Activities users who have selected the single-time electricity tariff are presented.
                total_energy()
                amount_of_day()
                consume_elec_pre_year()
                print("\n")
                no_type(consumer_no,consumer_type)
                energy_printer(daytime_energy_used,peak_energy_used,night_energy_used,total_energy1)
                all_time_outputs(AGRI_ACT_S_T_FEE,AGRI_ACT_S_T_FEE,AGRI_ACT_S_T_FEE,HIGH_ECT,AGRI_ACT_DISTRIBUTION,LOW_VAT)
                profit_loss_amount =time_bill(AGRI_ACT_D_P_FEE,AGRI_ACT_P_P_FEE,AGRI_ACT_N_P_FEE,HIGH_ECT,AGRI_ACT_DISTRIBUTION,LOW_VAT)- time_bill(AGRI_ACT_S_T_FEE,AGRI_ACT_S_T_FEE,AGRI_ACT_S_T_FEE,HIGH_ECT,AGRI_ACT_DISTRIBUTION,LOW_VAT)
                loss_profit_situation(profit_loss_amount)       #Profit_loss_amount receives the difference between the tariff consumer did not choose and the tariff consumer did choose.
                now_year_total_electric = total_energy1 + elec_pre_year
                print(f"Total electricity consumption amount in the current year as of this billing period is {now_year_total_electric}")
                free_consumer(now_year_total_electric)
                tax_calculator(distribution_amount ,ect_amount  ,total_vat_amount1)
            else:           #In this section, inputs and outputs of Agricultural Activities users who have selected the multi-time electricity tariff are presented.
                total_energy()
                amount_of_day()
                consume_elec_pre_year()
                print("\n")
                no_type(consumer_no,consumer_type)
                energy_printer(daytime_energy_used,peak_energy_used,night_energy_used,total_energy1)
                all_time_outputs(AGRI_ACT_D_P_FEE,AGRI_ACT_P_P_FEE,AGRI_ACT_N_P_FEE,HIGH_ECT,AGRI_ACT_DISTRIBUTION,LOW_VAT)
                profit_loss_amount =time_bill(AGRI_ACT_S_T_FEE,AGRI_ACT_S_T_FEE,AGRI_ACT_S_T_FEE,HIGH_ECT,AGRI_ACT_DISTRIBUTION,LOW_VAT)- time_bill(AGRI_ACT_D_P_FEE,AGRI_ACT_P_P_FEE,AGRI_ACT_N_P_FEE,HIGH_ECT,AGRI_ACT_DISTRIBUTION,LOW_VAT)
                loss_profit_situation(profit_loss_amount)   #Profit_loss_amount receives the difference between the tariff consumer did not choose and the tariff consumer did choose.
                now_year_total_electric = total_energy1 + elec_pre_year
                print(f"Total electricity consumption amount in the current year as of this billing period is {now_year_total_electric}")
                free_consumer(now_year_total_electric)
                tax_calculator(distribution_amount ,ect_amount  ,total_vat_amount1)
            if highest_consumer_total_bill < time_bills:
                highest_consumer_no = consumer_no
                highest_consumer_daily_av_energy = total_energy1/amount_day
                highest_consumer_total_bill = time_bills
                highest_costumer_type = consumer_type
            total_consume_of_agricultural_a += total_energy1

        elif consumer_type in["I","i",]:        #Performs inputs ,outputs and counts for Industry in this section
            consumer_type = "Industry"
            num_of_industry += 1
            if time_type() in["S","s"]:         #In this section, inputs and outputs of Industry users who have selected the single-time electricity tariff are presented.
                total_energy()
                amount_of_day()
                consume_elec_pre_year()
                print("\n")
                no_type(consumer_no,consumer_type)
                energy_printer(daytime_energy_used,peak_energy_used,night_energy_used,total_energy1)
                all_time_outputs(INDUSTRY_S_T_FEE,INDUSTRY_S_T_FEE,INDUSTRY_S_T_FEE,LOW_ECT,INDUSTRY_DISTRIBUTION,HIGH_VAT)
                profit_loss_amount = time_bill(INDUSTRY_D_P_FEE,INDUSTRY_P_P_FEE,INDUSTRY_N_P_FEE,LOW_ECT,INDUSTRY_DISTRIBUTION,HIGH_VAT) - time_bill(INDUSTRY_S_T_FEE,INDUSTRY_S_T_FEE,INDUSTRY_S_T_FEE,LOW_ECT,INDUSTRY_DISTRIBUTION,HIGH_VAT)
                loss_profit_situation(profit_loss_amount)   #Profit_loss_amount receives the difference between the tariff consumer did not choose and the tariff consumer did choose.
                now_year_total_electric = total_energy1 + elec_pre_year
                print(f"Total electricity consumption amount in the current year as of this billing period is {now_year_total_electric}")
                free_consumer(now_year_total_electric)
                tax_calculator(distribution_amount ,ect_amount  ,total_vat_amount1)
            else:           #In this section, inputs and outputs of Industry users who have selected the multi-time electricity tariff are presented.
                total_energy()
                amount_of_day()
                consume_elec_pre_year()
                print("\n")
                no_type(consumer_no,consumer_type)
                energy_printer(daytime_energy_used,peak_energy_used,night_energy_used,total_energy1)
                all_time_outputs(INDUSTRY_D_P_FEE,INDUSTRY_P_P_FEE,INDUSTRY_N_P_FEE,LOW_ECT,INDUSTRY_DISTRIBUTION,HIGH_VAT)
                profit_loss_amount =time_bill(INDUSTRY_S_T_FEE,INDUSTRY_S_T_FEE,INDUSTRY_S_T_FEE,LOW_ECT,INDUSTRY_DISTRIBUTION,HIGH_VAT) - time_bill(INDUSTRY_D_P_FEE,INDUSTRY_P_P_FEE,INDUSTRY_N_P_FEE,LOW_ECT,INDUSTRY_DISTRIBUTION,HIGH_VAT)
                loss_profit_situation(profit_loss_amount)       #Profit_loss_amount receives the difference between the tariff consumer did not choose and the tariff consumer did choose.
                now_year_total_electric = total_energy1 + elec_pre_year
                print(f"Total electricity consumption amount in the current year as of this billing period is {now_year_total_electric}")
                free_consumer(now_year_total_electric)
                tax_calculator(distribution_amount ,ect_amount  ,total_vat_amount1)
            if highest_consumer_total_bill < time_bills:
                highest_consumer_no = consumer_no
                highest_consumer_daily_av_energy = total_energy1/amount_day
                highest_consumer_total_bill = time_bills
                highest_costumer_type = consumer_type
            if total_energy1 > HIGH_CONSUME_ENERGY or time_bills > HIGH_BILL :
                high_industry += 1
            total_consume_of_industry += total_energy1
        else :      #Performs inputs,outputs and counts for Lighting in this section
            consumer_type = "Lighting"
            num_of_lighting += 1
            total_energy()
            amount_of_day()
            consume_elec_pre_year()
            print("\n")
            no_type(consumer_no,consumer_type)
            energy_printer(daytime_energy_used,peak_energy_used,night_energy_used,total_energy1)
            all_time_outputs(LIGHTING_S_T_FEE,LIGHTING_S_T_FEE,LIGHTING_S_T_FEE,HIGH_ECT,LIGHTING_DISTRIBUTION,HIGH_VAT)
            now_year_total_electric = total_energy1 + elec_pre_year
            print(f"Total electricity consumption amount in the current year as of this billing period is {now_year_total_electric}")
            free_consumer(now_year_total_electric)
            total_consume_of_lighting += total_energy1
            tax_calculator(distribution_amount ,ect_amount  ,total_vat_amount1)
        if highest_consumer_total_bill < time_bills:
            highest_consumer_no = consumer_no
            highest_consumer_daily_av_energy = total_energy1/amount_day
            highest_consumer_total_bill = time_bills
            highest_costumer_type = consumer_type
        print("----------------------------------------------------------------------------------------")
num_of_ppo = single_num_of_ppo + multi_num_of_ppo
total_consume_of_ppo = total_consume_of_multi_ppo +total_consume_of_single_ppo
total_consumer = num_of_ppo + num_of_lighting + num_of_agricultural_a +num_of_industry +num_of_residential

# Statistical outputs are given in this bottom section
print(f"Statistical results of Public and Private Sevices Sector and Other:  Number: {num_of_ppo},  Percentages: {(num_of_ppo/total_consumer*100):.2f}%,  Average electricity \
consumption amounts in this period: {(total_consume_of_ppo/num_of_ppo):.2f}kWh, total electricity consumption amounts in this period: {(total_consume_of_ppo):.2f}kWh")
print("\n")
print(f"Statistical results of Residential :  Number: {num_of_residential},  Percentages: {(num_of_residential/total_consumer*100):.2f}%, Average electricity \
consumption amounts in this period: {(total_consume_of_residential/num_of_residential):.2f}kWh, total electricity consumption amounts in this period: {(total_consume_of_residential):.2f}kWh")
print("\n")
print(f"Statistical results of Agricultural Activities:  Number: {num_of_agricultural_a}, Percentages: {(num_of_agricultural_a/total_consumer*100):.2f}%, Average electricity \
consumption amounts in this period:  {(total_consume_of_agricultural_a/num_of_agricultural_a):.2f}kWh, total electricity consumption amounts in this period: {(total_consume_of_agricultural_a):.2f}kWh")
print("\n")
print(f"Statistical results of Industry:  Number: {num_of_industry},  Percentages: {(num_of_industry/total_consumer*100):.2f}%,  Average electricity \
consumption amounts in this period: {(total_consume_of_industry/num_of_industry):.2f}kWh, total electricity consumption amounts in this period: {(total_consume_of_industry):.2f}kWh")
print("\n")
print(f"Statistical results of Lighting:  Number: {num_of_lighting},  Percentages: {(num_of_lighting/total_consumer*100):.2f}%,  Average electricity \
consumption amounts in this period: {(total_consume_of_lighting/num_of_lighting):.2f}kWh, total electricity consumption amounts in this period: {(total_consume_of_lighting):.2f}kWh")
print("\n")
print(f"Bornova's total electricity consumption amount in this period: {(total_consume_of_lighting + total_consume_of_industry + total_consume_of_agricultural_a + total_consume_of_residential + total_consume_of_ppo):.2f}kWh")
print("\n")
print(f"Rates about Public and Privates Sevices Sector and Other: Single rate: {(single_num_of_ppo/num_of_ppo*100):.2f}%,  Multi rate: {(multi_num_of_ppo/num_of_ppo*100):.2f}%, \
Rate of total consume of single: {(total_consume_of_single_ppo/single_num_of_ppo):.2f}kWh,  Rate of total consume of multi: {(total_consume_of_multi_ppo/multi_num_of_ppo):.2f}kWh")
print("\n")
print(f"The number of industry type consumers whose electricity consumption amount is more than 10000 kWh or whose electricity bill is more than 100000 TL is: {high_industry},\
percentage among industry type consumers is: {(high_industry / num_of_industry*100):.2f}%")
print("\n")
print(f"Highest residential no: {highest_residential_no},  Highest residential daily avarage energy: {highest_residential_daily_av_energy:.2f}kWh,\
Highest residential total bill: {highest_residential_total_bill:.2f}TL" )
print("\n")
print(f"Highest consumer no: {highest_consumer_no},  Highest costumer type: {highest_costumer_type},  Highest consumer daily avarage energy: {highest_consumer_daily_av_energy:.2f}kWh,\
Highest consumer total bill: {highest_consumer_total_bill:.2f}TL")
print("\n")
print(f"Total ECT amounts: {total_ect_amounts:.2f}TL,  Total VAT amounts: {total_vat_amounts:.2f}TL,  Total distribution amount: {total_distribution_amount:.2f}TL")
print("\n")
print(f"the percentage of those who made a loss despite choosing multi-time tariff in the \
relevant period is: {(lose_consumer*100/(num_of_ppo+num_of_residential+num_of_agricultural_a+num_of_industry - martyr_number)):.2f}%")