`timescale 1ns / 1ps

`define assert(signal, value) \
if (signal !== value) begin \
    $display("@@@@@@@@@@ASSERTION FAILED in %m: signal != value"); \
    //$finish; \
end


`define BT_RND
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
  reg output_z_ack_acc_reg;


  wire   [31:0] output_z_apx; //output_z
  wire   output_z_stb_apx;
  wire   output_z_ack_apx;
  reg output_z_ack_apx_reg;
  
  parameter number_of_input_pairs = 8; 
  //variables to read from a file 
  reg [31:0] data [0:2*number_of_input_pairs - 1];
  // initialize the hexadecimal reads from the vectors.txt file
  initial $readmemh("float_values_in_hex.txt", data);
  integer i;
  
  
  //reset 
  initial
  begin
    rst <= 1'b1;
    #50 rst <= 1'b0;
  end

  
  //clk 
  initial
  begin
    clk <= 1'b0;
    while (1) begin
      #5 clk <= ~clk;
    end
  end
 
  
  //sample input, generate results, compare results 
  initial
  begin
      //input_a <= 32'b00111111100110011001100110011010; //1.2
      //input_b <= 32'b01000000100001100110011001100110; //4.2
      //input_a <= 32'b01000000100010011001100110011010; //4.3
      //input_b <= 32'b11000000100100110011001100110011; //-4.6
      //input_a <= 32'b01001010111111111111111111111110; //8388607.0      
      //input_b <= 32'b01000001101000001100110011001101; //20.1
      for (i=0; i < number_of_input_pairs; i = i + 1)begin
           #10
           output_z_ack_apx_reg <= 0;
           output_z_ack_acc_reg <= 0;
           //$display("%d:%h",i,data[i]);
           //$display("%d:%h",i,data[i+1]);
           input_a <= data[2*i];
           input_b <= data[2*i + 1];
           #100 
           input_a_stb <= 1;
           input_b_stb <= 1;
           #1000 
           $display("====================================");
           $display("input_a is %x", input_a);
           $display("input_b is %x", input_b);
           $display("accurate adder output is %x", output_z_acc);
           $display("apx adder output is %x", output_z_apx);
           $display(" ");
           output_z_ack_apx_reg <= 1;
           output_z_ack_acc_reg <= 1;
           #10           
           `assert(output_z_acc, output_z_apx)
           

      end
  end
  
  
  //generate waves
  initial
  begin
      $shm_open ("my_waves.shm"); //necessary to dump the signals
      //$Dumpvars(1,test_bench_tb );
      $shm_probe("AS"); //probing for all the signals 
  end
  
  
  //finish
  initial
  begin
      #2000000 

      $finish;
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
    .output_z_ack(output_z_ack_acc_reg));


  apx_float_adder #(3) adder_39759952_apx(
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
    .output_z_ack(output_z_ack_apx_reg));

endmodule
