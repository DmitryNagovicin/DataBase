import pandas as pd

print('----'*20)
print('Табель учащихся в средней школе # 1')

stud_card = {
        'ID': ['01','02','03','04','05'],
        'Имя' : ['Иван','Сергей','Марина','Петр','Сидр'],
        'Фамилия': ['Иванов','Сергеев','Маринина','Петров','Сидоров'],
        'Дата рождения' : ['05.05.2005','06.06.2006','07.07.2007','08.08.2005','09.09.2006'],
}
    
sc = pd.DataFrame(data = stud_card)

with open('student.csv', 'a', encoding='UTF-8') as cl:
        cl.write(f'{sc}')
        cl.write('\n')
    
print(sc)