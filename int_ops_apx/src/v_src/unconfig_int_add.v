`timescale 1ns/1ps




//--- the following configuratble adder uses input Mux
//for the purpose of truncation
module unconfig_int_add(
 clk,
 rst,
 a,
 b,
 c
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
output [DATA_PATH_BITWIDTH-1:0] c;


////---F: Ripple Cary Adder deisng
////module test ripple_adder_4bit; 
//wire Cout;
// // Instantiate the Unit Under Test (UUT)
//ripple_adder_4bit uut (
//  .Sum(c[3:0]), 
//  .Cout(Cout), 
//  .A(a[3:0]), 
//  .B(b[3:0]), 
//  .Cin(a[0])
// );


//--- F: simple design
wire o_temp_1, o_temp_2, o_temp_3;

//and(o_temp_1, a[0], b[0]);
nand(nand_a, a[0], a[1]);
nand(nand_b, b[0], b[1]);
nor(c[0], nand_a, nand_b);

//not(a_not_0, a[0]);
//not(a_not_1, a[1]);
//not(b_not_0, b[0]);
//not(b_not_1, b[1]);
//or(ors_a, a_not_0, a_not_1);
//or(ors_b, b_not_0, b_not_1);
//nor(c[0], ors_a, ors_b);

//not(a_not, a);
//not(b_not, b);
//or(c[0], a_not, b_not);

//not(o_temp_2, o_temp_1);
//t(c[0], o_temp_2);
//or(c[0], o_temp_1, o_temp_2);


//--- no flop design
//assign c = a * b;

/*
//--- regs, wires
reg [DATA_PATH_BITWIDTH-1:0]  reg_c;
wire [OP_BITWIDTH -1 : 0]w_c;
reg [DATA_PATH_BITWIDTH -1:0]  reg_a;
reg [DATA_PATH_BITWIDTH -1:0]  reg_b;


//--- design
acc_int_add #(OP_BITWIDTH) u0_ac (reg_a[DATA_PATH_BITWIDTH -1: DATA_PATH_BITWIDTH - OP_BITWIDTH], reg_b[DATA_PATH_BITWIDTH -1: DATA_PATH_BITWIDTH - OP_BITWIDTH], w_c);

always @(posedge clk or negedge rst)
begin
  if (~rst)
  begin
    reg_a <= 0;
    reg_b <= 0;
  end
  else 
  begin
      reg_a <= a;
      reg_b <= b;
  end
end

always @(posedge clk or negedge rst)
begin
  if (~rst)
  begin
    reg_c <= #0.1 0;
  end
  else 
  begin
    reg_c[DATA_PATH_BITWIDTH-1: DATA_PATH_BITWIDTH-OP_BITWIDTH] <= w_c;
  end
end

assign c = reg_c; 

*/
endmodule

