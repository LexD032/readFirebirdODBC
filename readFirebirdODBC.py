import pyodbc as db
server   = 'Server2019/3052'      # 'port:server.base.sql'
bddata   = 'D:\IADb\IAPTEKA.FDB'  # 'mybd' 
user     = 'SYSDBA'
password = 'masterkey'

str_dt1 = input("Начальная дата:") 
str_dt2 = input("Конечная  дата:") 

conn = db.connect(r"Dsn=IA3; Driver={Firebird/InterBase(r) driver}; \
                  client=C:\Program Files\Firebird3x64\fbclient.dll")

cursor = conn.cursor()
sql = r"select dp.dep_id, d.user_id, m.med_id, -sum(di.qtty) as klv_sale,-sum(di.ssum) as sum_sale from docitem di, docs d, items i,medicine m, department dp where d.doc_id = di.doc_id  and i.iid = di.iid and d.doctype = 40 and d.subtype = 40  and i.med_id = m.med_id and d.dep_id = dp.dep_id and (d.docdate >='"+str_dt1+"' and d.docdate <='"+str_dt2+"')  group by   dp.dep_id,d.user_id,m.med_id"

cursor.execute(sql)
x = open(r"d:\\test.txt","w")

row = cursor.fetchone()
while row:
    if row:
        x.write(""+str(row[0])+';'+str(row[1])+';'+str(row[2])+';'+str(row[3])+';'+str(row[4])+"\n")
    row = cursor.fetchone()
print(" вывела!")
x.close()