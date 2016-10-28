//////////////////////////////////////////////////////////////
// Bio-Inspired Multiplier (BAM)
// Author : Seogoo Lee
// Date : 2014-10-30
// Function : Bio-Inspired Multiplier 
// Revision : v0.1 (2014-10-30) : Initial version
//////////////////////////////////////////////////////////////

`timescale 1ns/1ps

module btm (
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

wire   [DA-DAC-1:0]                               a_rc;
wire   [DB-DAC-1:0]                               b_rc;

wire   [DA-DAC-1:0]                               a_abs;
wire   [DB-DAC-1:0]                               b_abs;
wire   [DO-DAC-DAC-1:0]                           c_abs_pre;
wire   [DO-DAC-DAC-1:0]                           c_pre;

rnd #(DA+2, DAC+2) u0_rnd(
  .i_din                   ({a, 2'b0}      ),
  .o_dout                  (a_rc              )
);

rnd #(DB+2, DAC+2) u1_rnd(
  .i_din                   ({b, 2'b0}      ),
  .o_dout                  (b_rc              )
);

//assign a_sign = a_rc[DA-DAC-1];
//assign b_sign = b_rc[DB-DAC-1];
//assign c_sign = a_sign != b_sign ? 1 : 0;

//assign a_abs = a_sign ? -a_rc : a_rc;
//assign b_abs = b_sign ? -b_rc : b_rc;

//assign c_abs_pre = a_abs * b_abs;
//assign c_pre = c_sign ? -c_abs_pre : c_abs_pre;
assign c_pre = a_rc * b_rc;
//assign c = {c_pre, {{2*DAC}{1'b0}}};
assign c = (DAC == 0) ? c_pre: {c_pre, {{2*DAC}{1'b0}}};

endmodule
