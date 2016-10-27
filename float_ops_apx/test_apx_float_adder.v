`timescale 1ns / 1ps

`define assert(signal, value) \
if (signal !== value) begin \
    $display("ASSERTION FAILED in %m: signal != value"); \
    $finish; \
end

module test_bench_tb;
  reg  clk;
  reg  rst;
  reg [31:0] input_a; //input_a
  
  //real input_a; //input_a
 
  reg input_a_stb;  //input_a_stb
  wire   input_a_ack;
  reg [31:0] input_b; //input_b
  //real input_b; //input_a
  
  reg input_b_stb; //input_b_stb
  wire   input_b_ack;
  
  wire   [31:0] output_z_acc; //output_z
  wire   output_z_stb_acc;
  wire   output_z_ack_acc;

  wire   [31:0] output_z_apx; //output_z
  wire   output_z_stb_apx;
  wire   output_z_ack_apx;



  initial
  begin
    rst <= 1'b1;
    #50 rst <= 1'b0;
  end

  
  initial
  begin
    #2000000 
    $display("accurate adder output is %b", output_z_acc);
    $display("apx adder output is %b", output_z_apx);
    `assert(output_z_acc, output_z_apx)
    `assert(output_z_acc, 31'b0)
$finish;
  
end

  
  initial
  begin
    clk <= 1'b0;
    while (1) begin
      #5 clk <= ~clk;
    end
  end
 
  initial
  begin
      #10
      //input_a <= 32'b00111111100110011001100110011010; //1.2
      //input_b <= 32'b01000000100001100110011001100110; //4.2
      //input_a <= 32'b01000000100010011001100110011010; //4.3
      //input_b <= 32'b11000000100100110011001100110011; //-4.6
      input_a <= 32'b01001010111111111111111111111110; //8388607.0      
      input_b <= 32'b01000001101000001100110011001101; //20.1

      #10 
      input_a_stb <= 1;
      input_b_stb <= 1;
  end
  
  initial
  begin
      $shm_open ("my_waves.shm"); //necessary to dump the signals
      //$Dumpvars(1,test_bench_tb );
      $shm_probe("AS"); //probing for all the signals 
      /* 
      $shm_probe ( clk,
          rst,
          input_a,
          input_a_stb,
          input_a_ack,
          input_b,
          input_b_stb,
          input_b_ack,
          output_z,
          output_z_reg, 
          output_z_stb,
          output_z_ack);
      */
  
  end
  

  adder adder_39759952_acc(
    .clk(clk),
    .rst(rst),
    .input_a(input_a),
    .input_a_stb(input_a_stb),
    .input_a_ack(input_a_ack),
    .input_b(input_b),
    .input_b_stb(input_b_stb),
    .input_b_ack(input_b_ack),
    .output_z(output_z_acc),
    .output_z_stb(output_z_stb_acc),
    .output_z_ack(output_z_ack_acc));


  apx_float_adder #(0) adder_39759952_apx(
    .clk(clk),
    .rst(rst),
    .input_a(input_a),
    .input_a_stb(input_a_stb),
    .input_a_ack(input_a_ack),
    .input_b(input_b),
    .input_b_stb(input_b_stb),
    .input_b_ack(input_b_ack),
    .output_z(output_z_apx),
    .output_z_stb(output_z_stb_apx),
    .output_z_ack(output_z_ack_apx));

endmodule
