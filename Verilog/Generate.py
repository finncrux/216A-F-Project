#for i in range(784):
    #print("FeatureBuf_{}<= Pix_{};".format(i,i))
    #print("reg[9:0] Adder_In_{};".format(i))

for i in range(66):
    state = i + 2
    Mul_i = i-6
    Add_i = i-6-16
    Final_i= i-6-16-4
    print("    {}:begin".format(state))
    print("     nxt_state = {};".format((state +1)))
    if(i<40):
        print("     //Feed input to Multipliers")
        for j in range(196):
            pixel = int(i/10)*196 + j
            outtgt  = int(i/4)
            print("         Multiplyer_matrix[{}].Feature = FeatureBuf_{};".format(j,pixel))
            print("         Multiplyer_matrix[{}].Weight = Wgt_{}_{};".format(j,outtgt,pixel))
    if (Mul_i>=0) & (Mul_i<40):
        print("     //Feed input to Adders")
        for j in range(98):
            print("         Adder_Base[{}].A = Multiplyer_matrix[{}].Result;".format(j,j*2))
            print("         Adder_Base[{}].B = Multiplyer_matrix[{}].Result;".format(j,j*2+1))
    if (Add_i>=0)&(Add_i<40):
        print("     //Collect Partial result form Adder")
        portion = Add_i%4
        target = int(Add_i/4)
        print("         Res_{}_{} = Part_Res;".format(target,portion))

    if (Add_i>=0)&(Add_i<40):
        portion = Add_i%4
        target = int(Add_i/4)
        if(portion == 3):
            print("     //Feed to final Adder")
            print("         l1 = Part_Res;".format(target,portion))
            print("         l2 = Res_{}_{};".format(target,portion-1))
            print("         r1 = Res_{}_{};".format(target,portion-2))
            print("         r2 = Res_{}_{};".format(target,portion-3))

    if (Final_i>=0)&(Final_i<40):
        portion = Final_i%4
        target = int(Final_i/4)
        if(portion ==3):
            print("     //Collect result from final Adder")
            print("         Res{} = Final_Res;".format(target))

    print("     end")

    
input()