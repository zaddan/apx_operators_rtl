module conf_int_add__noFF__arch_agnos( clk, rst, a, b, d
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
output [DATA_PATH_BITWIDTH :0] d;


//--- no flop design
assign  d = (a + b);

endmodule


module conf_int_add__noFF__arch_agnos__w_wrapper( clk, rst, a, b, d
,d__acc, acc__sel);

//--- parameters
//parameter BT_RND = 0
parameter OP_BITWIDTH = 16; //operator bit width
parameter DATA_PATH_BITWIDTH = 16; //flip flop Bit width


//--- input,outputs
input [DATA_PATH_BITWIDTH -1:0] a;
input [DATA_PATH_BITWIDTH-1:0] b;
input [32:0] d__acc;
input acc__sel;
output [32:0] d;
input clk;
input rst;

wire [DATA_PATH_BITWIDTH:0] d__apx;
// synopsys dc_script_begin
 //set_dont_touch d__apx
 //set_dont_touch d__acc
 // synopsys dc_script_end


conf_int_add__noFF__arch_agnos #(OP_BITWIDTH, DATA_PATH_BITWIDTH) add__inst(.clk(clk), .rst(rst), .a(a), .b(b), 
    .d(d__apx));

assign d[32: (32-DATA_PATH_BITWIDTH)] = acc__sel ? d__acc[32: 32-DATA_PATH_BITWIDTH] : d__apx;
assign  d[32-DATA_PATH_BITWIDTH - 1 : 0]= acc__sel ? d__acc[32-DATA_PATH_BITWIDTH - 1 : 0]:{(32-DATA_PATH_BITWIDTH){1'b0}};


endmodule 
