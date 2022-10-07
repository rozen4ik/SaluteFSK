from django.shortcuts import render
import requests
from lessons.data.data_source_info_card import DataSourceInfoCard
from lessons.models import Section
from lessons.services import KonturMessage

# url_info_card = "http://81.200.31.254:33355/spd-xml-api"
# url_passage_card = "http://81.200.31.254:33355/monitor?script=True"
url_info_card = "http://213.208.176.194:55577/spd-xml-api"
url_passage_card = "http://213.208.176.194:55577/monitor?script=True"
kontur_message = KonturMessage


def index(request):
    if request.user.is_authenticated:
        id_tren = request.user.id
        sections = Section.objects.filter(trener=id_tren)
        user_fl = request.user
        data = {
            "user_fl": user_fl,
            "sections": sections
        }
    else:
        data = {}
    return render(request, "lessons/index.html", data)


def info_card(request):
    if request.user.is_authenticated:
        id_tren = request.user.id
        sections = Section.objects.filter(trener=id_tren)
        number_card = request.POST.get("number_card")
        response = requests.post(url=url_info_card, data=kontur_message.message_info_card(number_card))
        message = response.text
        sorted_message = DataSourceInfoCard(message)
        full_name = sorted_message.get_full_name()
        balance = sorted_message.get_balance_card()
        packages = sorted_message.get_list_package()

        data = {
            "number_card": number_card,
            "full_name": full_name,
            "balance": balance,
            "sections": sections,
            "packages": packages,
        }
    else:
        data = {}
    return render(request, "lessons/infocard.html", data)


def passage_card(request):
    number_card = request.POST.get("number_card")
    device_id = request.POST.get("device_id")
    if request.user.is_authenticated:
        id_tren = request.user.id
        sections = Section.objects.filter(trener=id_tren)
        lock_device = requests.post(
            url=url_passage_card,
            data=kontur_message.message_block_device(device_id).encode('windows-1251'),
            headers={'Content-Type': 'application/xml', 'charset': 'windows-1251'}
        )

        passage = requests.post(
            url=url_passage_card,
            data=kontur_message.message_passage_card(device_id, number_card).encode('windows-1251'),
            headers={'Content-Type': 'application/xml', 'charset': 'windows-1251'}
        )

        sorted_message = DataSourceInfoCard(passage.text)
        msg = sorted_message.get_msg()

        solution = msg.partition('<Reason>')[2]
        solution = solution.partition('</Reason>')[0]

        if solution == "Проход разрешен":
            solution = "Занятие списано"
        else:
            solution = "Нет допуска к занятиям"

        repeat_passage = requests.post(
            url=url_passage_card,
            data=msg.encode('windows-1251'),
            headers={'Content-Type': 'application/xml', 'charset': 'windows-1251'}
        )

        unlock_device = requests.post(
            url=url_passage_card,
            data=kontur_message.message_unblock_device(device_id).encode('windows-1251'),
            headers={'Content-Type': 'application/xml', 'charset': 'windows-1251'}
        )

        answer_device = requests.post(
            url=url_passage_card,
            data=kontur_message.answer_device(device_id).encode('windows-1251'),
            headers={'Content-Type': 'application/xml', 'charset': 'windows-1251'}
        )

        response = requests.post(url=url_info_card, data=kontur_message.message_info_card(number_card))
        message = response.text
        sorted_message = DataSourceInfoCard(message)
        balance = sorted_message.get_balance_card()
        packages = sorted_message.get_list_package()

        data = {
            "number_card": number_card,
            "solution": solution,
            "balance": balance,
            "packages": packages,
            "sections": sections
        }
    else:
        data = {
            "number_card": number_card
        }
    return render(request, "lessons/passage_card.html", data)
