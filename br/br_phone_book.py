
def getDetailCompanyName(companyName):
    companyName = str(companyName)
    if companyName == "시장" or companyName == "비서실장" or companyName == "수행비서" or companyName == "민원보좌관":
        return "시장실"
    elif companyName == "농업기술센터소장":
        return companyName[:-2]
    elif companyName[-2:] == "소장":
        return companyName[:-1]
    elif companyName == "보건소장실":
        return "보건소"
    elif companyName == "농업기술센터소장실":
        return "농업기술센터"
    elif companyName[-2:] == "팀장":
        return companyName[:-1]
    elif companyName[-2:] == "과장":
        return companyName[:-1]
    elif companyName[-2:] == "단장":
        return companyName[:-1]
    elif companyName[-3:] == "본부장":
        return companyName[:-1]
    elif companyName[-2:] == "부장":
        return companyName[:-1]
    elif companyName[-2:] == "실장":
        return companyName[:-1]
    elif companyName[-2:] == "국장":
        return companyName[:-1]
    elif companyName == "공중보건의사":
        return "진료팀"
    elif companyName[-2:] == "읍장" or companyName[-2:] == "면장":
        return companyName[:-1] + "사무소"
    elif companyName[-2:] == "동장":
        return companyName[:-1] + "주민센터"
    else:
        return companyName


def renameLastName(lastName):
    lastName = str(lastName)
    if lastName[-2:] == "팀장":
        return lastName[:-2]
    elif lastName[-2:] == "공익":
        return lastName[:-3]
    else:
        return lastName


def processPhoneBookDateFrame(sdf):
    # 필요없는 행 제거
    sdf = sdf.iloc[:2610]
    # 필요없는 컬럼 제거
    sdf = sdf.dropna(how='all', axis=1)
    # 공백인 행 제거
    sdf = sdf.dropna(how='all', axis=0)
    sdf = sdf.drop(["FIRSTNAME", "MOBILEPHONE", "PHONE_LEVEL", "COMPANYPHONE",
                    "ADDRESS1", "ADDRESS3", "CITY", "ZIP", "HOUSEPHONE.1",
                    "ACCOUNTNO", "JOB", "FAX"], axis=1)

    # 특정 column을 기준으로 중복 행 제거 (첫번째 행을 남김)
    sdf = sdf.drop_duplicates(["LASTNAME", "COMPANY", "HOUSEPHONE"], keep='first')

    # HOUSEPHONE column이 fax라면 LASTNAME column을 '팩스'로 설정
    sdf.loc[sdf["HOUSEPHONE"] == "FAX", 'LASTNAME'] = "팩스"
    sdf.loc[sdf["LASTNAME"] == "fax", 'LASTNAME'] = "팩스"
    sdf.loc[sdf["LASTNAME"] == "FAX", 'LASTNAME'] = "팩스"
    sdf.loc[sdf["LASTNAME"] == "FXA", 'LASTNAME'] = "팩스"

    # LASTNAME에 '팀장'이 들어간 문자열 지우기
    sdf["LASTNAME"] = sdf["LASTNAME"].apply(renameLastName)

    # DETAIL_COMPANY 컬럼 추가
    sdf["DETAIL_COMPANY"] = sdf["HOUSEPHONE"].apply(getDetailCompanyName)

    # sdf['LASTNAME'].dropna(axis=0, how='any')

    # # HOUSEPHONE 컬럼이 '선장'인 값 개별로 처리
    # captain1 = sdf[sdf["LASTNAME"] == "조영일"]
    # captain1.iloc[0]["DETAIL_COMPANY"] = "섬자원개발팀"
    # # sdf[sdf["LASTNAME"] == "조영일"].iloc[0]["HOUSEPHONE"] = "섬자원개발팀"
    # # captain1.iloc[0]["HOUSEPHONE"] = "섬자원개발팀"
    #
    # captain2 = sdf[sdf["LASTNAME"] == "원유천"]
    # captain2.iloc[0]["DETAIL_COMPANY"] = "어업지원팀"
    # # sdf[sdf["LASTNAME"] == "원유천"].iloc[0]["HOUSEPHONE"] = "어업지원팀"
    # # captain2.iloc[0]["HOUSEPHONE"] = "어업지원팀"
    #
    # captain3 = sdf[sdf["LASTNAME"] == "이창섭"]
    # captain3.iloc[0]["DETAIL_COMPANY"] = "총무팀"
    # # sdf[sdf["LASTNAME"] == "이창섭"].iloc[0]["HOUSEPHONE"] = "총무팀"
    # # captain3.iloc[0]["HOUSEPHONE"] = "총무팀"

    # 결측치 행 처리
    return sdf