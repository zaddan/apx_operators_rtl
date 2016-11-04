`timescale 1ns / 1ps

`define assert(signal, value) \
if (signal !== value) begin \
    $display("@@@@@@@@@@ASSERTION FAILED in %m: signal != value"); \
    $finish; \
end

//`define BT_RND

module test_bench_tb;
  reg  clk;
  reg  rst;
  reg [31:0] input_a; //input_a
  
  reg [63:0] double_input_a;//this is necessary b/c bitstoreal get a 64 bit, which means we need to convert all the 32 bit values we want to write as float to double
  reg [63:0] double_input_b;//this is necessary b/c bitstoreal get a 64 bit, which means we need to convert all the 32 bit values we want to write as float to double
  reg [63:0] double_output_z_apx;//this is necessary b/c bitstoreal get a 64 bit, which means we need to convert all the 32 bit values we want to write as float to double



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
  
  parameter number_of_input_pairs = 50000; 
  parameter NAB = 0; 
  parameter BT_RND = 1; 
  //variables to read from a file 
  reg [31:0] data [0:2*number_of_input_pairs - 1];
  // initialize the hexadecimal reads from the vectors.txt file
  initial $readmemh("float_values_in_hex.txt", data);
  integer i;
  
  integer f;
  integer f2; //file 2 identiier (to write)
  initial begin
      if (BT_RND == 1) begin
          f = $fopen("BT_RND.txt","w");
          f2 = $fopen("BT_RND_acc_vs_apx.txt","w");
      end
      else begin
          f = $fopen("TRUNCATION.txt","w");
          f2 = $fopen("TRUNCATION_acc_vs_apx.txt","w");
      end
  end
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
           #2600 
           output_z_ack_apx_reg <= 1;
           output_z_ack_acc_reg <= 1;
           #2
           /* 
           double_input_a = {input_a[31], input_a[30], {3{~input_a[30]}}, input_a[29:23], input_a[22:0], {29{1'b0}}};
           double_input_b = {input_b[31], input_b[30], {3{~input_b[30]}}, input_b[29:23], input_b[22:0], {29{1'b0}}};
           double_output_z_apx = {output_z_apx[31], output_z_apx[30], {3{~output_z_apx[30]}}, output_z_apx[29:23], output_z_apx[22:0], {29{1'b0}}};
           
           $fwrite(f,"%f %f %f \n",$bitstoreal(double_input_a), $bitstoreal(double_input_b) , $bitstoreal(double_output_z_apx));
           */
           
          //$fwrite(f,"%x %x %x\n",input_a, input_b , output_z_apx);
          $fwrite(f2,"%x %x %x %x \n",input_a, input_b, output_z_acc, output_z_apx);
          $fwrite(f,"%x %x %x\n",input_a, input_b , output_z_apx);
          
          if (NAB == 0)begin
               `assert(output_z_acc, output_z_apx)
            end
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
      #170000000
      $fclose(f); 
      $fclose(f2); 
      $finish;
  end


  multiplier multiplier_39759952_acc(
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


  apx_float_multiplier #(NAB, BT_RND) multiplier_39759952_apx(
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
