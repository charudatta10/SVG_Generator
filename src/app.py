# This file is part of [Your Project Name]
#
# Copyright (C) 2024 Charudatta
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
from flask import Flask, request
from waitress import serve
from jinja2 import Template

#from origin import origin
app = Flask(__name__)

@app.route('/hi')
def hello_world():
    return 'Successful response.'

@app.route('/banner')
def svg_banner_endpoint():
    type = request.args.get('type')
    text1 = request.args.get('text1')
    text2 = request.args.get('text2')
    height = request.args.get('height')
    width = request.args.get('width')
    with open(f"docs/templates/{type}.svg","r+") as f:
        svg_str = f.read()
        svg_str = svg_str.replace('{text1}', text1, -1)
        svg_str = svg_str.replace('{text2}', text2, -1)
        svg_str = svg_str.replace('{height}', height, -1)
        svg_str = svg_str.replace('{width}', width, -1)

    # Assuming you have an svgs dictionary with different SVG templates
    svgs = {
        "origin": svg_str,
        }
    error_svg = "origin"

    svg = svgs.get(type, svgs[error_svg])
    return svg, 200, {'Content-Type': 'image/svg+xml'}

@app.route('/badges')
def svg_badges_endpoint():
    data = request.get_json()
    with open("docs/templates/badge_template.svg", 'r') as template_file:
        template_content = template_file.read()
    # Create a Jinja2 template
    template = Template(template_content)

    rendered_svg = template.render(**data)

    return rendered_svg, 200, {'Content-Type': 'image/svg+xml'}

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)

