`timescale 1ns / 1ps

//generates two outputs:
//f: file which contains in1, in2 and the result of the apx adder
//f2: file which contains acc_adder and apx_adder results
//note: if NAB (Number of Appx Bits) == 0, it also compares the value of accurate
    //and approximate to ensure the sanity of the design
`define assert(signal, value) \
if (signal !== value) begin \
    $display("@@@@@@@@@@ASSERTION FAILED in %m: signal != value"); \
    $finish; \
end


module test_bench_tb;
reg  clk;
reg  rst;
reg [31:0] input_a; //input_a
reg input_a_stb;  //input_a_stb
wire   input_a_ack;
reg [31:0] input_b; //input_b
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

wire   [31:0] output_z_apx_2; //output_z
wire   output_z_stb_apx_2;
wire   output_z_ack_apx_2;
reg output_z_ack_apx_reg_2;

/*
reg [63:0] double_input_a;//this is necessary b/c bitstoreal get a 64 bit, which means we need to convert all the 32 bit values we want to write as float to double
reg [63:0] double_input_b;//this is necessary b/c bitstoreal get a 64 bit, which means we need to convert all the 32 bit values we want to write as float to double
reg [63:0] double_output_z_apx;//this is necessary b/c bitstoreal get a 64 bit, which means we need to convert all the 32 bit values we want to write as float to double
*/

//--- parameters
parameter number_of_input_pairs = 50000; 
parameter BT_RND = 0; 
parameter NAB = 10;  

//variables to read from a file 
reg [31:0] data [0:2*number_of_input_pairs - 1];
// initialize the hexadecimal reads from the vectors.txt file
initial $readmemh("float_values_in_hex.txt", data);
  integer i;
  integer f; //file 1 to write
  integer f2;  //file 2 identifier (to write)
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
      for (i=0; i < number_of_input_pairs; i = i + 1)begin
          #10
          output_z_ack_apx_reg <= 0;
          output_z_ack_acc_reg <= 0;
          output_z_ack_apx_reg_2 <= 0;

          input_a <= data[2*i];
          input_b <= data[2*i + 1];
          #100 
          input_a_stb <= 1;
          input_b_stb <= 1;
          #2000 
          output_z_ack_apx_reg <= 1;
          output_z_ack_acc_reg <= 1;
          output_z_ack_apx_reg_2<= 1;

          /*
          double_input_a = {input_a[31], input_a[30], {3{~input_a[30]}}, input_a[29:23], input_a[22:0], {29{1'b0}}};
          double_input_b = {input_b[31], input_b[30], {3{~input_b[30]}}, input_b[29:23], input_b[22:0], {29{1'b0}}};
          double_output_z_apx = {output_z_apx[31], output_z_apx[30], {3{~output_z_apx[30]}}, output_z_apx[29:23], output_z_apx[22:0], {29{1'b0}}};
          //$fwrite(f,"%f %f %f \n",$bitstoreal(double_input_a), $bitstoreal(double_input_b) , $bitstoreal(double_output_z_apx), output_z_apx);
          */ 
        
         //$display(,"%x %x \n",output_z_acc, output_z_apx);
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
     #100000000
     $fclose(f); 
     $fclose(f2); 
     $finish;
 end


 //---accurate adder instantiated
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

 //---apx adder (either rounding or apx) instantiated
 apx_float_adder #(NAB, BT_RND) adder_39759952_apx(
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

 //--- apx_adder instantiated only approximated
 apx_float_adder#(NAB, 0) adder_39759952_apx_2(
     .clk(clk),
     .rst(rst),
     .input_a(input_a),
     .input_a_stb(input_a_stb),
     .input_a_ack(input_a_ack),
     .input_b(input_b),
     .input_b_stb(input_b_stb),
     .input_b_ack(input_b_ack),
     .output_z(output_z_apx_2),
     .output_z_stb(output_z_stb_apx_2),
     .output_z_ack(output_z_ack_apx_reg_2));
 endmodule
