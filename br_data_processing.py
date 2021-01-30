import pandas as pd
import department
import staffer


pd.set_option('display.max_columns', 20)


def main():
    boryeong_branch_id = '0dbf43a0-a168-11e9-a893-49ac915e00a7'

    all_user_data_file_name = 'data/allUserData_20210118092328 (1).xls'
    department_data_file_name = 'data/stafferName.xlsx'

    sh_br_department = pd.read_excel(io=all_user_data_file_name, sheet_name=0)
    sh_br = pd.read_excel(io=all_user_data_file_name, sheet_name=1, converters={
        '회사전화': str, '조직코드': str})
    sh_match_department_staffer = pd.read_excel(io=department_data_file_name, sheet_name=0, converters={
        'STATION': str})

    # 조직 정보 데이터 전처리
    ddf = department.processDepartmentDataFrame(sh_br_department)

    # 전체 사용자 정보 데이터 전처리
    sdf = staffer.removeColumn(sh_br)

    # 직원 명부 데이터 전처리
    stafferList = staffer.processDepartmentDataFrame(sh_match_department_staffer)
    print(stafferList)


if __name__ == '__main__':
    main()
