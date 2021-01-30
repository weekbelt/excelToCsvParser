def removeColumn(sdf):
    sdf = sdf.drop(["테넌트", "아이디", "휴대전화", "사진", "순서",
                    "이메일주소", "정규", "기타", "상태", "SADN2", "SADN3",
                    "SADN4"], axis=1)
    return sdf


def processDepartmentDataFrame(sdf):
    sdf = sdf.dropna(how='all', axis=1)
    return sdf
