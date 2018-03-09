# -*- coding: utf-8 -*-
import pip


def installer(package, params=['--user', '--upgrade']):
    """Update packages using pip

    :param package: package name
    :param params: pip command line arguments
    :return:
    """
    pip.main(['install', package] + params)


packages = ['pip',
            'numpy',  # numerical operations
            'scipy',  # scientific functions
            'numexpr',  # compiler for simple numerical expressions
            'numba',  # just-in-time compiler
            'joblib',  # easy parallelization
            'pandas',   # data frames
            'matplotlib',  # plotting
            'seaborn',  # better plotting
            'bokeh',  # dynamic plotting
            'plotly',  # online interactive plotting
            'scikit-learn',  # machine learning
            'keras',  # more machine learning
            'theano',  # more machine learning
            'sympy',  # symbolic mathematics
            'statsmodels',  # statistical models
            'pymc3',  # Bayesian stats
            'nltk',  # natural language tools
            'gensim',  # more natural language tools
            'spacy',  # advanced natural language tools
            'pillow',  # image manipulation
            'requests',  # http requests
            'arrow',  # improved date and time functionality
            'scrapy',  # web scraping
            'wxpython',  # gui tools
            'sh',  # shell subprocesses
            'fs',  # filesystem object handling
            'crontabs',  # cron jobs scheduler
            'pytest']  # unit testing

if __name__ == '__main__':
    for package in packages:
        installer(package)
