`timescale 1ns / 1ps

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
  wire   [31:0] output_z; //output_z
  real output_z_reg; 
  wire   output_z_stb;
  wire   output_z_ack;

  initial
  begin
    rst <= 1'b1;
    #50 rst <= 1'b0;
  end

  
  initial
  begin
    #2000000 
    $display("adder output is %b", output_z);
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
  

  adder #(9) adder_39759952(
    .clk(clk),
    .rst(rst),
    .input_a(input_a),
    .input_a_stb(input_a_stb),
    .input_a_ack(input_a_ack),
    .input_b(input_b),
    .input_b_stb(input_b_stb),
    .input_b_ack(input_b_ack),
    .output_z(output_z),
    .output_z_stb(output_z_stb),
    .output_z_ack(output_z_ack));


  adder #(9) adder_39759952(
    .clk(clk),
    .rst(rst),
    .input_a(input_a),
    .input_a_stb(input_a_stb),
    .input_a_ack(input_a_ack),
    .input_b(input_b),
    .input_b_stb(input_b_stb),
    .input_b_ack(input_b_ack),
    .output_z(output_z),
    .output_z_stb(output_z_stb),
    .output_z_ack(output_z_ack));

endmodule
