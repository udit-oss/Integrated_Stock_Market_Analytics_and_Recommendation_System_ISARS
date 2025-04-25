from setuptools import setup, find_packages

setup(
    name="isars_commons",                
    version="0.1.0",                      
    author="Udit",                  
    author_email="udit9503@gmail.com",    
    description="Shared utilities for ISARS project",
    packages=find_packages(where="src"),  
    package_dir={"": "src"},              
    install_requires=[                    
        "SQLAlchemy>=1.4",
        "python-dotenv>=0.19",
        "psycopg2-binary>=2.9"
    ],
    python_requires=">=3.8",          
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
