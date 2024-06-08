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

    # Assuming you have an svgs dictionary with different SVG templates
    svgs = {
        "origin": lambda text1, text2, height, width: f"""<svg fill="none" viewBox="0 0 {width} {height}" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
	<foreignObject width="100%" height="100%">
		<div xmlns="http://www.w3.org/1999/xhtml">
			<style>
				@keyframes rotate {{
					0% {{
						transform: rotate(3deg);
                    }}
					100% {{
						transform: rotate(-3deg);
                    }}
				}}

				@keyframes gradientBackground {{
					0% {{
						background-position: 0% 50%;
					}}
					50% {{
						background-position: 100% 50%;
					}}
					100% {{
						background-position: 0% 50%;
					}}
				}}

				@keyframes fadeIn {{
					0% {{
						opacity: 0;
					}}
					66% {{
						opacity: 0;
					}}
					100% {{
						opacity: 1;
					}}
				}}

				.container {{
					font-family:
						system-ui,
						-apple-system,
						'Segoe UI',
						Roboto,
						Helvetica,
						Arial,
						sans-serif,
						'Apple Color Emoji',
						'Segoe UI Emoji';
					display: flex;
					flex-direction: column;
					align-items: center;
					justify-content: center;
					margin: 0;
					width: 100%;
					height: {height}px;
					background: linear-gradient(-45deg, #fc5c7d, #6a82fb, #05dfd7);
					background-size: 600% 400%;
					animation: gradientBackground 10s ease infinite;
					border-radius: 10px;
					color: white;
					text-align: center;
				}}

				h1 {{
					font-size: 50px;
					line-height: 1.3;
					letter-spacing: 5px;
					text-transform: uppercase;
					text-shadow:
						0 1px 0 #efefef,
						0 2px 0 #efefef,
						0 3px 0 #efefef,
						0 4px 0 #efefef,
						0 12px 5px rgba(0, 0, 0, 0.1);
					animation: rotate ease-in-out 1s infinite alternate;
				}}

				p {{
					font-size: 20px;
					text-shadow: 0 1px 0 #efefef;
					animation: 5s ease 0s normal forwards 1 fadeIn;
				}}
			</style>
			<div class="container">
				<h1>{text1}</h1>
				<p>{text2}</p>
			</div>
		</div>
	</foreignObject>
</svg>
""",
        "glitch": lambda text1, text2, height, width: f"""<svg fill="none" viewBox="0 0 {width} {height}" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
	<foreignObject width="100%" height="100%">
		<div xmlns="http://www.w3.org/1999/xhtml">
			<style>
                .container {{
                font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji';
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                margin: 0;
                width: 100%;
                height: {height}px;
                /* background: linear-gradient(-45deg, #fc5c7d, #6a82fb, #05dfd7); */
                background: #333;
                background-size: 600% 400%;
                border-radius: 10px;
                /* color: white; */
                text-align: center;
                }}


                h1 {{
                text-align: center;
                color: #fff;
                font-size: 5em;
                letter-spacing: 8px;
                font-family: "Lucida Console", Monaco, monospace;	
                font-weight: 400;
                /*Create overlap*/
                
                margin: 0;
                line-height: 0;
                /*Animation*/
                
                animation: glitch1 2.5s infinite;
                }}

                h1:nth-child(2) {{
                color: #67f3da;
                animation: glitch2 2.5s infinite;
                }}

                h1:nth-child(3) {{
                color: #f16f6f;
                animation: glitch3 2.5s infinite;
                }}
                /*Keyframes*/

                @keyframes glitch1 {{
                0% {{
                    transform: none;
                    opacity: 1;
                }}
                7% {{
                    transform: skew(-0.5deg, -0.9deg);
                    opacity: 0.75;
                }}
                10% {{
                    transform: none;
                    opacity: 1;
                }}
                27% {{
                    transform: none;
                    opacity: 1;
                }}
                30% {{
                    transform: skew(0.8deg, -0.1deg);
                    opacity: 0.75;
                }}
                35% {{
                    transform: none;
                    opacity: 1;
                }}
                52% {{
                    transform: none;
                    opacity: 1;
                }}
                55% {{
                    transform: skew(-1deg, 0.2deg);
                    opacity: 0.75;
                }}
                50% {{
                    transform: none;
                    opacity: 1;
                }}
                72% {{
                    transform: none;
                    opacity: 1;
                }}
                75% {{
                    transform: skew(0.4deg, 1deg);
                    opacity: 0.75;
                }}
                80% {{
                    transform: none;
                    opacity: 1;
                }}
                100% {{
                    transform: none;
                    opacity: 1;
                }}
                }}

                @keyframes glitch2 {{
                0% {{
                    transform: none;
                    opacity: 0.25;
                }}
                7% {{
                    transform: translate(-2px, -3px);
                    opacity: 0.5;
                }}
                10% {{
                    transform: none;
                    opacity: 0.25;
                }}
                27% {{
                    transform: none;
                    opacity: 0.25;
                }}
                30% {{
                    transform: translate(-5px, -2px);
                    opacity: 0.5;
                }}
                35% {{
                    transform: none;
                    opacity: 0.25;
                }}
                52% {{
                    transform: none;
                    opacity: 0.25;
                }}
                55% {{
                    transform: translate(-5px, -1px);
                    opacity: 0.5;
                }}
                50% {{
                    transform: none;
                    opacity: 0.25;
                }}
                72% {{
                    transform: none;
                    opacity: 0.25;
                }}
                75% {{
                    transform: translate(-2px, -6px);
                    opacity: 0.5;
                }}
                80% {{
                    transform: none;
                    opacity: 0.25;
                }}
                100% {{
                    transform: none;
                    opacity: 0.25;
                }}
                }}

                @keyframes glitch3 {{
                0% {{
                    transform: none;
                    opacity: 0.25;
                }}
                7% {{
                    transform: translate(2px, 3px);
                    opacity: 0.5;
                }}
                10% {{
                    transform: none;
                    opacity: 0.25;
                }}
                27% {{
                    transform: none;
                    opacity: 0.25;
                }}
                30% {{
                    transform: translate(5px, 2px);
                    opacity: 0.5;
                }}
                35% {{
                    transform: none;
                    opacity: 0.25;
                }}
                52% {{
                    transform: none;
                    opacity: 0.25;
                }}
                55% {{
                    transform: translate(5px, 1px);
                    opacity: 0.5;
                }}
                50% {{
                    transform: none;
                    opacity: 0.25;
                }}
                72% {{
                    transform: none;
                    opacity: 0.25;
                }}
                75% {{
                    transform: translate(2px, 6px);
                    opacity: 0.5;
                }}
                80% {{
                    transform: none;
                    opacity: 0.25;
                }}
                100% {{
                    transform: none;
                    opacity: 0.25;
                }}
                }}
			</style>
			<div class="container">
                <h1>{text1}</h1>
                <h1>{text1}</h1>
                <h1>{text1}</h1>
            </div>
        </div>
	</foreignObject>
</svg>""",
        "luminance": lambda text1,text2, height, width: f"""<svg fill="none" viewBox="0 0 {width} {height}" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
	<foreignObject width="100%" height="100%">
		<div xmlns="http://www.w3.org/1999/xhtml">
			<style>
                .container {{
                font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji';
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                margin: 0;
                width: 100%;
                height: ${height}px;
                background: #333641;
                background-size: 600% 400%;
                border-radius: 10px;
                color: white;
                text-align: center;
                }}
              
                .luminance {{
                background: 50% 100%/50% 50% no-repeat radial-gradient(ellipse at bottom, #fff, transparent, transparent);
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
                font-size: 10vw;
                font-family:
						system-ui,
						-apple-system,
						'Segoe UI',
						Roboto,
						Helvetica,
						Arial,
						sans-serif,
						'Apple Color Emoji',
						'Segoe UI Emoji';
                -webkit-animation: reveal 3000ms ease-in-out forwards 200ms, glow 2500ms linear infinite 2000ms;
                        animation: reveal 3000ms ease-in-out forwards 200ms, glow 2500ms linear infinite 2000ms;
                }}
                @-webkit-keyframes reveal {{
                80% {{
                    letter-spacing: 8px;
                }}
                100% {{
                    background-size: 300% 300%;
                }}
                }}
                @keyframes reveal {{
                80% {{
                    letter-spacing: 8px;
                }}
                100% {{
                    background-size: 300% 300%;
                }}
                }}
                @-webkit-keyframes glow {{
                40% {{
                    text-shadow: 0 0 8px #fff;
                }}
                }}
                @keyframes glow {{
                40% {{
                    text-shadow: 0 0 8px #fff;
                }}
                }}
			</style>
			<div class="container">
                <div class="luminance">
                    {text1}
                </div>
            </div>
        </div>
	</foreignObject>
</svg> """,
    "rainbow": lambda text1,text2, height, width: f"""<svg fill="none" viewBox="0 0 {width} {height}" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
	<foreignObject width="100%" height="100%">
		<div xmlns="http://www.w3.org/1999/xhtml">
			<style>
                :root {{
                --color-background: #31037D;
                --axis-x: 1px;
                --axis-y: 1rem;
                --delay: 10;
                --color-black: #000;
                --color-white: #fff;
                --color-orange: #D49C3D;
                --color-red: #D14B3D;
                --color-violet: #CF52EB;
                --color-blue: #44A3F7;
                --color-green: #5ACB3C;
                --color-yellow: #DEBF40;
                --color-foreground: var(--color-white);
                }}
                .container {{
                font-family:
						system-ui,
						-apple-system,
						'Segoe UI',
						Roboto,
						Helvetica,
						Arial,
						sans-serif,
						'Apple Color Emoji',
						'Segoe UI Emoji';
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                margin: 0;
                width: 100%;
                height: {{height}}px;
                background-color: var(--color-background);
                background-size: 600% 400%;
                border-radius: 10px;
                color: rgba(255,255,255,.75);
                text-align: center;
                font-size: 24px;
                }}
                .c-rainbow {{
                counter-reset: rainbow;
                position: relative;
                display: block;
                list-style: none;
                padding: 0;
                margin: 0;
                line-height: 2px;
                }}
                .c-rainbow__layer {{
                --text-color: var(--color-foreground);
                counter-increment: rainbow;
                font-size: 3rem;
                font-weight: 600;
                color: var(--text-color);
                text-shadow: -1px -1px 0 var(--color-black), 1px -1px 0 var(--color-black), -1px 1px 0 var(--color-black), 1px 1px 0 var(--color-black), 4px 4px 0 rgba(0, 0, 0, 0.2);
                animation: rainbow 1.5s ease-in-out infinite;
                }}
                .c-rainbow__layer:nth-child(1) {{
                animation-delay: calc( 1 / var(--delay) * 1s);
                margin-left: 36px;
                /* z-index: -10; */
                }}
                .c-rainbow__layer:nth-child(2) {{
                animation-delay: calc( 2 / var(--delay) * 1s);
                margin-left: 30px;
                /* z-index: -20; */
                }}
                .c-rainbow__layer:nth-child(3) {{
                animation-delay: calc( 3 / var(--delay) * 1s);
                margin-left: 24px;
                /* z-index: -30; */
                }}
                .c-rainbow__layer:nth-child(4) {{
                animation-delay: calc( 4 / var(--delay) * 1s);
                margin-left: 18px;
                /* z-index: -40; */
                }}
                .c-rainbow__layer:nth-child(5) {{
                animation-delay: calc( 5 / var(--delay) * 1s);
                margin-left: 12px;
                /* z-index: -50; */
                }}
                .c-rainbow__layer:nth-child(6) {{
                animation-delay: calc( 6 / var(--delay) * 1s);
                margin-left: 6px;
                /* z-index: -60; */
                }}
                .c-rainbow__layer:nth-child(7) {{
                animation-delay: calc( 7 / var(--delay) * 1s);
                /* margin-left: 1em; */
                /* z-index: -70; */
                }}
                /* .c-rainbow__layer:not(:first-child) {{
                position: absolute;
                top: 0;
                }} */
                .c-rainbow__layer--white {{
                --text-color: var(--color-white);
                }}
                .c-rainbow__layer--orange {{
                --text-color: var(--color-orange);
                }}
                .c-rainbow__layer--red {{
                --text-color: var(--color-red);
                }}
                .c-rainbow__layer--violet {{
                --text-color: var(--color-violet);
                }}
                .c-rainbow__layer--blue {{
                --text-color: var(--color-blue);
                }}
                .c-rainbow__layer--green {{
                --text-color: var(--color-green);
                }}
                .c-rainbow__layer--yellow {{
                --text-color: var(--color-yellow);
                }}

                @keyframes rainbow {{
                0%, 100% {{
                    transform: translatey(var(--axis-y));
                }}
                50% {{
                    transform: translatey(calc(var(--axis-y) * -1));
                }}
                }}

			</style>
			<div class="container">
                <ul class="c-rainbow">
                    <li class="c-rainbow__layer c-rainbow__layer--yellow">{text1}</li>
                    <li class="c-rainbow__layer c-rainbow__layer--green">{text1}</li>
                    <li class="c-rainbow__layer c-rainbow__layer--blue">{text1}</li>
                    <li class="c-rainbow__layer c-rainbow__layer--violet">{text1}</li>
                    <li class="c-rainbow__layer c-rainbow__layer--red">{text1}</li>
                    <li class="c-rainbow__layer c-rainbow__layer--orange">{text1}</li>
                    <li class="c-rainbow__layer c-rainbow__layer--white">{text1}</li>
                </ul>
            </div>
        </div>
	</foreignObject>
</svg>
""",}
    error_svg = "origin"

    svg = svgs.get(type, svgs[error_svg])
    return svg(text1, text2, height, width), 200, {'Content-Type': 'image/svg+xml'}

if __name__ == '__main__':
    app.run(port=1234)
