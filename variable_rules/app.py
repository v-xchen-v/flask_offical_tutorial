# ou can add variable sections to a URL by marking sections with <variable_name>. Your function then receives the <variable_name> as a keyword argument. Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.
# converter: string, int, float, path, uuid


from flask import Flask
app = Flask(__name__)
from markupsafe import escape

@app.route('/user/<username>')
def show_user_name(user_name):
    return f'User {escape(user_name)}'

@app.route('/post/{int:<post_id>}')
def show_post(post_id):
    # the post_id is an integer
    return f'Post {post_id}';

@app.route('/path/<path:sub_path>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'