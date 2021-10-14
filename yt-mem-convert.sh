 
#!/bin/bash

echo "Youtube Member List HTML Parser"

yt_list="$(date --iso-8601)_yt-members.csv"
echo "Name" > $yt_list

# Read HTML from file by line
while read -r line <&9
do
    if [[ "$line" == *"sponsor-info-name"* ]]
    then
        #echo $line | sed -e 's/*sponsor-info-name style-scope ytsp-sponsors-dialog">\(.*\)<\/div*/\1/'
        trim="${line##*'sponsor-info-name style-scope ytsp-sponsors-dialog">'}"
        trim="${trim%%'</div'*}"
        echo $trim >> $yt_list
    fi

done 9< <(cat $1)
