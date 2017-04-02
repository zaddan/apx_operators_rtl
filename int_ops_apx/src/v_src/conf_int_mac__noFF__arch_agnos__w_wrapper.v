module conf_int_mac__noFF__arch_agnos( clk, rst, a, b, c, d
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
input [DATA_PATH_BITWIDTH-1:0] c;
output [DATA_PATH_BITWIDTH-1:0] d;

reg [DATA_PATH_BITWIDTH -1:0] a_reg;
reg [DATA_PATH_BITWIDTH-1:0] b_reg;


always @(posedge clk or negedge rst)
begin
  if (~rst)
  begin
      a_reg <= 0;
      b_reg <= 0;
  end
  else
  begin
      a_reg <= a;
      b_reg <= b;
  end
end


//--- no flop design
assign  d = (a_reg * b_reg) + c;

endmodule


module conf_int_mac__noFF__arch_agnos__w_wrapper_minus_1 ( clk, rst, a, b, c, d
);

//--- parameters
//parameter BT_RND = 0
parameter OP_BITWIDTH = 16; //operator bit width
parameter DATA_PATH_BITWIDTH = 16; //flip flop Bit width


//--- input,outputs
input [DATA_PATH_BITWIDTH -1:0] a;
input [DATA_PATH_BITWIDTH-1:0] b;
reg [DATA_PATH_BITWIDTH-1:0] c_reg;
input [DATA_PATH_BITWIDTH-1:0] c;
output [DATA_PATH_BITWIDTH-1:0] d;
wire [DATA_PATH_BITWIDTH-1:0] d_internal;
input clk;
input rst;


always @(posedge clk or negedge rst)
begin
  if (~rst)
  begin
      c_reg <= 0;
  end
  else
  begin
      c_reg <= d_internal; 
  end
end

assign d = c_reg;

conf_int_mac__noFF__arch_agnos #(DATA_PATH_BITWIDTH, OP_BITWIDTH) mac(.clk(clk), .rst(rst), .a(a), .b(b), .c(c),
    .d(d_internal));

endmodule 


module conf_int_mac__noFF__arch_agnos__w_wrapper ( clk, rst, a, b, d
);

//--- parameters
//parameter BT_RND = 0
parameter OP_BITWIDTH = 16; //operator bit width
parameter DATA_PATH_BITWIDTH = 16; //flip flop Bit width


//--- input,outputs
input [DATA_PATH_BITWIDTH -1:0] a;
input [DATA_PATH_BITWIDTH-1:0] b;
//wire [DATA_PATH_BITWIDTH-1:0] c; // synopsys keep_signal_name "c"
output [DATA_PATH_BITWIDTH-1:0] d;


//assign c = d; 
//assign c = {d[Pn:0], Pn'b0};


input clk;
input rst;

conf_int_mac__noFF__arch_agnos__w_wrapper_minus_1 #(DATA_PATH_BITWIDTH, OP_BITWIDTH) my_mac(.clk(clk), .rst(rst), .a(a), .b(b), .c(d),
    .d(d));

endmodule 





