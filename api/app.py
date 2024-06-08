from flask import Flask, request
#from origin import origin
app = Flask(__name__)

@app.route('/hi')
def hello_world():
    return 'Successful response.'

@app.route('/')
def svg_endpoint():
    type = request.args.get('type')
    text1 = request.args.get('text1')
    text2 = request.args.get('text2')
    height = request.args.get('height')
    width = request.args.get('width')
    with open(f"SVG/{type}.svg","r+") as f:
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

if __name__ == '__main__':
    app.run(port=1234)
