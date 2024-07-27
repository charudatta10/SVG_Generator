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
