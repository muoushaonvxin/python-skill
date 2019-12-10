
```python
[root@zhangyz bin]# ./easy_install -U cython
Searching for cython
Reading https://pypi.python.org/simple/cython/
Downloading https://files.pythonhosted.org/packages/9c/9b/706dac7338c2860cd063a28cdbf5e9670995eaea408abbf2e88ba070d90d/Cython-0.29.14.tar.gz#sha256=e4d6bb8703d0319eb04b7319b12ea41580df44fd84d83ccda13ea463c6801414
Best match: Cython 0.29.14
Processing Cython-0.29.14.tar.gz
Writing /tmp/easy_install-oszvmluj/Cython-0.29.14/setup.cfg
Running Cython-0.29.14/setup.py -q bdist_egg --dist-dir /tmp/easy_install-oszvmluj/Cython-0.29.14/egg-dist-tmp-9llg_t1y
Unable to find pgen, not compiling formal grammar.
Compiling /tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Plex/Scanners.py because it changed.
Compiling /tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Plex/Actions.py because it changed.
Compiling /tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/Scanning.py because it changed.
Compiling /tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/Visitor.py because it changed.
Compiling /tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FlowControl.py because it changed.
Compiling /tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Runtime/refnanny.pyx because it changed.
Compiling /tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.py because it changed.
Compiling /tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Tempita/_tempita.py because it changed.
[1/8] Cythonizing /tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FlowControl.py
[2/8] Cythonizing /tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.py
[3/8] Cythonizing /tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/Scanning.py
[4/8] Cythonizing /tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/Visitor.py
[5/8] Cythonizing /tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Plex/Actions.py
[6/8] Cythonizing /tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Plex/Scanners.py
[7/8] Cythonizing /tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Runtime/refnanny.pyx
[8/8] Cythonizing /tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Tempita/_tempita.py
warning: no files found matching 'Doc/*'
warning: no files found matching '*.pyx' under directory 'Cython/Debugger/Tests'
warning: no files found matching '*.pxd' under directory 'Cython/Debugger/Tests'
warning: no files found matching '*.pxd' under directory 'Cython/Utility'
warning: no files found matching 'pyximport/README'
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c: In function ‘__pyx_pw_6Cython_8Compiler_9FusedNode_17FusedCFuncDefNode_21_dtype_type’:
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20769: warning: dereferencing pointer ‘func.2894’ does break strict-aliasing rules
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20769: note: initialized from here
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20735: warning: dereferencing pointer ‘func.2885’ does break strict-aliasing rules
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20735: note: initialized from here
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20736: warning: dereferencing pointer ‘func.2885’ does break strict-aliasing rules
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20736: note: initialized from here
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20736: warning: dereferencing pointer ‘func.2885’ does break strict-aliasing rules
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20736: note: initialized from here
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c: In function ‘__pyx_pw_6Cython_8Compiler_9FusedNode_17FusedCFuncDefNode_33_buffer_declarations’:
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20769: warning: dereferencing pointer ‘func.2894’ does break strict-aliasing rules
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20769: note: initialized from here
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20735: warning: dereferencing pointer ‘func.2885’ does break strict-aliasing rules
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20735: note: initialized from here
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20736: warning: dereferencing pointer ‘func.2885’ does break strict-aliasing rules
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20736: note: initialized from here
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20736: warning: dereferencing pointer ‘func.2885’ does break strict-aliasing rules
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20736: note: initialized from here
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20769: warning: dereferencing pointer ‘func.2894’ does break strict-aliasing rules
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20769: note: initialized from here
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20735: warning: dereferencing pointer ‘func.2885’ does break strict-aliasing rules
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20735: note: initialized from here
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20736: warning: dereferencing pointer ‘func.2885’ does break strict-aliasing rules
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20736: note: initialized from here
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20736: warning: dereferencing pointer ‘func.2885’ does break strict-aliasing rules
/tmp/easy_install-oszvmluj/Cython-0.29.14/Cython/Compiler/FusedNode.c:20736: note: initialized from here
creating /usr/local/python34/lib/python3.4/site-packages/Cython-0.29.14-py3.4-linux-x86_64.egg
Extracting Cython-0.29.14-py3.4-linux-x86_64.egg to /usr/local/python34/lib/python3.4/site-packages
Adding Cython 0.29.14 to easy-install.pth file
Installing cython script to /usr/local/python34/bin
Installing cythonize script to /usr/local/python34/bin
Installing cygdb script to /usr/local/python34/bin

Installed /usr/local/python34/lib/python3.4/site-packages/Cython-0.29.14-py3.4-linux-x86_64.egg
Processing dependencies for cython
Finished processing dependencies for cython
[root@zhangyz bin]# ll
total 17208
lrwxrwxrwx 1 root root       8 Sep 21  2017 2to3 -> 2to3-3.4
-rwxr-xr-x 1 root root     110 Sep 21  2017 2to3-3.4
-rwxr-xr-x 1 root root     398 Dec 10 15:15 cygdb
-rwxr-xr-x 1 root root     400 Dec 10 15:15 cython
-rwxr-xr-x 1 root root     406 Dec 10 15:15 cythonize
-rwxr-xr-x 1 root root     250 Sep 21  2017 easy_install
-rwxr-xr-x 1 root root     250 Sep 21  2017 easy_install-3.4
lrwxrwxrwx 1 root root       7 Sep 21  2017 idle3 -> idle3.4
-rwxr-xr-x 1 root root     108 Sep 21  2017 idle3.4
-rwxr-xr-x 1 root root     251 Sep 21  2017 iptest
-rwxr-xr-x 1 root root     251 Sep 21  2017 iptest3
-rwxr-xr-x 1 root root     244 Sep 21  2017 ipython
-rwxr-xr-x 1 root root     244 Sep 21  2017 ipython3
-rwxr-xr-x 1 root root     233 Dec 10 15:13 pip
-rwxr-xr-x 1 root root     233 Dec 10 15:13 pip3
-rwxr-xr-x 1 root root     233 Dec 10 15:13 pip3.4
lrwxrwxrwx 1 root root       8 Sep 21  2017 pydoc3 -> pydoc3.4
-rwxr-xr-x 1 root root      93 Sep 21  2017 pydoc3.4
-rwxr-xr-x 1 root root     235 Sep 21  2017 pygmentize
lrwxrwxrwx 1 root root       9 Sep 21  2017 python3 -> python3.4
-rwxr-xr-x 2 root root 8773578 Sep 21  2017 python3.4
lrwxrwxrwx 1 root root      17 Sep 21  2017 python3.4-config -> python3.4m-config
-rwxr-xr-x 2 root root 8773578 Sep 21  2017 python3.4m
-rwxr-xr-x 1 root root    3073 Sep 21  2017 python3.4m-config
lrwxrwxrwx 1 root root      16 Sep 21  2017 python3-config -> python3.4-config
lrwxrwxrwx 1 root root      10 Sep 21  2017 pyvenv -> pyvenv-3.4
-rwxr-xr-x 1 root root     245 Sep 21  2017 pyvenv-3.4
```
