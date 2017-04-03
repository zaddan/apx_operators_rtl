module conf_int_mac__noFF__arch_agnos( clk, racc, rapx, a, b, c, d
 );

//--- parameters
//parameter BT_RND = 0
parameter OP_BITWIDTH = 16; //operator bit width
parameter DATA_PATH_BITWIDTH = 16; //flip flop Bit width

//--- input,outputs
input clk;
input rapx;
input racc;
input [DATA_PATH_BITWIDTH -1:0] a;
input [DATA_PATH_BITWIDTH-1:0] b;
input [DATA_PATH_BITWIDTH-1:0] c;
output [DATA_PATH_BITWIDTH-1:0] d;

reg [DATA_PATH_BITWIDTH -1:0] a_reg;
reg [DATA_PATH_BITWIDTH-1:0] b_reg;


always @(posedge clk or negedge racc) 
begin
  if (~racc)
  begin
      a_reg[DATA_PATH_BITWIDTH - 1: DATA_PATH_BITWIDTH- OP_BITWIDTH]<= 0;
      b_reg[DATA_PATH_BITWIDTH - 1: DATA_PATH_BITWIDTH- OP_BITWIDTH]<= 0;
  end
  else
  begin
      a_reg[DATA_PATH_BITWIDTH - 1: DATA_PATH_BITWIDTH- OP_BITWIDTH]<= a[DATA_PATH_BITWIDTH - 1: DATA_PATH_BITWIDTH- OP_BITWIDTH];
      b_reg[DATA_PATH_BITWIDTH - 1: DATA_PATH_BITWIDTH- OP_BITWIDTH]<= b[DATA_PATH_BITWIDTH - 1: DATA_PATH_BITWIDTH- OP_BITWIDTH];
  end
end

always @(posedge clk or negedge rapx) 
begin
  if (~rapx)
  begin
      a_reg[DATA_PATH_BITWIDTH- OP_BITWIDTH - 1 : 0]<= 0;
      b_reg[DATA_PATH_BITWIDTH- OP_BITWIDTH - 1 : 0]<= 0;
  end
  else
  begin
      a_reg[DATA_PATH_BITWIDTH- OP_BITWIDTH - 1: 0]<= a[DATA_PATH_BITWIDTH- OP_BITWIDTH - 1: 0];
      b_reg[DATA_PATH_BITWIDTH- OP_BITWIDTH - 1: 0]<= b[DATA_PATH_BITWIDTH- OP_BITWIDTH - 1: 0];
  end
end


//--- no flop design
assign  d = (a_reg * b_reg) + c;

endmodule


module conf_int_mac__noFF__arch_agnos__w_wrapper_minus_1 ( clk, racc, rapx, a, b, c, d
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
input racc;
input rapx;

always @(posedge clk or negedge racc) 
begin
  if (~racc)
  begin
      c_reg[DATA_PATH_BITWIDTH - 1: 2*(DATA_PATH_BITWIDTH- OP_BITWIDTH)]<= 0;
  end
  else
  begin
      c_reg[DATA_PATH_BITWIDTH - 1: 2*(DATA_PATH_BITWIDTH- OP_BITWIDTH)]<= d_internal[DATA_PATH_BITWIDTH - 1: 2*(DATA_PATH_BITWIDTH- OP_BITWIDTH)];
  end
end

always @(posedge clk or negedge rapx) 
begin
  if (~rapx)
  begin
      c_reg[2*(DATA_PATH_BITWIDTH- OP_BITWIDTH) - 1 : 0]<= 0;
  end
  else
  begin
      c_reg[2*(DATA_PATH_BITWIDTH- OP_BITWIDTH) - 1: 0]<= d_internal[2*(DATA_PATH_BITWIDTH- OP_BITWIDTH) - 1: 0];
  end
end


assign d = c_reg;

conf_int_mac__noFF__arch_agnos #(OP_BITWIDTH ,DATA_PATH_BITWIDTH) mac(.clk(clk), .racc(racc), .rapx(rapx), .a(a), .b(b), .c(c),
    .d(d_internal));

endmodule 


module conf_int_mac__noFF__arch_agnos__w_wrapper ( clk, racc, rapx, a, b, d
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
input racc; //reset acc. The reason I shortened the name was to make sure the synthesized design would fit in the line (for the sake of parsing)
input rapx;

conf_int_mac__noFF__arch_agnos__w_wrapper_minus_1 #(OP_BITWIDTH, DATA_PATH_BITWIDTH) my_mac(.c(d), .d(d), .clk(clk), .racc(racc),.rapx(rapx), .a(a), .b(b));

endmodule 





