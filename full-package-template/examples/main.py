import fastvector


"""
how to install the program locally:

detup.py
setup.cfg
pyproject.toml

One of these must be defined here. Why alternatives?
Because of the historical development of Python.

Today only use "pyproject.toml"!!!! Do not
use the other alternatives

Installation
------------

ch@ubuntu-ThinkPad-T470s:~/Documents/github-gmx/package-template$ pip install -e .
Defaulting to user installation because normal site-packages is not writeable
Obtaining file:///home/ch/Documents/github-gmx/package-template
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Installing backend dependencies ... done
  Preparing editable metadata (pyproject.toml) ... done
Building wheels for collected packages: fastvector
  Building editable for fastvector (pyproject.toml) ... done
  Created wheel for fastvector: filename=fastvector-1.0.0-0.editable-py3-none-any.whl size=2534 sha256=ad4a89f408624051dd032eb282d580ddfc7518c3d6e06d91f430b5611df58f6b
  Stored in directory: /tmp/pip-ephem-wheel-cache-92vykvxl/wheels/53/24/ae/346d6c26eb326d86deb738e3121d9493825eece1967ecf4ae2
Successfully built fastvector
Installing collected packages: fastvector
Successfully installed fastvector-1.0.0


"""

def main() -> None:
    V = fastvector.Vector2D(1, 1)
    print(V)


if __name__ == "__main__":
    main()
