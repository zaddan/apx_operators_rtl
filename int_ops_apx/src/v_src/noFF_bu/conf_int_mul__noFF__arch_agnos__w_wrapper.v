module conf_int_mul__noFF__arch_agnos( clk, rst, a, b, d
 );

//--- parameters
//parameter BT_RND = 0
parameter OP_BITWIDTH = 16; //operator bit width
parameter DATA_PATH_BITWIDTH = 16; //flip flop Bit width

//--- input,outputs
input clk;
input rst;
input [DATA_PATH_BITWIDTH -1:0] a;
input [DATA_PATH_BITWIDTH-1:0] b;
output [DATA_PATH_BITWIDTH-1:0] d;


//--- no flop design
assign  d = (a * b);

endmodule


module conf_int_mul__noFF__arch_agnos__w_wrapper( clk, rst, a, b, d
);

//--- parameters
//parameter BT_RND = 0
parameter OP_BITWIDTH = 16; //operator bit width
parameter DATA_PATH_BITWIDTH = 16; //flip flop Bit width


//--- input,outputs
input [DATA_PATH_BITWIDTH -1:0] a;
input [DATA_PATH_BITWIDTH-1:0] b;
output [DATA_PATH_BITWIDTH-1:0] d;
input clk;
input rst;

conf_int_mul__noFF__arch_agnos #(DATA_PATH_BITWIDTH, OP_BITWIDTH) mul(.clk(clk), .rst(rst), .a(a), .b(b), 
    .d(d));

endmodule 
