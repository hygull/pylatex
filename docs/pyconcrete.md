# pyconcrete

```bash
Microsoft Windows [Version 10.0.16299.192]
(c) 2017 Microsoft Corporation. All rights reserved.

C:\Users\rishikesh agrawani>pip install pyconcrete --egg --install-option="--passphrase=quantsword"
C:\AnacondaPython2.5.0.1\lib\site-packages\pip\commands\install.py:194: UserWarning: Disabling all use of wheels due to the use of --build-options / --global-options / --install-options.
  cmdoptions.check_install_build_global(options)
DEPRECATION: --egg has been deprecated and will be removed in the future. This flag is mutually exclusive with large parts of pip, and actually using it invalidates pip's ability to manage the installation process.
Collecting pyconcrete
  Downloading pyconcrete-0.11.3.tar.gz (44kB)
    100% |################################| 51kB 76kB/s
Skipping bdist_wheel for pyconcrete, due to binaries being disabled for it.
Installing collected packages: pyconcrete
  Running setup.py install for pyconcrete ... error
    Complete output from command C:\AnacondaPython2.5.0.1\python.exe -u -c "import setuptools, tokenize;__file__='c:\\users\\rishik~1\\appdata\\local\\temp\\pip-build-4jmvjw\\pyconcrete\\setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record c:\users\rishik~1\appdata\local\temp\pip-iti1e6-record\install-record.txt --compile --passphrase=quantsword:
    running install
    running build
    running build_py
    creating build
    creating build\lib.win-amd64-2.7
    creating build\lib.win-amd64-2.7\pyconcrete
    copying src\pyconcrete\version.py -> build\lib.win-amd64-2.7\pyconcrete
    copying src\pyconcrete\__init__.py -> build\lib.win-amd64-2.7\pyconcrete
    running build_ext
    building 'pyconcrete._pyconcrete' extension
    error: Microsoft Visual C++ 9.0 is required. Get it from http://aka.ms/vcpython27

    ----------------------------------------
Command "C:\AnacondaPython2.5.0.1\python.exe -u -c "import setuptools, tokenize;__file__='c:\\users\\rishik~1\\appdata\\local\\temp\\pip-build-4jmvjw\\pyconcrete\\setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record c:\users\rishik~1\appdata\local\temp\pip-iti1e6-record\install-record.txt --compile --passphrase=quantsword" failed with error code 1 in c:\users\rishik~1\appdata\local\temp\pip-build-4jmvjw\pyconcrete\

C:\Users\rishikesh agrawani
```

Then I downloaded **Microsoft Visual C++ Compiler package for Python 2.7** from [http://aka.ms/vcpython27](http://aka.ms/vcpython27) and installed it.

```bash
rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Tasks/PyLaTex/pyconcrete
$ ls
pyconcrete.py

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Tasks/PyLaTex/pyconcrete
$ python pyconcrete.py
Fullname:- Rishikesh Agrawani
Age:- 25

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Tasks/PyLaTex/pyconcrete
$ pyconcrete-admin.py compile --source=pyconcrete.py  --pye

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Tasks/PyLaTex/pyconcrete
$ ls
pyconcrete.py  pyconcrete.pye

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Tasks/PyLaTex/pyconcrete
$ mkdir pyconcrete_enc

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Tasks/PyLaTex/pyconcrete
$ mv pyconcrete.pye ./pyconcrete_enc/

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Tasks/PyLaTex/pyconcrete
$ ls
pyconcrete.py  pyconcrete_enc/

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Tasks/PyLaTex/pyconcrete
$ cd pyconcrete_enc/

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Tasks/PyLaTex/pyconcrete/pyconcrete_enc
$ ls
pyconcrete.pye

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Tasks/PyLaTex/pyconcrete/pyconcrete_enc
$ pyconcrete pyconcrete.pye
Fullname:- Rishikesh Agrawani
Age:- 25

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Tasks/PyLaTex/pyconcrete/pyconcrete_enc
$ cat pyconcrete.pye
k▒!▒]▒:▒ ▒▒2▒F▒▒6v▒#▒▒+_▒▒▒▒P▒eb▒NU▒yy▒▒G▒▒▒▒▒▒▒;HYጕm▒▒Y'8▒t8▒ Sm
cO▒▒Vr▒M▒4▒▒▒▒▒\▒▒▒▒0-7▒n▒e▒TV▒▒?-▒▒U▒7▒▒f&▒f▒1▒.6▒oW.Eġ
                                                        ▒▒▒2▒▒▒\5CM▒
W8m\▒[Q6++▒Q▒K1▒▒▒DR▒kq@▒▒▒:f▒▒▒▒
                                 ▒▒▒▒▒-▒"▒Q&b▒{6▒bM▒▒▒[>ּ        3
▒▒q▒+▒▒▒Q▒UvOҰ▒▒0$▒▒▒▒KB▒▒▒▒=▒}5▒▒7j▒$▒▒ȸ▒
                                          ▒▒
                                            ▒
                                             ▒<Vl'A&Z▒▒▒}
                                                         ▒+S▒4▒ᴾ▒▒;▒▒▒▒▒▒▒▒▒▒t▒lgl▒▒▒▒▒`▒k▒:▒0Z
                                                                                               ^
                                                                                                ▒▒▒&|#▒▒7▒▒▒▒@ ▒C▒ ▒▒C▒▒▒▒yO▒▒▒▒▒lE▒▒▒C▒!▒i▒7▒▒▒A▒;'▒ĈQf<=▒>▒▒▒&j▒$▒▒ȸ▒
                                                                ▒▒
                                                                  ▒
                                                                   ▒▒$▒▒▒▒&▒mbdPC▒▒>v'▒t▒Qr'▒]n
                                                                                               ▒#+ݧ]=▒(g(S▒G*Y\˾▒ϚJ>8▒L▒{▒/TO▒▒▒▒e▒S▒'5▒▒&▒Z-f▒▒λ!"J*˻▒1▒▒▒▒kp7{g▒ڱhpxI$vcNo▒▒▒▒-x▒▒▒▒B▒▒▒▒x▒▒▒p▒▒4▒▒▒▒▒▒׀$▒7q▒▒i▒L▒▒▒6▒q▒>▒▒P`▒S▒I▒7▒q٩▒▒▒▒E36▒▒ԕ"▒\▒
                                        _f▒*)<▒▒▒▒l▒▒l▒▒▒▒▒
▒▒9▒▒▒▒▒▒▒l ▒mU▒[G▒P▒!y▒▒JH▒W▒G▒▒

rishikesh agrawani@DESKTOP-8AATOO4 MINGW64 /d/projects/Tasks/PyLaTex/pyconcrete/pyconcrete_enc
$
```

***In short***

```bash
 python pyconcrete.py
  645  pyconcrete-admin.py compile --source=pyconcrete.py  --pye
  646  ls
  647  mkdir pyconcrete_enc
  648  mv pyconcrete.pye ./pyconcrete_enc/
  649  ls
  650  cd pyconcrete_enc/
  651  ls
  652  pyconcrete pyconcrete.pye
  653  cat pyconcrete.pye

  ```