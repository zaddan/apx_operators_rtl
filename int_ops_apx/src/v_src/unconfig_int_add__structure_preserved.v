
module unconfig_int_add ( clk, rst, a, b, c
 );
  input [31:0] a; 
  input [31:0] b;
  output [31:0] c;
  input clk, rst;

  wire a_not, b_not; 
  
  // --- F: forces the HDL compiler to not destroy the logic (or rather optimize) 
  // synopsys dc_script_begin
  // set_dont_touch a_not
  // set_dont_touch b_not
  // synopsys dc_script_end
  
  //--- note the following can be structural or behavioral 
  assign a_not = ~a[0];
  assign b_not = ~b[0];
  //assign c[0] = a_not & b_not;
  AND2_X2 U3(.A1(a_not), .A2(b_not), .ZN(c[0]));
 
  
  //  not(a_not, a[0]);
//  not(b_not, b[0]);
//  and(c[0], a_not, b_not);

  endmodule

