def tot_calc(bill_amount, tip_perc):
    tot = bill_amount * (1 + 0.01 * tip_perc)
    tot = round(tot, 2)
    print(f"Please pay ${tot}")

tot_calc(150, 20)