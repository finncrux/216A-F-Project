#for i in range(784):
    #print("FeatureBuf_{}<= Pix_{};".format(i,i))
    #print("reg[9:0] Adder_In_{};".format(i))

for i in range(106):
    state = i + 2
    Mul_i = i-6
    Add_i = i-6-14
    Final_i= i-6-14-6
    print("    {}:begin".format(state))
    print("     nxt_state = {};".format((state +1)))
    if(i<80):
        print("     //Feed input to Multipliers")
        for j in range(98):
            pixel = int(i%8)*98 + j
            outtgt  = int(i/8)
            print("         Multiplyer_matrix[{}].Feature = FeatureBuf_{};".format(j,pixel))
            print("         Multiplyer_matrix[{}].Weight = Wgt_{}_{};".format(j,outtgt,pixel))
    if (Mul_i>=0) & (Mul_i<80):
        print("     //Feed input to Adders")
        for j in range(49):
            print("         Adder_Base[{}].A = Multiplyer_matrix[{}].Result;".format(j,j*2))
            print("         Adder_Base[{}].B = Multiplyer_matrix[{}].Result;".format(j,j*2+1))
    if (Add_i>=0)&(Add_i<80):
        print("     //Collect Partial result form Adder")
        portion = Add_i%8
        target = int(Add_i/8)
        print("         Res_{}_{}_n = Part_Res;".format(target,portion))

    if (Add_i>=0)&(Add_i<80):
        portion = Add_i%8
        target = int(Add_i/8)
        if(portion == 7):
            print("     //Feed to final Adder")
            print("         A1 = Part_Res;".format(target,portion))
            print("         A2 = Res_{}_{}_n;".format(target,portion-1))
            print("         A3 = Res_{}_{}_n;".format(target,portion-2))
            print("         A4 = Res_{}_{}_n;".format(target,portion-3))
            print("         A5 = Res_{}_{}_n;".format(target,portion-4))
            print("         A6 = Res_{}_{}_n;".format(target,portion-5))
            print("         A7 = Res_{}_{}_n;".format(target,portion-6))
            print("         A8 = Res_{}_{}_n;".format(target,portion-7))

    if (Final_i>=0)&(Final_i<80):
        portion = Final_i%8
        target = int(Final_i/8)
        if(portion ==7):
            print("     //Collect result from final Adder")
            print("         Res{}_n = Final_Res;".format(target))

    print("     end")

    
input()