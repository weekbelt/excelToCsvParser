def removeColumn(ddf):
    df = ddf.drop(["테넌트", "상태", "순서"], axis=1)
    return df


def conditionFunc(departmentName):
    if departmentName[-1:] == '면':
        return departmentName + "사무소"
    elif departmentName[-1:] == '동':
        return departmentName + "주민센터"
    elif departmentName[-1:] == '읍':
        return departmentName + "사무소"
    elif departmentName == '시장':
        return departmentName + "실"
    else:
        return departmentName


def renameDepartmentName(ddf):
    ddf["이름"] = ddf["이름"].apply(conditionFunc)
    return ddf


def processDepartmentDataFrame(ddf):
    # Department Name 조건에 따른 수정
    ddf = renameDepartmentName(ddf)
    # 필요 없는 컬럼 지우기
    ddf = removeColumn(ddf)
    return ddf