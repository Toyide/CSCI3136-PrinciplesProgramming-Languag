#!/bin/bash

TESTS='bonus*.in'
PROG=runme.sh
count=0
DEBUG=0

if [ "$1" == "debug" ]; then
  let "DEBUG=1"
fi

if [ ! -x $PROG ]; then
  echo Error: $PROG is not in the current directory or is not executable
  exit 1
fi

for T in $TESTS; do
  base=`basename $T .in`
  if [ -f $base.in ]; then  
    echo ===========================================
    echo Test file: $base.in 
    ./$PROG < $base.in > $base.out
    if diff $base.out $base.gold > /dev/null; then
      echo " " PASSED
      let "count = count + 1"
      rm $base.out
    elif [ $DEBUG -eq 1 ]; then
        echo Test $T failed, here are the differences
        echo My program output "                     " Expected program output
        echo ================= "                     " =======================
        diff -W 80 -y $base.out $base.gold | more
        exit 1
    else
      echo " " FAILED
    fi
  else
    echo Oops: file $base.in does not exist!
  fi
done

echo =============================================
echo $count tests passed



