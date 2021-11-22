module part_test();
    reg clk;
    reg GlobalReset;
   wire[25:0] Part_Res;
    wire[25:0] Final_Res;
    // Base
    genvar j;
    for(j = 0; j<98; j=j+1) begin:Adder_Base
        wire[25:0] A,B;
        assign A = j;
        assign B = 98-j;
        wire[25:0] Res;
        FixedPointAdder Adder( .clk(clk),.GlobalReset(~GlobalReset),.Port1(A),.Port2(B),.Output_syn(Res));
        end

    // L1
    genvar k;
    for(k = 0; k<49; k=k+1) begin:Adder_L1
        wire[25:0] Res;
        FixedPointAdder Adder( .clk(clk),.GlobalReset(~GlobalReset),.Port1(Adder_Base[k*2].Res),.Port2(Adder_Base[k*2+1].Res),.Output_syn(Res));
    end
    
    // L2
    genvar l;
    for(l=0; l<25; l=l+1) begin:Adder_L2
        wire[25:0] Res;
        if(l<24)
            FixedPointAdder Adder( .clk(clk),.GlobalReset(~GlobalReset),.Port1(Adder_L1[l*2].Res),.Port2(Adder_L1[l*2+1].Res),.Output_syn(Res));
        else
            FixedPointAdder Adder( .clk(clk),.GlobalReset(~GlobalReset),.Port1(Adder_L1[l*2].Res),.Port2(26'b0),.Output_syn(Res));
    end

    // L3
    genvar m;
    for(m=0; m<13; m=m+1) begin:Adder_L3
        wire[25:0] Res;
        if(m<12)
            FixedPointAdder Adder( .clk(clk),.GlobalReset(~GlobalReset),.Port1(Adder_L2[m*2].Res),.Port2(Adder_L2[m*2+1].Res),.Output_syn(Res));
        else
            FixedPointAdder Adder( .clk(clk),.GlobalReset(~GlobalReset),.Port1(Adder_L2[m*2].Res),.Port2(26'b0),.Output_syn(Res));
    end

    // L4
    genvar n;
    for(n=0; n<7; n=n+1) begin:Adder_L4
        wire[25:0] Res;
        if(n < 6)
            FixedPointAdder Adder( .clk(clk),.GlobalReset(~GlobalReset),.Port1(Adder_L3[n*2].Res),.Port2(Adder_L3[n*2+1].Res),.Output_syn(Res));
        else 
            FixedPointAdder Adder( .clk(clk),.GlobalReset(~GlobalReset),.Port1(Adder_L3[n*2].Res),.Port2(26'b0),.Output_syn(Res));
    end

    // L5
    genvar o;
    for(o=0; o<4; o=o+1) begin:Adder_L5
        wire[25:0] Res;
        if(o < 3)
            FixedPointAdder Adder( .clk(clk),.GlobalReset(~GlobalReset),.Port1(Adder_L4[o*2].Res),.Port2(Adder_L4[o*2+1].Res),.Output_syn(Res));
        else
            FixedPointAdder Adder( .clk(clk),.GlobalReset(~GlobalReset),.Port1(Adder_L4[o*2].Res),.Port2(26'b0),.Output_syn(Res));
    end

    // L6
    genvar p;
    for(p=0; p<2;p=p+1) begin:Adder_L6
        wire[25:0] Res;
            FixedPointAdder Adder( .clk(clk),.GlobalReset(~GlobalReset),.Port1(Adder_L5[p*2].Res),.Port2(Adder_L5[p*2+1].Res),.Output_syn(Res));
    end

    // L7
    FixedPointAdder FinalAdder( .clk(clk),.GlobalReset(~GlobalReset),.Port1(Adder_L6[0].Res),.Port2(Adder_L6[1].Res),.Output_syn(Part_Res));


    initial begin
        clk = 0;
        GlobalReset = 0;
        #10
        GlobalReset = 1;
    end

    always
        #5 clk = ~clk;
endmodule