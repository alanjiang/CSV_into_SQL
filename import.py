
import csv

def gen(tableName, import_csv_file,  out_csv_file):

   fo = open(out_csv_file, "w")
   with open(import_csv_file)as f:
       f_csv = csv.reader(f)
       k = 0
       header_str='insert into {}  ('.format(tableName)
       for row in f_csv:
         
          if ( k == 0) :
              print('头部:{}'.format(row))
              j=0;
              size = len(row)
              for column in row:
                   if (j == size-1):
                      header_str+=column+') values ('
                   else:
                      header_str+=column+','
                   j+=1
             
              
          else:
              
              m=0 
              size = len(row)
              insert_str = ''
              insert_str+=header_str
             
              for value in row:    
                  if (m ==size-1):
                      if  (value == ''):
                           value ='null'
                      else:
                          value ='\''+value+'\''
                      insert_str+=value+');'
                  else:
                       if  (value == ''):
                           value ='null'
                       else:
                          value ='\''+value+'\''
                       insert_str+=value+','
                  m+=1
              fo.write(insert_str+'\n\t')
         
          k+=1
   fo.close() 
 
if __name__ == '__main__':
       
       tableName='t_admin'
       import_csv_file='/Users/pengjiang/source_code/dian-web/记录/PSQL/t_admin_202012031410.csv'
       out_csv_file='/Users/pengjiang/source_code/dian-web/记录/PSQL/t_admin.sql'
       gen(tableName, import_csv_file,  out_csv_file)
       
       