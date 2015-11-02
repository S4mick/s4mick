#!/usr/bin/tclsh

set c [read stdin 1]
set modalita "lololo"
while "1" {
 if { $modalita == "enable" } {
    puts -nonewline "Router#"
    }
    else {
    puts -nonewline "Router>"
      }
    flush stdout
    set name [gets stdin]
    if { $name=="ena" } {
    puts "Could you say it more gently?"
    }
    if { $name=="enable please" } {
    puts "You are welcome!"
    set modalita "enable"
    }

     
