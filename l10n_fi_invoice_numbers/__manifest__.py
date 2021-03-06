##############################################################################
#
#    Author: Avoin.Systems
#    Copyright 2015-2019 Avoin.Systems
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

# noinspection PyStatementEffect
{
    "name": "Finnish Invoice References",
    "version": "12.0.1.0.0",
    "author": "Avoin.Systems",
    "category": "Localization",
    "website": "https://avoin.systems",
    "license": "AGPL-3",
    "images": ["static/description/icon.png"],
    "depends": [
        "account",
    ],
    "data": [
        "views/account_invoice_views.xml",
    ],
    "summary": "Suomalainen laskunumero",
    "active": False,
    "installable": True,
    "auto_install": False,
    "application": False
}
