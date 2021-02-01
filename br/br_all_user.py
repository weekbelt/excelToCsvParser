def getProcessedPhoneNumber(phone_number):
    phone_number = str(phone_number)

    if phone_number == 'nan':
        return ""
    else:
        if "930" in phone_number:
            return "내선"
        else:
            return "외부국선"


def checkPhoneType(phone_number):
    phone_number = str(phone_number)

    if phone_number == 'nan':
        return ""
    else:
        # TODO: Detail
        if "930" in phone_number:
            return "내선"
        else:
            return "외부국선"


def createPhoneTypeColumn(allUserData):
    allUserData["phone_type"] = allUserData["회사전화"].apply(checkPhoneType)


def processAllUserData(allUserData):
    # 필요 없는 Column 제거
    allUserData = allUserData.drop(["테넌트", "휴대전화", "사진", "순서",
                                    "이메일주소", "정규", "기타", "상태", "SADN1", "SADN2", "SADN3",
                                    "SADN4"], axis=1)
    allUserData = allUserData.dropna(how='all', axis=1)
    # phoneType 컬럼 추가
    createPhoneTypeColumn(allUserData)
    # phoneNumber 전처리


    return allUserData