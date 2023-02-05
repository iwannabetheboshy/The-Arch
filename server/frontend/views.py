from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ContactForm
import telebot
from django.contrib import messages
import os


Token = str(os.getenv('BotToken'))
bot=telebot.TeleBot(Token)

def cotact_modal_form(request, url):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['first_name']
            email = form.cleaned_data['email_address']
            city = form.cleaned_data['city']
            phone = form.cleaned_data['phone']
            category = form.cleaned_data['category']
            message = form.cleaned_data['message']
            file = form.cleaned_data['file']
            form.save()

            bot.send_message(457515370, 'Заявка с сайта\n Имя: {0}\n Email: {1}\n Город: {2}\n Телефон: {3}\n Категория: {4}\n Описание: {5}\n Файл: {6}'.
                             format(name, email, city, phone, category, message, file))
            return HttpResponseRedirect(url)



def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['first_name']
            email = form.cleaned_data['email_address']
            city = form.cleaned_data['city']
            phone = form.cleaned_data['phone']
            category = form.cleaned_data['category']
            message = form.cleaned_data['message']
            file = form.cleaned_data['file']
            form.save()

            bot.send_message(457515370, 'Заявка с сайта\n Имя: {0}\n Email: {1}\n Город: {2}\n Телефон: {3}\n Категория: {4}\n Описание: {5}\n Файл: {6}'.
                             format(name, email, city, phone, category, message, file))
            return HttpResponseRedirect("/")

    form = ContactForm()
    return render(request, 'frontend/home.html', {'form': form})


def projects(request):
    cotact_modal_form(request, '/projects')
    form = ContactForm()
    return render(request, 'frontend/projects.html', {'form': form})

def about(request):
    cotact_modal_form(request, '/about')
    form = ContactForm()
    return render(request, 'frontend/about.html', {'form': form})

def philosophy(request):
    cotact_modal_form(request, '/philosophy')
    form = ContactForm()
    return render(request, 'frontend/philosophy.html', {'form': form})

def bim(request):
    cotact_modal_form(request, '/bim')
    form = ContactForm()
    return render(request, 'frontend/bim.html', {'form': form})

def buying_mistakes(request):
    cotact_modal_form(request, '/buying-mistakes')
    form = ContactForm()
    return render(request, 'frontend/buying-mistakes.html', {'form': form})

def architecture_and_nature(request):
    cotact_modal_form(request, '/architecture-and-nature')
    form = ContactForm()
    return render(request, 'frontend/architecture-and-nature.html', {'form': form})

def prototyping(request):
    cotact_modal_form(request, '/prototyping')
    form = ContactForm()
    return render(request, 'frontend/prototyping.html', {'form': form})

def entry_group(request):
    cotact_modal_form(request, '/entry-group')
    form = ContactForm()
    return render(request, 'frontend/entry-group.html', {'form': form})

def architectural_style(request):
    cotact_modal_form(request, '/architectural-style')
    form = ContactForm()
    return render(request, 'frontend/architectural-style.html', {'form': form})

def finished_projects(request):
    cotact_modal_form(request, '/finished-projects')
    form = ContactForm()
    return render(request, 'frontend/finished-projects.html', {'form': form})


