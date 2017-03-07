

module conf_int_mac__noFF__redundant_ports(clk, rst, a_h,a, b_h, b, c_h, c, d);
//--- parameters
//parameter BT_RND = 0
parameter OP_BITWIDTH = 16; //operator bit width
parameter DATA_PATH_BITWIDTH = 16; //flip flop Bit width
parameter Pn = 12; //lowest precision requrested

//--- input,outputs
input clk;
input rst;
input [DATA_PATH_BITWIDTH -1:0] a;
input [DATA_PATH_BITWIDTH-1:0] b;
input [DATA_PATH_BITWIDTH-1:0] c;
input [31: Pn] a_h;
input [31: Pn] b_h;
input [31: (2*Pn)] c_h;
output [DATA_PATH_BITWIDTH-1:0] d;


//--- no flop design
wire [31:0] L_L;
wire [31:0] H_L;
wire [31:0] L_H;
wire [31:0] H_H;
wire [31:0] H_L_shifted;
wire [31:0] L_H_shifted;
wire [31:0] H_H_shifted;
wire [31:0] top_half;
wire [31:0] bottom_half;
wire [31:0] mul_res;

assign L_L = a[Pn-1:0] * b[Pn-1:0];
assign H_L = a[31:Pn] * b[Pn-1:0];
assign L_H = a[Pn-1:0] * b[31:Pn];
assign H_H = a_h * b_h;

assign H_L_shifted = H_L << Pn;
assign L_H_shifted = L_H << Pn;
assign H_H_shifted = H_H << (2*Pn);

assign top_half = H_H_shifted + L_H_shifted;
assign bottom_half = H_L_shifted + L_L;
assign mul_res = bottom_half + top_half;
assign d = mul_res + c; 

endmodule


module conf_int_mac__noFF__wrapper(clk, rst, a, b, c, d);
    parameter OP_BITWIDTH = 16; //operator bit width
    parameter DATA_PATH_BITWIDTH = 16; //flip flop Bit width
    parameter Pn = 12; //lowest precision requrested
    
    
    //--- input,outputs
    input clk;
    input rst;
    input [DATA_PATH_BITWIDTH -1:0] a;
    input [DATA_PATH_BITWIDTH-1:0] b;
    input [DATA_PATH_BITWIDTH-1:0] c;
    output [DATA_PATH_BITWIDTH-1:0] d;
    
    
    //*** F:DN Body 
    conf_int_mac__noFF__redundant_ports  #(OP_BITWIDTH, DATA_PATH_BITWIDTH, Pn) mac(.clk(clk),
        .rst(rst), .a_h(a[31:Pn]),.a(a), .b_h(b[31: Pn]), .b(b), .c_h(c[31: (2*Pn)]), .c(c), .d(d));
endmodule
