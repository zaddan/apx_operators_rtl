`timescale 1ns/1ps

module acc_adder (
  input [32:0] a,
  input [32:0] b,
  output [32: 0] c
);
assign c = a + b;

endmodule
