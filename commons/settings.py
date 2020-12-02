#
# @settings.py Copyright (c) 2020 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 subsuelo Edif. La Unión, Av. Gral. Inofuentes, Calacoto, La Paz, Bolivia
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the termns of the license agreement you entered into
# with Jalasoft.
#

from django.conf import settings

# Base directory
BASE_DIR = settings.BASE_DIR

# PATH settings for Java and Python
PYTHON39_PATH = BASE_DIR / 'third_parties/python/Python39-32/python.exe'
JAVA13_PATH = BASE_DIR / 'third_parties/java/jdk-13.0.2/bin'

# File templates
PYTHON2_HELLO_WORLD = 'print "Hello world!"'
PYTHON3_HELLO_WORLD = 'print("Hello world!")'
JAVA13_HELLO_WORLD = '''package com;

public class Main {

	public static void main(String[] args) {
        System.out.println("Hello world!");
	}
}'''
