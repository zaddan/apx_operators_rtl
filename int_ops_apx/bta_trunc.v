//////////////////////////////////////////////////////////////
// Lower-bit OR Adder
// Author : Seogoo Lee
// Date : 2014-10-30
// Function : Lower-bit OR Adder
// Revision : v0.1 (2014-10-30) : Initial version
//////////////////////////////////////////////////////////////

`timescale 1ns/1ps

module bta_trunc (
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

wire [DWO-DW_AC-1:0]          c_rc;
assign c_rc = a[DWA-1:DW_AC] + b[DWB-1:DW_AC];
assign c = (DW_AC == 0) ? c_rc: {c_rc, {{DW_AC}{1'b0}}};

endmodule
