`timescale 1ns/1ps

//--- the following configuratble adder uses input Mux
//for the purpose of truncation
module config_int_add_clkGate(
 clk,
 rst,
 reg_en, 
 a,
 b,
 c
);

//parameter BT_RND = 0
//--- parameters
parameter DATA_PATH_BITWIDTH = 32;  //data path bits
parameter CLKGATED_BITWIDTH = 16; //number of clock gated bits

//--- input,outputs
input clk;
input rst;
input [DATA_PATH_BITWIDTH-1:0] a;
input [DATA_PATH_BITWIDTH-1:0] b;
output [DATA_PATH_BITWIDTH-1:0] c;
input reg_en;

//--- wires,regs
reg [DATA_PATH_BITWIDTH-1:0]  reg_a;
reg [DATA_PATH_BITWIDTH-1:0]  reg_b;
reg [DATA_PATH_BITWIDTH-1:0]  reg_c;
wire [DATA_PATH_BITWIDTH-1:0]  w_c;


//--- design
acc_int_add #(DATA_PATH_BITWIDTH) u0_ac (reg_a, reg_b, w_c);

//--- clk gating inputs
always @(posedge clk or negedge rst)
begin
  if (~rst)
  begin
    reg_a[DATA_PATH_BITWIDTH -1: CLKGATED_BITWIDTH] <= #0.1 0;
    reg_b[DATA_PATH_BITWIDTH -1: CLKGATED_BITWIDTH] <= #0.1 0;
  end
  else 
  begin
    reg_a[DATA_PATH_BITWIDTH-1: CLKGATED_BITWIDTH] <= a[DATA_PATH_BITWIDTH-1:CLKGATED_BITWIDTH];
    reg_b[DATA_PATH_BITWIDTH-1: CLKGATED_BITWIDTH] <= b[DATA_PATH_BITWIDTH-1:CLKGATED_BITWIDTH];
  end
end

always @(posedge clk or negedge rst)
begin
  if (~rst)
  begin
    reg_a[CLKGATED_BITWIDTH-1:0] <= #0.1 0;
    reg_b[CLKGATED_BITWIDTH-1:0] <= #0.1 0;
  end
  else if (rst && reg_en)
  begin
    reg_a[CLKGATED_BITWIDTH-1:0] <= a[CLKGATED_BITWIDTH-1:0];
    reg_b[CLKGATED_BITWIDTH-1:0] <= b[CLKGATED_BITWIDTH-1:0];
  end
end

//--- clk gating output
always @(posedge clk or negedge rst)
begin
  if (~rst)
  begin
    reg_c[DATA_PATH_BITWIDTH -1: CLKGATED_BITWIDTH] <= #0.1 0;
  end
  else 
  begin
    reg_c[DATA_PATH_BITWIDTH-1: CLKGATED_BITWIDTH] <= w_c[DATA_PATH_BITWIDTH-1:CLKGATED_BITWIDTH];
  end
end

always @(posedge clk or negedge rst)
begin
  if (~rst)
  begin
    reg_c[CLKGATED_BITWIDTH-1:0] <= #0.1 0;
  end
  else if (rst && reg_en)
  begin
    reg_c[CLKGATED_BITWIDTH-1:0] <= w_c[CLKGATED_BITWIDTH-1:0];
  end
end




/*
always @(posedge clk or negedge rst)
begin
  if (~rst)
  begin
    reg_c <= #0.1 0;
  end
  else 
  begin
    reg_c <= w_c;
  end
end
*/
assign c = reg_c;

endmodule

