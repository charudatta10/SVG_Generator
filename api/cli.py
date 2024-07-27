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
import json
from jinja2 import Template




def svg_badges_endpoint(path_json, file_name):

    with open(path_json, "r") as f:
        data = json.load(f)

    with open("../SVG/badge_template.svg", 'r') as template_file:
        template_content = template_file.read()

    # Create a Jinja2 template
    template = Template(template_content)

    rendered_svg = template.render(data)

    with open(file_name, "w") as f:
        f.write(rendered_svg)

    

if __name__ == '__main__':
    svg_badges_endpoint("test.json", "test1.svg")

