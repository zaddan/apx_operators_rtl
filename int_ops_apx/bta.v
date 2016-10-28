//////////////////////////////////////////////////////////////
// Lower-bit OR Adder
// Author : Seogoo Lee
// Date : 2014-10-30
// Function : Lower-bit OR Adder
// Revision : v0.1 (2014-10-30) : Initial version
//////////////////////////////////////////////////////////////

`timescale 1ns/1ps

module bta (
  a,
  b,
  c
);

parameter DWA = 16;
parameter DWB = 16;
parameter DW_AC = 8;
parameter DWO = DWA > DWB ? DWA : DWB;

// generated parameter: precise bits
// parameter DW_P = DW-DW_AC;

input  [DWA-1:0]              a;
input  [DWB-1:0]              b;
output [DWO-1:0]              c;

wire [DWA-DW_AC-1:0]          a_rc;
wire [DWB-DW_AC-1:0]          b_rc;
wire [DWO-DW_AC-1:0]          c_rc;

// imprecise parts
wire [DW_AC-1:0]              a_ip;
wire [DW_AC-1:0]              b_ip;

rnd #(DWA+2, DW_AC+2) u0_rnd_clp(
  .i_din                   ({a, 2'b0}      ),
  .o_dout                  (a_rc              )
);

rnd #(DWB+2, DW_AC+2) u1_rnd_clp(
  .i_din                   ({b, 2'b0}      ),
  .o_dout                  (b_rc              )
);

assign c_rc = a_rc + b_rc;

//assign c = {c_rc, {{DW_AC}{1'b0}}};
assign c = (DW_AC == 0) ? c_rc: {c_rc, {{DW_AC}{1'b0}}};
endmodule
