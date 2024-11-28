import setuptools

setuptools.setup(     
     name="telcorain",     
     version="0.0.1",
     python_requires=">=3.8",   
     packages=["telcorain"],
     install_requires=['influxdb_client==1.48.0',   
                        'mariadb==1.1.6',
                        'matplotlib==3.9.2',
                        'numpy==1.23.5',
                        'pandas==1.5.0',
                        'Pillow==9.2.0',
                        'pycomlink==0.4.1',
                        'PyQt6==6.7.1',
                        'PyQt6_sip==13.4.0',
                        'Requests==2.32.3',
                        'scipy==1.14.1',
                        'setuptools==75.6.0',
                        'Shapely==1.8.4',
                        'urllib3==1.26.12',
                        'xarray==2023.12.0'])