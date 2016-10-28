//////////////////////////////////////////////////////////////
// Bio-Inspired Multiplier (BAM)
// Author : Seogoo Lee
// Date : 2014-10-30
// Function : Bio-Inspired Multiplier 
// Revision : v0.1 (2014-10-30) : Initial version
//////////////////////////////////////////////////////////////

`timescale 1ns/1ps

module btm_trunc (
  a,
  b,
  c
);

parameter DA = 10;
parameter DB = 10;
parameter DAC = 1;
parameter DO = DA+DB-1;

input  [DA-1:0]                                   a;
input  [DB-1:0]                                   b;
output [DO-1:0]                                   c;

wire                                              a_sign;
wire                                              b_sign;
wire                                              c_sign;

wire   [DA-DAC-1:0]                               a_abs;
wire   [DB-DAC-1:0]                               b_abs;
wire   [DO-DAC-DAC-1:0]                           c_abs_pre;
wire   [DO-DAC-DAC-1:0]                           c_pre;

/*
assign a_sign = a[DA-1];
assign b_sign = b[DB-1];
assign c_sign = a_sign != b_sign ? 1 : 0;

assign a_abs = a_sign ? -a[DA-1:DAC] : a[DA-1:DAC];
assign b_abs = b_sign ? -b[DB-1:DAC] : b[DB-1:DAC];

assign c_abs_pre = a_abs * b_abs;
*/

assign c_pre = a[DA-1:DAC] * b[DB-1:DAC];
assign c = (DAC == 0) ? c_pre: {c_pre, {{2*DAC}{1'b0}}};
//assign c = {c_pre, {{2*DAC}{1'b0}}};

endmodule
