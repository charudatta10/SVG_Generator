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




def svg_badges_endpoint(path_template, path_json, path_svg):

    with open(path_json, "r") as f:
        data = json.load(f)

    with open(path_template, 'r') as template_file:
        template_content = template_file.read()

    # Create a Jinja2 template
    template = Template(template_content)

    rendered_svg = template.render(data)

    with open(path_svg, "w") as f:
        f.write(rendered_svg)

    

if __name__ == '__main__':
    svg_badges_endpoint("docs/templates/badge_template.svg", "tests/test.json", "tests/test1.svg")

