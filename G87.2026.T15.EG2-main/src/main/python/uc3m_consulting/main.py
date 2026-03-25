import enterprise_project

# Assuming request date of 16/01/2023 as set in enterprise_project
def show_md5():
    obj = enterprise_project.EnterpriseProject('A58818501','PROJ01','TreasureHunters2','HR','21/05/2026',1000000.00)
    print(obj.project_id)

if __name__ == '__main__':
    show_md5()