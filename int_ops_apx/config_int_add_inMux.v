`timescale 1ns/1ps

//--- the following configuratble adder uses input Mux
//for the purpose of truncation
module config_int_add_inMux_truncation(
 clk,
 rst,
 apx_ctl,  
 a,
 b,
 c
);

//parameter BT_RND = 0
parameter BWOP = 32;
parameter NAB = 0; //this can not be 0, otherwise it'll error out

input clk;
input rst;
input [BWOP-1:0] a;
input [BWOP-1:0] b;
output [BWOP-1:0] c;
input apx_ctl;

reg [BWOP-1:0]  reg_c;
wire [BWOP-1:0]  w_c;
wire [BWOP-1:0] a_apx;
wire [BWOP-1:0] b_apx;
assign a_apx = apx_ctl ? {a[BWOP-1: NAB], {{NAB}{1'b0}}} : a;
assign b_apx = apx_ctl ? {b[BWOP-1: NAB], {{NAB}{1'b0}}} : b;
acc_int_add #(BWOP) u0_ac (a_apx, b_apx, w_c);

always @(posedge clk or negedge rst)
begin
  if (~rst)
  begin
    reg_c <= #1 0;
  end
  else 
  begin
    reg_c <= #1 w_c;
  end
end

assign c = reg_c;

endmodule

