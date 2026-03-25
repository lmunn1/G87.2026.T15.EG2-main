import enterprise_project

# Assuming request date of 16/01/2023 as set in enterprise_project
def show_md5():
    obj = enterprise_project.EnterpriseProject(
        'A58818501',
        'PRO01',
        'ProjectOne',
        'FINANCE',
        '31/12/2027',
        50000.00
    )
    print(obj.project_id)

if __name__ == '__main__':
    show_md5()