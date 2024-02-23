
import os

os.chdir('/Users/ayaanleahassan/Documents/ZEALAND/Second_Semester/IoT/Labs')

for f in os.listdir():
   f_name ,f_ext = os.path.splitext(f)

   print(f_name.split('_'))
   #print(f_name)


   #z_name, w_name, title, number, k , i = f_name.split('_')

 #  print(z_name)

