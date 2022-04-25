import allure

""" Accounts array """
ACCOUNT_ARRAY = {

}


def getAccount(nameDef):
    """ Search account for test

    :param nameDef: list
    :return: list
    """
    with allure.step('Получения аккаунта для теста'):
        for i in ACCOUNT_ARRAY:
            if nameDef == i:
                with allure.step(f'Аккаунт: {ACCOUNT_ARRAY[i]}'):
                    return ACCOUNT_ARRAY[i]

        return False
