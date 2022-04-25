import allure
import pytest

import env
from Entities.TimeoutEntities import TIMEOUT
from browserSettings.BuildConfig import configDesktop

""" Build config for desktop testing """
configDesktop()

""" Service list xpath """
SERVICE_LIST_XPATH = '//*[@class="service__list"]'

""" Adata-api xpath """
ADATA_API_XPATH = '//*[@class="adata-api"]'

""" Service xpath """
SERVICE_XPATH = '//*[@class="service__list service__list-useful"]'

""" Free check xpath """
FREE_CHECK_XPATH = '//*[@class="free-check"]'

""" Mail xpath """
MAIL_XPATH = '//*[@class="mail"]'


class MainPageTest:
    @pytest.mark.smoke
    @allure.suite('Smoke')
    @allure.severity('trivial')
    @allure.title('Главная страница')
    def testMainPage(self, sb):
        """ Main page test

        :param sb: WebDriver
        """
        with allure.step('Открытие главной страницы'):
            sb.maximize_window()
            sb.get(env.MODULE_PK_URL)

        with allure.step('Проверка полей на главной странице'):
            with allure.step('intro__title'):
                sb.assert_text('Избавьтесь от лишних рисков!', timeout = TIMEOUT)
                sb.assert_text('Получите всю информацию о любой')
                sb.assert_text('компании всего за пару кликов')

            with allure.step('intro__subtitle'):
                sb.assert_text('Проверьте контрагента и сэкономьте свой бюджет и время')
                sb.assert_text('на решение проблем с неблагонадежным контрагентом')

            with allure.step('Как работать с сервисом 1'):
                sb.assert_text('Как работать с сервисом', timeout = TIMEOUT)

                with allure.step('service "Основная информация"'):
                    sb.assert_text('1', selector = SERVICE_LIST_XPATH)
                    sb.assert_text('Основная информация', selector = SERVICE_LIST_XPATH)
                    sb.assert_text(
                            'Изучите регистрационные сведения компании. Сколько времени компания на рынке. Кто ее владелец и руководитель.',
                            selector = SERVICE_LIST_XPATH
                    )

                with allure.step('service "Налоговые отчисления"'):
                    sb.assert_text('2', selector = SERVICE_LIST_XPATH)
                    sb.assert_text('Налоговые отчисления', selector = SERVICE_LIST_XPATH)
                    sb.assert_text(
                            'Изучите динамику налоговых отчислений по годам, имеется ли падение или рост оплат. Проверьте по каким КБК поставщик оплачивает налоги.',
                            selector = SERVICE_LIST_XPATH)

                with allure.step('service "Судебные дела"'):
                    sb.assert_text('3', selector = SERVICE_LIST_XPATH)
                    sb.assert_text('Налоговые отчисления', selector = SERVICE_LIST_XPATH)
                    sb.assert_text(
                            'Изучите не проходит ли Ваш поставщик ответчиком по судебным делам.',
                            selector = SERVICE_LIST_XPATH
                    )
                    sb.assert_text(
                            'Проверьте историю судебных дел.',
                            selector = SERVICE_LIST_XPATH
                    )

                with allure.step('service "Участие в закупках"'):
                    sb.assert_text('4', selector = SERVICE_LIST_XPATH)
                    sb.assert_text('Налоговые отчисления', selector = SERVICE_LIST_XPATH)
                    sb.assert_text(
                            'Изучите в каких закупках участвует ваш контрагент, кто его основной поставщик или заказчик. Проверьте на наличие в реестрах недобросовестных поставщиков.',
                            selector = SERVICE_LIST_XPATH
                    )

                with allure.step('service "Задолженность"'):
                    sb.assert_text('5', selector = SERVICE_LIST_XPATH)
                    sb.assert_text('Задолженность', selector = SERVICE_LIST_XPATH)
                    sb.assert_text(
                            'Проверьте поставщика на наличие задолженностей по налогам и исполнительным производствам, арестов на банковские счета или ограничения на выезд из страны.',
                            selector = SERVICE_LIST_XPATH
                    )

                with allure.step('service "Схема связей"'):
                    sb.assert_text('7', selector = SERVICE_LIST_XPATH)
                    sb.assert_text('Схема связей', selector = SERVICE_LIST_XPATH)
                    sb.assert_text(
                            'Проверьте связи по номеру телефона, адресу, по руководителю и владельцам, по общим заказчикам и судебным делам.',
                            selector = SERVICE_LIST_XPATH
                    )

                with allure.step('service "Схема связей"'):
                    sb.assert_text('8', selector = SERVICE_LIST_XPATH)
                    sb.assert_text('Сравнение контрагентов', selector = SERVICE_LIST_XPATH)
                    sb.assert_text(
                            'Изучите всех поставщиков по основным критериям:Какое место занимает на рынке, по сумме оплаченных налогов, признаков благонадежности.',
                            selector = SERVICE_LIST_XPATH
                    )

            with allure.step('Adata.API'):
                sb.assert_text('Adata.API —', selector = ADATA_API_XPATH)
                sb.assert_text('Интегрируйте вашу информационную систему', selector = ADATA_API_XPATH)
                sb.assert_text('с Adata.API и получайте актуальные данные о', selector = ADATA_API_XPATH)
                sb.assert_text('ваших контрагентов автоматически', selector = ADATA_API_XPATH)

            with allure.step('Как работать с сервисом 2'):
                with allure.step('Руководителю'):
                    sb.assert_text('Руководителю', selector = SERVICE_XPATH)
                    sb.assert_text(
                            'Найдите ключевых партнеров и потенциальных поставщиков. Изучите их благонадежность и примите решение о сотрудничестве.',
                            selector = SERVICE_XPATH
                    )

                with allure.step('Отделу закупок'):
                    sb.assert_text('Отделу закупок', selector = SERVICE_XPATH)
                    sb.assert_text(
                            'Оцените надежность поставщиков, изучите заключенные контракты. Проверяйте на наличие в реестрах недобросовестных поставщиков.',
                            selector = SERVICE_XPATH
                    )

                with allure.step('Финансовому отделу'):
                    sb.assert_text('Финансовому отделу', selector = SERVICE_XPATH)
                    sb.assert_text(
                            'Проверьте контрагента на наличие заблокированных счетов. Изучите финансовую устойчивость.',
                            selector = SERVICE_XPATH
                    )

                with allure.step('Отделу кадров'):
                    sb.assert_text('Отделу кадров', selector = SERVICE_XPATH)
                    sb.assert_text(
                            'Проверьте потенциальных сотрудников на благонадежность. Просматривайте резюме, которые выкладывают сотрудники компании. Анализируйте кадры конкурентов.',
                            selector = SERVICE_XPATH
                    )

                with allure.step('Бухгалтерии'):
                    sb.assert_text('Бухгалтерии', selector = SERVICE_XPATH)
                    sb.assert_text(
                            'Проверьте регистрационные и учредительные данные. Получите сведения о руководителе. Определите неплатежеспособных контрагентов.',
                            selector = SERVICE_XPATH
                    )

                with allure.step('Службе безопасности'):
                    sb.assert_text('Службе безопасности', selector = SERVICE_XPATH)
                    sb.assert_text(
                            'Определите аффилированные компании и компании-однодневки. Проверьте участие сотрудников в других компаниях.',
                            selector = SERVICE_XPATH
                    )

            with allure.step('Бесплатные проверки'):
                sb.assert_text('Бесплатные проверки', selector = FREE_CHECK_XPATH)
                sb.assert_text('Зарегистрируйтесь и получите', selector = FREE_CHECK_XPATH)
                sb.assert_text('бесплатные 5 проверки каждый день', selector = FREE_CHECK_XPATH)
                sb.assert_text('Зарегистрироваться', selector = FREE_CHECK_XPATH)

            with allure.step('Интересует больше данных'):
                sb.assert_text('Интересует больше данных?', selector = MAIL_XPATH)
                sb.assert_text(
                        'Оставьте комментарий мы обязательно ответим Вам в кратчайшие сроки',
                        selector = MAIL_XPATH
                )
                sb.assert_text('Отправить', selector = MAIL_XPATH)

            with allure.step('info-quantity__item'):
                sb.assert_text('+ 550 000', timeout = TIMEOUT)
                sb.assert_text('Юридических лиц')
                sb.assert_text('+ 1 000 000')
                sb.assert_text('Индивидуальных предпринимателей')
                sb.assert_text('+ 25')
                sb.assert_text('Источников информации')
                sb.assert_text('+ 92')
                sb.assert_text('Финансовые показатели')

        sb.driver.quit()
