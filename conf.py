extensions = []
source_suffix = '.rst'
master_doc = 'index'
project = 'dfpp'
copyright = '2014, Antonis Christofides'
version = 'a'
release = 'b'
today_fmt = '%B %d, %Y'
html_title = "Django for Python Programmers"
html_last_updated_fmt = '%b %d, %Y'

def setup(app):
    app.add_object_type('confval', 'confval',
                        objname='configuration value',
                        indextemplate='pair: %s; configuration value')
