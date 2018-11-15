 #!/bin/bash 
counter=1 
olddir="A" 
for f in */*; do fp=$(dirname "$f");
    ext="${f##*.}" ;
    if [ "$fp" !=  "$olddir" ];
    then
        let counter=1;
    fi
    mv "$f" "$fp"/"$fp$counter"."$ext";
    let counter++;
    olddir="$fp"
done                            