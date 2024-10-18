
from setuptools import setup, find_packages  

setup(  
    name='HackaPUCSP',                  # Substitua pelo nome do seu projeto  
    version='0.1.0',                             # Versão do seu projeto  
    description='hackaton 2024 PUC-SP',  # Breve descrição do seu projeto  
    author='Fabiana campanari',                           # Seu nome ou nome da sua organização  
    author_email='fabicampanari@proton.me',        # Seu e-mail  
    url='https://github.com/Mindful-AI-Assistants/HackaPUCSP'  # URL do repositório do seu projeto  
    packages=find_packages(),                    # Encontra automaticamente pacotes e subpacotes  
    install_requires=[                           # Lista de dependências do seu projeto  
        'dependencia1',                          # Exemplo: 'numpy',  
        'dependencia2',                          # Exemplo: 'requests',  
    ],  
    classifiers=[                                # Classificadores que descrevem seu projeto  
        'Programming Language :: Python :: 3',  # Indica que é um projeto Python 3  
        'License : MIT License', # Licença do projeto  
        'Operating System :: OS Independent',    # Sistema operacional independente  
    ],  
    python_requires='>=3.6',                    # Versão mínima do Python necessária  
)
