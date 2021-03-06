# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016 Sistemas de Datos (<http://www.sdatos.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Sdatos Reminders Extra",
    'version': '1.0.0',
    'author' : 'Sistemas de Datos',
    'maintainer': 'Sistemas de Datos',
    'category': 'Reminders and Agenda',
    'website': 'http://sdatos.com',
    'summary': 'Reminders for Notes',
    'description' : """
Reminders Extra
===============

Module that add reminders in Notes
----------------------------------

This module have use reminder_base, module development by IT-Projects LLC, Ivan Yelizariev

    """, 
    'depends': ['reminder_base', 
                'note'],
    'data': [
        'views.xml',
        ],
    'installable': False,
}
