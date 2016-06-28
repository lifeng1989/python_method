#! /usr/bin/awk -f
BEGIN{		
	while(getline <"solid"){
		a[$1] = $0	
	}
	while (getline < "rfree"){
		if(a[$1])
			a[$1] = a[$1]"\t"$2
	}
	while (getline < "lfree"){
		if(a[$1])
			a[$1] = a[$1]"\t"$2		
	}
}
{
		
}
END{
	for(id in a)
			print a[id]
		}
