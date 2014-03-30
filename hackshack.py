##############################################################################
#																			                                       #
# Author:		Anton Tkacz											                             		 #
#																	                                      		 #
# Project:		Hacking the piece of shit, that is Java Shack at Chestnut      #
#				Residence, University of Toronto, Canada. Takes in a space           #
#				seperated DD MM YY and Student Number from as an argument            #
#				and returns the HTML page                                            #
#																			                                       #
# Last Updated:	21:10, 22/10/2013											                       #
#																			                                       #
##############################################################################


from urllib import *
import sys

def meal(dd, mm, yyyy, student):

    dd = str(dd)
    mm = str(mm)
    yyyy = str(yyyy)
    student = str(student)

    # print dd,mm,yyyy,student

    url_req = "http://www.89chestnutlunchbag.info/lunchbag/\
index.php?d={0}&m={1}&y={2}&show=true#input_frm".format(dd, mm, yyyy)


    params = urlencode({'student_num': student, 'search':'Search', \
        'meal': 'Sandwich', 'sides': 'None', 'submit': 'Submit'})
    html_req = urlopen(url_req, params)

    print html_req.read()


meal(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


meal(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