def projects_sample(request):
    if request.path_info == '/projects/residential-complex-in-nakhodka/':
        cotact_modal_form(request, '/residential-complex-in-nakhodka')
        form = ContactForm()
        return render(request, 'frontend/projects_sample/residential-complex-in-nakhodka.html', {'form': form})

    elif request.path_info == '/projects/river-park/':
        cotact_modal_form(request, '/river-park')
        form = ContactForm()
        return render(request, 'frontend/projects_sample/river-park.html', {'form': form})

    elif request.path_info == '/projects/modern-house/':
        cotact_modal_form(request, '/modern-house')
        form = ContactForm()
        return render(request, 'frontend/projects_sample/modern-house.html', {'form': form})

    elif request.path_info == '/projects/block-house/':
        cotact_modal_form(request, '/block-house')
        form = ContactForm()
        return render(request, 'frontend/projects_sample/block-house.html', {'form': form})

    elif request.path_info == '/projects/aljans/':
        cotact_modal_form(request, '/aljans')
        form = ContactForm()
        return render(request, 'frontend/projects_sample/aljans.html', {'form': form})

    elif request.path_info == '/projects/one-story-house/':
        cotact_modal_form(request, '/one-story-house')
        form = ContactForm()
        return render(request, 'frontend/projects_sample/one-story-house.html', {'form': form})

    elif request.path_info == '/projects/two-story-house/':
        cotact_modal_form(request, '/two-story-house')
        form = ContactForm()
        return render(request, 'frontend/projects_sample/two-story-house.html', {'form': form})

    elif request.path_info == '/projects/recreation-center-in-krasno/':
        cotact_modal_form(request, '/recreation-center-in-krasno')
        form = ContactForm()
        return render(request, 'frontend/projects_sample/recreation-center-in-krasno.html', {'form': form})

    elif request.path_info == '/projects/house-in-cottage-village/':
        cotact_modal_form(request, '/house-in-cottage-village')
        form = ContactForm()
        return render(request, 'frontend/projects_sample/house-in-cottage-village.html', {'form': form})

    elif request.path_info == '/projects/administrative-building/':
        cotact_modal_form(request, '/administrative-building')
        form = ContactForm()
        return render(request, 'frontend/projects_sample/administrative-building.html', {'form': form})

    elif request.path_info == '/projects/cottage-in-beregovoy/':
        cotact_modal_form(request, '/cottage-in-beregovoy')
        form = ContactForm()
        return render(request, 'frontend/projects_sample/cottage-in-beregovoy.html', {'form': form})

    elif request.path_info == '/projects/frame-house/':
        cotact_modal_form(request, '/frame-house')
        form = ContactForm()
        return render(request, 'frontend/projects_sample/frame-house.html', {'form': form})

    elif request.path_info == '/projects/high-tech/':
        cotact_modal_form(request, '/high-tech')
        form = ContactForm()
        return render(request, 'frontend/projects_sample/high-tech.html', {'form': form})

    elif request.path_info == '/projects/one-story-house-in-vladivostok/':
        cotact_modal_form(request, '/one-story-house-in-vladivostok')
        form = ContactForm()
        return render(request, 'frontend/projects_sample/one-story-house-in-vladivostok.html', {'form': form})

    else:
        cotact_modal_form(request, '/')
        form = ContactForm()
        return render(request, 'frontend/home.html', {'form': form})


def pre_project(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data['first_name']
            email = form.cleaned_data['email_address']
            city = form.cleaned_data['city']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            file = form.cleaned_data['file']
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено!')

            bot.send_message(457515370,
                            'Заявка с сайта\n Имя: {0}\n Email: {1}\n Город: {2}\n Телефон: {3}\n Описание: {4}\n Файл: {5}'.
                            format(name, email, city, phone, message, file))
            return HttpResponseRedirect("/service/preproject#contact")

    form = ContactForm()
    return render(request, 'frontend/service/pre-project.html', {'form': form})


def individual_housing_construction(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            print("YES")
            name = form.cleaned_data['first_name']
            email = form.cleaned_data['email_address']
            city = form.cleaned_data['city']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            file = form.cleaned_data['file']
            messages.success(request, 'Ваше сообщение успешно отправлено!')

            form.save()

            bot.send_message(457515370, 'Заявка с сайта\n Имя: {0}\n Email: {1}\n Город: {2}\n Телефон: {3}\n Описание: {4}\n Файл: {5}'.
                             format(name, email, city, phone, message, file))
            return HttpResponseRedirect("/service/individual-housing-construction#contact")

    form = ContactForm()
    return render(request, 'frontend/service/individual-housing-construction.html', {'form': form})


def fasad(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['first_name']
            email = form.cleaned_data['email_address']
            city = form.cleaned_data['city']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            file = form.cleaned_data['file']
            messages.success(request, 'Ваше сообщение успешно отправлено!')

            form.save()

            bot.send_message(457515370, 'Заявка с сайта\n Имя: {0}\n Email: {1}\n Город: {2}\n Телефон: {3}\n Описание: {4}\n Файл: {5}'.
                             format(name, email, city, phone, message, file))
            return HttpResponseRedirect("/service/fasad#contact")

    form = ContactForm()
    return render(request, 'frontend/service/fasad.html', {'form': form})


def commercial(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['first_name']
            email = form.cleaned_data['email_address']
            city = form.cleaned_data['city']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            file = form.cleaned_data['file']
            messages.success(request, 'Ваше сообщение успешно отправлено!')

            form.save()

            bot.send_message(457515370, 'Заявка с сайта\n Имя: {0}\n Email: {1}\n Город: {2}\n Телефон: {3}\n Описание: {4}\n Файл: {5}'.
                             format(name, email, city, phone, message, file))
            return HttpResponseRedirect("/service/commercial#contact")

    form = ContactForm()
    return render(request, 'frontend/service/commercial.html', {'form': form})
