"""
https://github.com/flasgger/flasgger
"""

from flask import Flask, jsonify
from flasgger import Swagger, SwaggerView, Schema, fields


class Color(Schema):
    name = fields.Str()


class Palette(Schema):
    pallete_name = fields.Str()
    colors = Color


class PaletteView(SwaggerView):
    parameters = [
        {
            "name": "palette",
            "in": "path",
            "type": "string",
            "enum": ["all", "rgb", "cmyk"],
            "required": True,
            "default": "all"
        }
    ]
    responses = {
        200: {
            "description": "A list of colors (may be filtered by palette)",
            "schema": Palette
        },
        404: {"description": "Not Found"}
    }

    def get(self, palette):
        """
        Colors API using schema
        """
        all_colors = {
            'cmyk': ['cyan', 'magenta', 'yellow', 'black'],
            'rgb': ['red', 'green', 'blue']
        }
        if palette == 'all':
            result = all_colors
        else:
            result = {palette: all_colors.get(palette)}

        return jsonify(result)


app = Flask(__name__)
swagger = Swagger(app)

app.add_url_rule(
    '/colors/<palette>',
    view_func=PaletteView.as_view('colors'),
    methods=['GET']
)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(debug=True)
