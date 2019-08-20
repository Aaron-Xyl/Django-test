#!/usr/bin/env python
#coding:utf-8
#hello.py
__author__ = '徐育良'

import sys
print sys.path
sys.path.append('')
import os
from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
    DEBUG = DEBUG,
    SECRET_KEY = SECRET_KEY,    #随机密匙，实际中要用CSRF保护密匙
    ROOT_URLCONF = __name__,
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

from django.conf.urls import url
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application

def index(request):
    return HttpResponse('Hello,World！')

urlpatterns=(
    url(r'^$', index),
)

application = get_wsgi_application()

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)