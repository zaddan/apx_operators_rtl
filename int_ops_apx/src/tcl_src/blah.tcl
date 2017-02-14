#--- 

proc make-reg_l {reg_na reg_le} {
    set reg_l {}
    set num_l {}
    for {set a 0} {$a < $reg_le} {incr a} {
        lappend num_l $a
    }
    foreach el $num_l {
        #append concat_res reg_a_reg $el 
        lappend reg_l  "${reg_na}\[${el}\]"
        #reg_a_reg[${el}]
    }
    set reg_l_flattened [join $reg_l]
    return $reg_l_flattened
}



set reg_a_l [make-reg_l "reg_a_reg" 13]
set reg_b_l [make-reg_l "reg_b_reg" 1]
set reg_c_l [make-reg_l "reg_c_reg" 1]
set joined [concat $reg_a_l $reg_b_l]
#puts $reg_a_l
#puts $joined

#--- regular string comparison
foreach el $reg_a_l {
    if {$el=="reg_a_reg\[10\]"} {
        puts "ehlo"
    }
}
puts $reg_a_l
#set a "reg_a_reg\[10\]"
#puts $a
#
#--- finding an element within a list
if {[lsearch -exact $reg_a_l "reg_a_reg\[10\]"] >= 0} {
    puts [lsearch -exact $reg_a_l "reg_a_reg\[10\]"]
}


set name(first) 0
set name(second) 1
set name(third) 0
set name(fourth) 1

puts "starting to print the array content"
puts $name(first)
puts $name(second)
puts $name(third)
puts $name(fourth)


set data [gets stdin]
scan $data "%d %d" myint mystring
puts "here is"
puts $myint
puts $mystring

puts [concat "hello" $mystring]
