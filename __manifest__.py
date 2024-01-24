# -*- coding: utf-8 -*-
<<<<<<< Updated upstream
###################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Cybrosys Technologies(<http://www.cybrosys.com>).
#    Author: cybrosys(<https://www.cybrosys.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
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
###################################################################################
{
    'name': 'Biometric Device Integration',
    'version': '12.0.1.1.1',
    'summary': """Integrating Biometric Device With HR Attendance (Face + Thumb)""",
    'description': 'This module integrates Odoo with the biometric device(Model: ZKteco uFace 202)',
=======
{
    'name': "Zkteco, eSSL, Cams Biometrics Integration Module with HR Attendance",
    'summary': """Receives the attendance/punches from the biometric devices and updates in hr.attendance module of odoo server.""",
    'description': """
        The module is developed based on the Cams biometric web api as documented at https://camsunit.com/application/biometric-web-api.html. It receives the biometric attendance on realtime and integrates with hr.attendance module. 
        
	It supports all the cams biometrics machines listed at https://camsunit.com/product/home.html
        It alos supports 
        	ZKTeco, 
        	eSSL, 
        	Identix, 
        	BioMax 
        	and more biometric machines provided they are verified at https://developer.camsunit.com/
        
        Module requires valid API license as listed at https://camsunit.com/application/biometric-web-api.html#api_cost
        
    """,

    'author': "Cams Biometrics",
>>>>>>> Stashed changes
    'category': 'Generic Modules/Human Resources',
    'version': '1.0',
    'license': 'AGPL-3',
    'company': 'Cams Biometrics',
    'website': "https://www.camsunit.com",
    'depends': ['hr','hr_attendance'],
    'installable': True,
    'images':[
        'static/description/banner.png',
        ],
    'data': [
        'security/ir.model.access.csv',
<<<<<<< Updated upstream
        'views/zk_machine_view.xml',
        'views/zk_machine_attendance_view.xml',
        'data/download_data.xml'

    ],
    'images': ['static/description/banner.gif'],
    'license': 'AGPL-3',
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
=======
        'views/views.xml',
        'views/config.xml',
        'views/inherited_employee_view.xml',
    ]
>>>>>>> Stashed changes
}
