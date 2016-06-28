#! /usr/bin/awk -f
{
gsub(/[A-Z,a-z]+/,"C",$0)
gsub(/[0-9]+/,"D",$0)
print $0
}
