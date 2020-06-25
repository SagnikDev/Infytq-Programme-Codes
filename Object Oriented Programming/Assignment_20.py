class Application:
    __application_dict={}
    __application_id_count=1000
    def __init__(self,name):
       self.__application_id=None
       self.__application_name=name
       self.__job_band=None

    @staticmethod
    def get_application_dict():
        return Application.__application_dict
    def get_application_id(self):
        return self.__application_id
    def get_application_name(self):
        return self.__application_name
    def get_job_band(self):
        return self.__job_band
    def generate_application_id(self):
        Application.__application_id_count+=1
        self.__application_id=Application.__application_id_count
    def apply_for_job(self,job_band):
        if job_band in Application.__application_dict:
            if(Application.__application_dict[job_band]==5):
                print("Error: Job for this Id Full")
                return -1
            else:
                Application.__application_dict[job_band]+=1
                self.generate_application_id()
                self.__job_band=job_band
                print("Application Id: {} , Name: {} , Job Band: {}".format(self.get_application_id(),self.get_application_name(),self.get_job_band()))
        else:
            Application.__application_dict[job_band]=1
            self.generate_application_id()
            self.__job_band=job_band
            print("Application Id: {} , Name: {} , Job Band: {}".format(self.get_application_id(),self.get_application_name(),self.get_job_band()))

appl1=Application("Sagnik")
appl1.apply_for_job(102)

appl2=Application("Sagnik")
appl2.apply_for_job(102)


appl3=Application("Sagnik")
appl3.apply_for_job(102)


appl4=Application("Sagnik")
appl4.apply_for_job(102)


appl5=Application("Sagnik")
appl5.apply_for_job(102)

appl6=Application("Sagnik")
appl6.apply_for_job(102)

