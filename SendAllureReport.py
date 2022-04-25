import base64
import json
import logging
import os
from datetime import date
from pathlib import Path

import env
from Helpers.CreateEnvForAllureReportHelper import createEnvForAllureReportHelper
from Helpers.RequestConnectorHelper import connector

""" Directory witch allure report result test """
DIR_ALLURE_REPORTS = os.path.abspath('allure_reports')

""" URLs allure API """
ALLURE_DOCKER_SERVICE_URL = '/allure-docker-service'
SEND_RESULT_URL = '/send-results'
GENERATE_REPORT_URL = '/generate-report'
PROJECT_URL = '/projects'
PROJECT_UI_URL = '/allure-docker-service-ui/projects/'


def buildContentBase64():
    """ Build results in content_base64

    :return: bool
    """
    jsonData = {
        'results': []
    }

    try:
        files = os.listdir(DIR_ALLURE_REPORTS)
    except Exception as e:
        logging.error(f'ERROR-buildContentBase64: No folder allure_result \n{e}')

        return False

    for fileName in files:
        try:
            with open(Path(f'{DIR_ALLURE_REPORTS}/{fileName}'), "rb") as file:
                base64String = base64.b64encode(file.read()).decode("utf-8")
                jsonData['results'].append({
                    "file_name": fileName,
                    "content_base64": base64String
                })
        except Exception as e:
            logging.error(f'ERROR-buildContentBase64: Error opening files: {files} \n{e}')

            break

    if jsonData['results'] == []:
        logging.warning('WARNING-buildContentBase64: results is empty')

        return False

    return jsonData


def sendResults(nameProject):
    """ Send result and create project.

    :param nameProject: name project Allure-Report
    :return: bool
    """
    jsonData = buildContentBase64()

    if not jsonData:
        return jsonData

    response = connector(
            method = 'post',
            url = f'{ALLURE_DOCKER_SERVICE_URL}{SEND_RESULT_URL}?project_id={nameProject}&force_project_creation=true',
            jsonData = jsonData
    )

    if not response:
        return False

    generateResult = generateReport(nameProject)

    if generateResult:
        print(f'{env.ALLURE_REPORT_UI_URL}{PROJECT_UI_URL}{nameProject}')

    return True


def generateReport(nameProject):
    """ Generate allure report.

    :param nameProject: name project Allure-Report
    :return: bool
    """
    response = connector(
            method = 'get',
            url = f'{ALLURE_DOCKER_SERVICE_URL}{GENERATE_REPORT_URL}?project_id={nameProject}'
    )

    if response:
        return True

    return False


def deleteProject(nameProject):
    """ Delete allure project.

    :param nameProject: name project Allure-Report
    :return: bool
    """
    response = connector(method = 'delete', url = f'{PROJECT_URL}/{nameProject}')

    if response:
        return True

    return False


def getProject():
    """ Get count and name project allure-report

    :return: bool|str
    """
    response = connector(method = 'get', url = f'{ALLURE_DOCKER_SERVICE_URL}{PROJECT_URL}')
    result = {
        'count_project': 0,
        'name_projects': []
    }

    if not response:
        return False

    responseJson = json.loads(response.text)['data']['projects']
    result['count_project'] = len(responseJson)

    for i in responseJson:
        result['name_projects'].append(i)

    return result


if __name__ == '__main__':
    createEnvForAllureReportHelper()
    projectData = getProject()
    nameProject = f'{date.today()}--{projectData["count_project"]}'

    if projectData["count_project"] >= env.COUNT_SAVE_REPORTS:
        print('Allure-report clear')
        nameProject = f'{date.today()}--1'

        for i in projectData['name_projects']:
            deleteProject(i)

    sendResults(nameProject = nameProject)
