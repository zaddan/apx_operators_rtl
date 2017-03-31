/////////////////////////////////////////////////////////////
// Created by: Synopsys DC Ultra(TM) in wire load mode
// Version   : L-2016.03-SP5-3
// Date      : Thu Mar 30 17:13:38 2017
/////////////////////////////////////////////////////////////


module conf_int_add__noFF__arch_agnos_OP_BITWIDTH32_DATA_PATH_BITWIDTH32 ( clk, 
        rst, a, b, d );
  input [31:0] a;
  input [31:0] b;
  output [31:0] d;
  input clk, rst;
  wire   n92, n146, n147, n170, n149, n148, n159, n155, n156, n154, n150, n152,
         n151, n153, n157, n158, n160, n168, n167, n161, n166, n162, n164,
         n163, n165, n169, n171, n181, n177, n178, n176, n172, n174, n173,
         n175, n179, n180, n182, n184, n183, n186, n185, n3, n2, n5, n7, n4,
         n6, n1, \intadd_1/n3 , \intadd_1/n2 , \intadd_1/n1 , n8, n9, n10, n11,
         n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23, n24, n25,
         n26, n27, n28, n29, n30, n31, n32, n33, n34, n35, n36, n37, n38, n39,
         n40, n41, n42, n43, n44, n45, n46, n47, n48, n49, n50, n53, n54, n55,
         n56, n57, n58, n59, n60, n61, n62, n63, n64, n65, n66, n67, n68, n69,
         n70, n71, n72, n73, n74, n75, n76, n77, n80, n81, n82, n83, n84, n85,
         n86, n87, n88, n89, n90, n91, n93, n94, n95, n96, n97, n98, n99, n100,
         n101, n102, n103, n104, n105, n106, n107, n108, n109, n110, n111,
         n112, n113, n114, n115, n116, n117, n118, n119, n120, n121, n122,
         n123, n124, n125, n126, n127, n128, n129, n130, n131, n132, n133,
         n134, n135, n136, n137, n138, n139, n140, n141, n142, n143, n144,
         n145, n187, n188, n190, n191;

  INV_X1 U150 ( .A(n92), .ZN(n146) );
  INV_X1 U190 ( .A(n147), .ZN(n170) );
  AOI21_X1 U191 ( .B1(n170), .B2(n149), .A(n148), .ZN(n159) );
  OAI21_X1 U192 ( .B1(n159), .B2(n155), .A(n156), .ZN(n154) );
  INV_X1 U193 ( .A(n150), .ZN(n152) );
  NAND2_X1 U194 ( .A1(n152), .A2(n151), .ZN(n153) );
  XNOR2_X1 U195 ( .A(n154), .B(n153), .ZN(d[7]) );
  INV_X1 U196 ( .A(n155), .ZN(n157) );
  NAND2_X1 U197 ( .A1(n157), .A2(n156), .ZN(n158) );
  XOR2_X1 U198 ( .A(n159), .B(n158), .Z(d[6]) );
  INV_X1 U199 ( .A(n160), .ZN(n168) );
  INV_X1 U200 ( .A(n167), .ZN(n161) );
  AOI21_X1 U201 ( .B1(n170), .B2(n168), .A(n161), .ZN(n166) );
  INV_X1 U202 ( .A(n162), .ZN(n164) );
  NAND2_X1 U203 ( .A1(n164), .A2(n163), .ZN(n165) );
  XOR2_X1 U204 ( .A(n166), .B(n165), .Z(d[5]) );
  NAND2_X1 U205 ( .A1(n168), .A2(n167), .ZN(n169) );
  XNOR2_X1 U206 ( .A(n170), .B(n169), .ZN(d[4]) );
  INV_X1 U207 ( .A(n171), .ZN(n181) );
  OAI21_X1 U208 ( .B1(n181), .B2(n177), .A(n178), .ZN(n176) );
  INV_X1 U209 ( .A(n172), .ZN(n174) );
  NAND2_X1 U210 ( .A1(n174), .A2(n173), .ZN(n175) );
  XNOR2_X1 U211 ( .A(n176), .B(n175), .ZN(d[3]) );
  INV_X1 U212 ( .A(n177), .ZN(n179) );
  NAND2_X1 U213 ( .A1(n179), .A2(n178), .ZN(n180) );
  XOR2_X1 U214 ( .A(n181), .B(n180), .Z(d[2]) );
  INV_X1 U215 ( .A(n182), .ZN(n184) );
  NAND2_X1 U216 ( .A1(n184), .A2(n183), .ZN(n186) );
  XOR2_X1 U217 ( .A(n186), .B(n185), .Z(d[1]) );
  INV_X1 U173 ( .A(n146), .ZN(n190) );
  NAND2_X1 U10 ( .A1(a[0]), .A2(b[0]), .ZN(n185) );
  NOR2_X1 U12 ( .A1(a[1]), .A2(b[1]), .ZN(n182) );
  NAND2_X1 U13 ( .A1(a[1]), .A2(b[1]), .ZN(n183) );
  OAI21_X1 U14 ( .B1(n182), .B2(n185), .A(n183), .ZN(n171) );
  NOR2_X1 U15 ( .A1(a[2]), .A2(b[2]), .ZN(n177) );
  NOR2_X1 U16 ( .A1(a[3]), .A2(b[3]), .ZN(n172) );
  NOR2_X1 U17 ( .A1(n177), .A2(n172), .ZN(n3) );
  NAND2_X1 U18 ( .A1(a[2]), .A2(b[2]), .ZN(n178) );
  NAND2_X1 U19 ( .A1(a[3]), .A2(b[3]), .ZN(n173) );
  OAI21_X1 U20 ( .B1(n172), .B2(n178), .A(n173), .ZN(n2) );
  AOI21_X1 U21 ( .B1(n171), .B2(n3), .A(n2), .ZN(n147) );
  NOR2_X1 U22 ( .A1(a[4]), .A2(b[4]), .ZN(n160) );
  NOR2_X1 U23 ( .A1(a[5]), .A2(b[5]), .ZN(n162) );
  NOR2_X1 U24 ( .A1(n160), .A2(n162), .ZN(n149) );
  NOR2_X1 U25 ( .A1(a[6]), .A2(b[6]), .ZN(n155) );
  NOR2_X1 U26 ( .A1(a[7]), .A2(b[7]), .ZN(n150) );
  NOR2_X1 U27 ( .A1(n155), .A2(n150), .ZN(n5) );
  NAND2_X1 U28 ( .A1(n149), .A2(n5), .ZN(n7) );
  NAND2_X1 U29 ( .A1(a[4]), .A2(b[4]), .ZN(n167) );
  NAND2_X1 U30 ( .A1(a[5]), .A2(b[5]), .ZN(n163) );
  OAI21_X1 U31 ( .B1(n162), .B2(n167), .A(n163), .ZN(n148) );
  NAND2_X1 U32 ( .A1(a[6]), .A2(b[6]), .ZN(n156) );
  NAND2_X1 U33 ( .A1(a[7]), .A2(b[7]), .ZN(n151) );
  OAI21_X1 U34 ( .B1(n150), .B2(n156), .A(n151), .ZN(n4) );
  AOI21_X1 U35 ( .B1(n148), .B2(n5), .A(n4), .ZN(n6) );
  OAI21_X1 U36 ( .B1(n147), .B2(n7), .A(n6), .ZN(n92) );
  FA_X1 \intadd_1/U4  ( .A(a[8]), .B(b[8]), .CI(n190), .CO(\intadd_1/n3 ), .S(
        d[8]) );
  FA_X1 \intadd_1/U3  ( .A(a[9]), .B(b[9]), .CI(\intadd_1/n3 ), .CO(
        \intadd_1/n2 ), .S(d[9]) );
  FA_X1 \intadd_1/U2  ( .A(b[10]), .B(a[10]), .CI(\intadd_1/n2 ), .CO(
        \intadd_1/n1 ), .S(d[10]) );
  AND2_X1 U11 ( .A1(n1), .A2(n185), .ZN(d[0]) );
  OR2_X1 U9 ( .A1(a[0]), .A2(b[0]), .ZN(n1) );
  OR2_X1 U3 ( .A1(a[12]), .A2(b[12]), .ZN(n28) );
  AND2_X1 U7 ( .A1(b[14]), .A2(a[14]), .ZN(n39) );
  OR2_X1 U8 ( .A1(b[14]), .A2(a[14]), .ZN(n34) );
  OR2_X1 U39 ( .A1(b[23]), .A2(a[23]), .ZN(n103) );
  NAND2_X1 U40 ( .A1(a[11]), .A2(b[11]), .ZN(n11) );
  NAND2_X1 U41 ( .A1(n29), .A2(n11), .ZN(n8) );
  XNOR2_X1 U42 ( .A(\intadd_1/n1 ), .B(n8), .ZN(d[11]) );
  OAI22_X1 U43 ( .A1(a[9]), .A2(b[9]), .B1(a[10]), .B2(b[10]), .ZN(n13) );
  NOR2_X1 U44 ( .A1(b[8]), .A2(a[8]), .ZN(n9) );
  NOR2_X1 U45 ( .A1(n13), .A2(n9), .ZN(n27) );
  AOI22_X1 U46 ( .A1(b[8]), .A2(a[8]), .B1(a[9]), .B2(b[9]), .ZN(n12) );
  NAND2_X1 U47 ( .A1(a[10]), .A2(b[10]), .ZN(n10) );
  OAI211_X1 U48 ( .C1(n13), .C2(n12), .A(n11), .B(n10), .ZN(n26) );
  AOI21_X1 U49 ( .B1(n190), .B2(n27), .A(n26), .ZN(n15) );
  NOR2_X1 U51 ( .A1(n15), .A2(n14), .ZN(n18) );
  XNOR2_X1 U52 ( .A(a[12]), .B(b[12]), .ZN(n16) );
  XNOR2_X1 U53 ( .A(n18), .B(n16), .ZN(d[12]) );
  NAND2_X1 U54 ( .A1(a[12]), .A2(b[12]), .ZN(n31) );
  INV_X1 U55 ( .A(n31), .ZN(n17) );
  AOI21_X1 U56 ( .B1(n18), .B2(n28), .A(n17), .ZN(n21) );
  NAND2_X1 U57 ( .A1(a[13]), .A2(b[13]), .ZN(n30) );
  INV_X1 U58 ( .A(n30), .ZN(n19) );
  NOR2_X1 U59 ( .A1(a[13]), .A2(b[13]), .ZN(n36) );
  NOR2_X1 U60 ( .A1(n19), .A2(n36), .ZN(n20) );
  XNOR2_X1 U61 ( .A(n21), .B(n20), .ZN(d[13]) );
  AOI21_X1 U62 ( .B1(n21), .B2(n30), .A(n36), .ZN(n23) );
  XNOR2_X1 U63 ( .A(b[14]), .B(a[14]), .ZN(n22) );
  XNOR2_X1 U64 ( .A(n23), .B(n22), .ZN(d[14]) );
  AOI21_X1 U65 ( .B1(n23), .B2(n34), .A(n39), .ZN(n25) );
  XOR2_X1 U66 ( .A(b[15]), .B(a[15]), .Z(n24) );
  XNOR2_X1 U67 ( .A(n25), .B(n24), .ZN(d[15]) );
  AOI21_X1 U68 ( .B1(n92), .B2(n27), .A(n26), .ZN(n33) );
  NAND2_X1 U69 ( .A1(n29), .A2(n28), .ZN(n32) );
  OAI211_X1 U70 ( .C1(n33), .C2(n32), .A(n31), .B(n30), .ZN(n35) );
  NAND2_X1 U71 ( .A1(n35), .A2(n34), .ZN(n101) );
  NOR2_X1 U73 ( .A1(n37), .A2(n36), .ZN(n80) );
  INV_X1 U74 ( .A(n80), .ZN(n38) );
  NOR2_X1 U75 ( .A1(n101), .A2(n38), .ZN(n48) );
  INV_X1 U76 ( .A(n48), .ZN(n41) );
  NAND2_X1 U77 ( .A1(n40), .A2(n39), .ZN(n47) );
  NAND2_X1 U78 ( .A1(b[15]), .A2(a[15]), .ZN(n46) );
  AND3_X1 U79 ( .A1(n41), .A2(n47), .A3(n46), .ZN(n43) );
  XOR2_X1 U80 ( .A(a[16]), .B(b[16]), .Z(n42) );
  XNOR2_X1 U81 ( .A(n43), .B(n42), .ZN(d[16]) );
  NOR2_X1 U82 ( .A1(a[16]), .A2(b[16]), .ZN(n50) );
  NAND2_X1 U83 ( .A1(a[16]), .A2(b[16]), .ZN(n56) );
  OAI21_X1 U84 ( .B1(n43), .B2(n50), .A(n56), .ZN(n45) );
  XNOR2_X1 U85 ( .A(a[17]), .B(b[17]), .ZN(n44) );
  XNOR2_X1 U86 ( .A(n45), .B(n44), .ZN(d[17]) );
  NAND2_X1 U87 ( .A1(a[17]), .A2(b[17]), .ZN(n49) );
  NAND3_X1 U88 ( .A1(n47), .A2(n49), .A3(n46), .ZN(n97) );
  AOI21_X1 U92 ( .B1(n53), .B2(n56), .A(n60), .ZN(n55) );
  XNOR2_X1 U93 ( .A(b[18]), .B(a[18]), .ZN(n54) );
  XNOR2_X1 U94 ( .A(n55), .B(n54), .ZN(d[18]) );
  NAND2_X1 U95 ( .A1(b[18]), .A2(a[18]), .ZN(n59) );
  NAND2_X1 U96 ( .A1(n59), .A2(n56), .ZN(n81) );
  INV_X1 U97 ( .A(b[18]), .ZN(n58) );
  INV_X1 U98 ( .A(a[18]), .ZN(n57) );
  AOI22_X1 U99 ( .A1(n60), .A2(n59), .B1(n58), .B2(n57), .ZN(n82) );
  OAI21_X1 U100 ( .B1(n61), .B2(n81), .A(n82), .ZN(n64) );
  XOR2_X1 U101 ( .A(b[19]), .B(a[19]), .Z(n62) );
  XNOR2_X1 U102 ( .A(n64), .B(n62), .ZN(d[19]) );
  NOR2_X1 U104 ( .A1(b[19]), .A2(a[19]), .ZN(n77) );
  AOI21_X1 U105 ( .B1(n64), .B2(n63), .A(n77), .ZN(n73) );
  XNOR2_X1 U106 ( .A(b[20]), .B(a[20]), .ZN(n65) );
  XNOR2_X1 U107 ( .A(n73), .B(n65), .ZN(d[20]) );
  INV_X1 U108 ( .A(n73), .ZN(n66) );
  NOR2_X1 U109 ( .A1(b[20]), .A2(a[20]), .ZN(n69) );
  NAND2_X1 U110 ( .A1(b[20]), .A2(a[20]), .ZN(n71) );
  OAI21_X1 U111 ( .B1(n66), .B2(n69), .A(n71), .ZN(n68) );
  NOR2_X1 U112 ( .A1(a[21]), .A2(b[21]), .ZN(n85) );
  INV_X1 U113 ( .A(n85), .ZN(n72) );
  NAND2_X1 U114 ( .A1(a[21]), .A2(b[21]), .ZN(n70) );
  NAND2_X1 U115 ( .A1(n72), .A2(n70), .ZN(n67) );
  XNOR2_X1 U116 ( .A(n68), .B(n67), .ZN(d[21]) );
  NOR2_X1 U117 ( .A1(n85), .A2(n69), .ZN(n76) );
  NAND2_X1 U118 ( .A1(n71), .A2(n70), .ZN(n88) );
  AOI22_X1 U119 ( .A1(n73), .A2(n76), .B1(n72), .B2(n88), .ZN(n75) );
  XOR2_X1 U120 ( .A(b[22]), .B(a[22]), .Z(n74) );
  XNOR2_X1 U121 ( .A(n75), .B(n74), .ZN(d[22]) );
  NAND2_X1 U122 ( .A1(n76), .A2(n84), .ZN(n89) );
  NOR2_X1 U123 ( .A1(n89), .A2(n77), .ZN(n83) );
  NAND2_X1 U127 ( .A1(n98), .A2(n80), .ZN(n100) );
  NAND3_X1 U128 ( .A1(n83), .A2(n82), .A3(n81), .ZN(n95) );
  NOR2_X1 U130 ( .A1(n86), .A2(n85), .ZN(n87) );
  AOI22_X1 U131 ( .A1(n88), .A2(n87), .B1(b[22]), .B2(a[22]), .ZN(n94) );
  INV_X1 U132 ( .A(n89), .ZN(n91) );
  NAND2_X1 U133 ( .A1(n91), .A2(n90), .ZN(n93) );
  NAND3_X1 U134 ( .A1(n95), .A2(n94), .A3(n93), .ZN(n96) );
  AOI21_X1 U135 ( .B1(n98), .B2(n97), .A(n96), .ZN(n99) );
  OAI21_X1 U136 ( .B1(n101), .B2(n100), .A(n99), .ZN(n104) );
  XNOR2_X1 U137 ( .A(b[23]), .B(a[23]), .ZN(n102) );
  XNOR2_X1 U138 ( .A(n104), .B(n102), .ZN(d[23]) );
  AOI22_X1 U139 ( .A1(n104), .A2(n103), .B1(a[23]), .B2(b[23]), .ZN(n117) );
  XOR2_X1 U140 ( .A(a[24]), .B(b[24]), .Z(n105) );
  XNOR2_X1 U141 ( .A(n117), .B(n105), .ZN(d[24]) );
  NAND2_X1 U143 ( .A1(a[24]), .A2(b[24]), .ZN(n115) );
  OAI21_X1 U144 ( .B1(n117), .B2(n106), .A(n115), .ZN(n109) );
  XNOR2_X1 U145 ( .A(a[25]), .B(b[25]), .ZN(n107) );
  XNOR2_X1 U146 ( .A(n109), .B(n107), .ZN(d[25]) );
  NAND2_X1 U147 ( .A1(a[25]), .A2(b[25]), .ZN(n116) );
  INV_X1 U148 ( .A(n116), .ZN(n119) );
  NOR2_X1 U149 ( .A1(a[25]), .A2(b[25]), .ZN(n121) );
  INV_X1 U151 ( .A(n121), .ZN(n108) );
  OAI21_X1 U152 ( .B1(n109), .B2(n119), .A(n108), .ZN(n112) );
  NAND2_X1 U153 ( .A1(b[26]), .A2(a[26]), .ZN(n126) );
  INV_X1 U154 ( .A(n126), .ZN(n110) );
  NOR2_X1 U155 ( .A1(b[26]), .A2(a[26]), .ZN(n120) );
  NOR2_X1 U156 ( .A1(n110), .A2(n120), .ZN(n111) );
  XNOR2_X1 U157 ( .A(n112), .B(n111), .ZN(d[26]) );
  OAI21_X1 U158 ( .B1(n112), .B2(n120), .A(n126), .ZN(n114) );
  XNOR2_X1 U159 ( .A(b[27]), .B(a[27]), .ZN(n113) );
  XNOR2_X1 U160 ( .A(n114), .B(n113), .ZN(d[27]) );
  NAND3_X1 U161 ( .A1(n117), .A2(n116), .A3(n115), .ZN(n124) );
  NOR2_X1 U162 ( .A1(n119), .A2(n118), .ZN(n122) );
  NOR2_X1 U163 ( .A1(b[27]), .A2(a[27]), .ZN(n127) );
  NOR4_X1 U164 ( .A1(n122), .A2(n127), .A3(n121), .A4(n120), .ZN(n123) );
  NAND2_X1 U165 ( .A1(n124), .A2(n123), .ZN(n143) );
  INV_X1 U166 ( .A(n143), .ZN(n128) );
  NAND2_X1 U167 ( .A1(b[27]), .A2(a[27]), .ZN(n125) );
  OAI21_X1 U168 ( .B1(n127), .B2(n126), .A(n125), .ZN(n140) );
  NOR2_X1 U169 ( .A1(n128), .A2(n140), .ZN(n131) );
  NAND2_X1 U170 ( .A1(b[28]), .A2(a[28]), .ZN(n136) );
  INV_X1 U171 ( .A(n136), .ZN(n129) );
  NOR2_X1 U172 ( .A1(b[28]), .A2(a[28]), .ZN(n134) );
  NOR2_X1 U174 ( .A1(n129), .A2(n134), .ZN(n130) );
  XNOR2_X1 U175 ( .A(n131), .B(n130), .ZN(d[28]) );
  OAI21_X1 U176 ( .B1(n131), .B2(n134), .A(n136), .ZN(n133) );
  XNOR2_X1 U177 ( .A(b[29]), .B(a[29]), .ZN(n132) );
  XNOR2_X1 U178 ( .A(n133), .B(n132), .ZN(d[29]) );
  NOR2_X1 U179 ( .A1(b[29]), .A2(a[29]), .ZN(n137) );
  NOR2_X1 U180 ( .A1(n137), .A2(n134), .ZN(n139) );
  INV_X1 U181 ( .A(n139), .ZN(n142) );
  NAND2_X1 U182 ( .A1(b[29]), .A2(a[29]), .ZN(n135) );
  OAI21_X1 U183 ( .B1(n137), .B2(n136), .A(n135), .ZN(n138) );
  AOI21_X1 U184 ( .B1(n140), .B2(n139), .A(n138), .ZN(n141) );
  OAI21_X1 U185 ( .B1(n143), .B2(n142), .A(n141), .ZN(n145) );
  XNOR2_X1 U186 ( .A(a[30]), .B(b[30]), .ZN(n144) );
  XNOR2_X1 U187 ( .A(n145), .B(n144), .ZN(d[30]) );
  FA_X1 U188 ( .A(a[30]), .B(b[30]), .CI(n145), .CO(n188), .S() );
  XNOR2_X1 U189 ( .A(b[31]), .B(a[31]), .ZN(n187) );
  XNOR2_X1 U218 ( .A(n188), .B(n187), .ZN(d[31]) );
  INV_X1 U1 ( .A(n53), .ZN(n61) );
  NOR2_X1 U2 ( .A1(n97), .A2(n48), .ZN(n53) );
  INV_X1 U4 ( .A(n106), .ZN(n118) );
  NOR2_X1 U5 ( .A1(b[24]), .A2(a[24]), .ZN(n106) );
  INV_X1 U6 ( .A(n63), .ZN(n90) );
  NAND2_X1 U37 ( .A1(a[19]), .A2(b[19]), .ZN(n63) );
  INV_X1 U38 ( .A(n14), .ZN(n29) );
  NOR2_X1 U50 ( .A1(b[11]), .A2(a[11]), .ZN(n14) );
  AND2_X2 U72 ( .A1(n83), .A2(n82), .ZN(n98) );
  INV_X1 U89 ( .A(n37), .ZN(n40) );
  NOR2_X1 U90 ( .A1(a[15]), .A2(b[15]), .ZN(n37) );
  INV_X1 U91 ( .A(n86), .ZN(n84) );
  NOR2_X1 U103 ( .A1(a[22]), .A2(b[22]), .ZN(n86) );
  OAI21_X1 U124 ( .B1(b[17]), .B2(a[17]), .A(n191), .ZN(n60) );
  NAND2_X1 U125 ( .A1(n49), .A2(n50), .ZN(n191) );
endmodule



    module conf_int_add__noFF__arch_agnos__w_wrapper_OP_BITWIDTH32_DATA_PATH_BITWIDTH32 ( 
        clk, rst, a, b, d );
  input [31:0] a;
  input [31:0] b;
  output [31:0] d;
  input clk, rst;
  wire   n1;

  LOGIC0_X1 U2 ( .Z(n1) );
  conf_int_add__noFF__arch_agnos_OP_BITWIDTH32_DATA_PATH_BITWIDTH32 add ( 
        .clk(clk), .rst(n1), .a(a), .b(b), .d(d) );
endmodule

