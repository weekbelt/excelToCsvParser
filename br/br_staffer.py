def processAllUserData(allUserData):
    allUserData = allUserData.drop(["테넌트", "아이디", "휴대전화", "사진", "순서",
                    "이메일주소", "정규", "기타", "상태", "SADN2", "SADN3",
                    "SADN4"], axis=1)
    return allUserData


# def companyConditionFunc(companyName):
#     if companyName == '보좌관':
#         return "시장실"
#     elif companyName[-2:] == '국장':
#         return companyName[:]
#     elif companyName[-3:] == ''


def processDepartmentDataFrame(sdf):
    sdf = sdf.dropna(how='all', axis=1)
    # sdf["COMPANY"] = sdf["COMPANY"].apply(companyConditionFunc)
    return sdf
