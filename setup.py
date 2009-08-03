from distutils.core import setup

setup(name='instwitter',
      version='0.9.0',
      description='Twitter API Library',
      author='Alecander Chichenin',
      author_email='sovnarkom@somebugs.com',
      url='http://github.com/sovnarkom/instwitter-py',
      packages=[
                'instwitter',
                'instwitter.authenticators',
                'instwitter.formatters',
                'instwitter.rest',
                'instwitter.rest.aggregated',
                'instwitter.streaming',
                'oauth'
               ]
      )