#grep CLUE crimescene | tee clues.txt
cd memberships
cat AAA Delta_SkyMiles Museum_of_Bash_History Terminal_City_Library | sort | uniq -c | grep 4 | cut -c 9- > ../suspects.txt
cd ..
while read p; do
  if grep "$p" -A1 vehicles | tail -1 | grep -q "Height: 6"; then
    if [ `grep "$p" people | cut -f 2` == "M" ]; then
      echo "---------------------------------"
      grep "$p" people
      FILENAME=`grep "$p" people | cut -f 4 | awk -F',' '{print $1}' | sed -e 's/ /_/g'`
      LINENUM=`grep "$p" people | awk -F'line ' '{print $2}'`
      INTNUM=`head -n $LINENUM streets/$FILENAME | tail -1 | awk -F'#' '{print $2}'`
      cat interviews/interview-$INTNUM
      echo "---------------------------------"
    fi 
  fi
done <suspects.txt
