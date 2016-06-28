#! /usr/bin/awk -f
BEGIN{
	while (getline < "fuhao.txt"){
			for(i = 1 ; i <= NF ; i++)
				 a[$i] = 1
		}
}
{
		for(i = 1 ; i <= length($0); i++){
				b = substr($0,i,1)
				if( a[b] != 1 )
					printf b; 
		}
		print ""
}
