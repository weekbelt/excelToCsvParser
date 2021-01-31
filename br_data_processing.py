import pandas as pd
from br import br_staffer, br_department

pd.set_option('display.max_columns', 20)


def main():
    boryeong_branch_id = '0dbf43a0-a168-11e9-a893-49ac915e00a7'

    all_user_data_file_name = 'br/data/allUserData_20210118092328 (1).xls'
    department_data_file_name = 'br/data/stafferName.xlsx'

    sh_br_department = pd.read_excel(io=all_user_data_file_name, sheet_name=0)
    sh_br = pd.read_excel(io=all_user_data_file_name, sheet_name=1, converters={
        '회사전화': str, '조직코드': str, 'SADN1': str})
    sh_match_department_staffer = pd.read_excel(io=department_data_file_name, sheet_name=0, converters={
        'STATION': str})

    # 조직 정보 데이터 전처리
    d_df = br_department.processDepartmentDataFrame(sh_br_department)

    # 전체 사용자 정보 데이터 전처리
    all_user_data_df = br_staffer.processAllUserData(sh_br)

    # 직원 명부 데이터 전처리
    pb_df = br_staffer.processDepartmentDataFrame(sh_match_department_staffer)

    # 전체 사용자 정보와 조직 정보를 left outer로 merge
    d_all_user_merged_df = pd.merge(left=all_user_data_df, right=d_df, how='left', on='조직코드')
    # 중복 컬럼명 변경
    d_all_user_merged_df.rename(columns={'이름_x':'이름', '이름_y':'부서이름'}, inplace=True)

    print(d_all_user_merged_df.head(30))


if __name__ == '__main__':
    main()
