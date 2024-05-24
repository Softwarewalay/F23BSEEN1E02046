class university:
    __name=input('What is the name of your university?\n')
    __establish=input('In which year, your university was established?\n')
    __location=input('Where is your university is located?\n')
    def uni_info(self):
        print('ISLAMIA UNIVERSITY BAHAWALPUR \n My university name is ',self.__name,'it is one of the largest university in Pakistan.It was established in ',self.__establish,'in the city of Nawabs',self.__location,'in pakistan')

    # def main_campus(self):
    #     maincampus_location=input('Where the maincampus of your university is located?:n')
class campuses(university):
    __m_campus=input('write the name of your main campus?:\n')    
    __m_location=input('write the exact location where your main campus is located?:\n')
    def main_campus(self):
        print('ABBASIA CAMPUS: \n there are five campuses of our university which are situated in different cities but the main campus',self.__m_campus,'is located in ',self.__m_location,'.')
    def sub_campus1(self):
        print('BAGHDAD-UL-JADEED CAMPUS:\n It is the sub_campus of our university,which is situated',self.sub_campus1,)

a1=campuses()
a1.uni_info()
a1.main_campus()
a1.sub_campus1()