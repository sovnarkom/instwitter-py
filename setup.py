from distutils.core import setup
from instwitter import __version__

setup(name='instwitter',
      version=__version__,
      description='Twitter API Library',
      author='Alexander Chichenin',
      author_email='sovnarkom@somebugs.com',
      url='http://github.com/sovnarkom/instwitter-py',
      packages=[
                'instwitter',
                'instwitter.authenticators',
                'instwitter.formatters',
                'instwitter.rest.partial',
                'instwitter.rest',
                'instwitter.streaming',
                'oauth'
               ]
      )