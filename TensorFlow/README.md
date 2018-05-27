## 安装tensorflow

<br>

<br>

```shell
[root@zhangyz ~]# /usr/local/python34/bin/pip3 install -i https://pypi.douban.com/simple tensorflow
Collecting tensorflow
Downloading https://pypi.doubanio.com/packages/1a/78/0c5afd582efacb2e9a1c7130d942d02466d62670f3cad0d4e224937ae749/tensorflow-1.8.0-cp34-cp34m-manylinux1_x86_64.whl (49.6MB)
  100% |████████████████████████████████| 49.6MB 417kB/s 
Collecting wheel>=0.26 (from tensorflow)
Downloading https://pypi.doubanio.com/packages/81/30/e935244ca6165187ae8be876b6316ae201b71485538ffac1d718843025a9/wheel-0.31.1-py2.py3-none-any.whl (41kB)
  100% |████████████████████████████████| 51kB 532kB/s 
Requirement already satisfied: six>=1.10.0 in /usr/local/python34/lib/python3.4/site-packages (from tensorflow)
Collecting termcolor>=1.1.0 (from tensorflow)
Downloading https://pypi.doubanio.com/packages/8a/48/a76be51647d0eb9f10e2a4511bf3ffb8cc1e6b14e9e4fab46173aa79f981/termcolor-1.1.0.tar.gz
Collecting grpcio>=1.8.6 (from tensorflow)
Downloading https://pypi.doubanio.com/packages/34/b8/3fb83a74d6d8352ed7e755da5790a06b1027868e22735c6d7c3a76c1fb4b/grpcio-1.12.0-cp34-cp34m-manylinux1_x86_64.whl (9.0MB)
  100% |████████████████████████████████| 9.0MB 473kB/s 
Collecting protobuf>=3.4.0 (from tensorflow)
Downloading https://pypi.doubanio.com/packages/03/80/c0718b484599694d57196107d1e66c288084d1cf51e518bd7b86dfab10aa/protobuf-3.5.2.post1-cp34-cp34m-manylinux1_x86_64.whl (6.4MB)
  100% |████████████████████████████████| 6.4MB 373kB/s 
Collecting gast>=0.2.0 (from tensorflow)
Downloading https://pypi.doubanio.com/packages/5c/78/ff794fcae2ce8aa6323e789d1f8b3b7765f601e7702726f430e814822b96/gast-0.2.0.tar.gz
Collecting numpy>=1.13.3 (from tensorflow)
Downloading https://pypi.doubanio.com/packages/10/ce/fc69d9ab5b375104b651745bedc72b8645ae038705ea25626db17dc75b14/numpy-1.14.3-cp34-cp34m-manylinux1_x86_64.whl (12.1MB)
  100% |████████████████████████████████| 12.1MB 437kB/s 
Collecting astor>=0.6.0 (from tensorflow)
Downloading https://pypi.doubanio.com/packages/b2/91/cc9805f1ff7b49f620136b3a7ca26f6a1be2ed424606804b0fbcf499f712/astor-0.6.2-py2.py3-none-any.whl
Collecting absl-py>=0.1.6 (from tensorflow)
Downloading https://pypi.doubanio.com/packages/57/8d/6664518f9b6ced0aa41cf50b989740909261d4c212557400c48e5cda0804/absl-py-0.2.2.tar.gz (82kB)
  100% |████████████████████████████████| 92kB 653kB/s 
Collecting tensorboard<1.9.0,>=1.8.0 (from tensorflow)
Downloading https://pypi.doubanio.com/packages/59/a6/0ae6092b7542cfedba6b2a1c9b8dceaf278238c39484f3ba03b03f07803c/tensorboard-1.8.0-py3-none-any.whl (3.1MB)
  100% |████████████████████████████████| 3.1MB 290kB/s 
Requirement already satisfied: setuptools in /usr/local/python34/lib/python3.4/site-packages (from protobuf>=3.4.0->tensorflow)
Collecting html5lib==0.9999999 (from tensorboard<1.9.0,>=1.8.0->tensorflow)
Downloading https://pypi.doubanio.com/packages/ae/ae/bcb60402c60932b32dfaf19bb53870b29eda2cd17551ba5639219fb5ebf9/html5lib-0.9999999.tar.gz (889kB)
  100% |████████████████████████████████| 890kB 384kB/s 
Collecting bleach==1.5.0 (from tensorboard<1.9.0,>=1.8.0->tensorflow)
Downloading https://pypi.doubanio.com/packages/33/70/86c5fec937ea4964184d4d6c4f0b9551564f821e1c3575907639036d9b90/bleach-1.5.0-py2.py3-none-any.whl
Requirement already satisfied: werkzeug>=0.11.10 in /usr/local/python34/lib/python3.4/site-packages (from tensorboard<1.9.0,>=1.8.0->tensorflow)
Collecting markdown>=2.6.8 (from tensorboard<1.9.0,>=1.8.0->tensorflow)
Downloading https://pypi.doubanio.com/packages/6d/7d/488b90f470b96531a3f5788cf12a93332f543dbab13c423a5e7ce96a0493/Markdown-2.6.11-py2.py3-none-any.whl (78kB)
  100% |████████████████████████████████| 81kB 258kB/s 
Installing collected packages: wheel, termcolor, grpcio, protobuf, gast, numpy, astor, absl-py, html5lib, bleach, markdown, tensorboard, tensorflow
Running setup.py install for termcolor ... done
Running setup.py install for gast ... done
Found existing installation: numpy 1.13.1
  Uninstalling numpy-1.13.1:
    Successfully uninstalled numpy-1.13.1
Running setup.py install for absl-py ... done
Found existing installation: html5lib 1.0.1
  Uninstalling html5lib-1.0.1:
    Successfully uninstalled html5lib-1.0.1
Running setup.py install for html5lib ... done
Found existing installation: bleach 2.1.3
  Uninstalling bleach-2.1.3:
    Successfully uninstalled bleach-2.1.3
Successfully installed absl-py-0.2.2 astor-0.6.2 bleach-1.5.0 gast-0.2.0 grpcio-1.12.0 html5lib-0.9999999 markdown-2.6.11 numpy-1.14.3 protobuf-3.5.2.post1 tensorboard-1.8.0 tensorflow-1.8.0 termcolor-1.1.0 wheel-0.31.1
```
