[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/vyahello/asynchronous.svg?branch=master)](https://travis-ci.org/vyahello/sync-to-async)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with flake8](https://img.shields.io/badge/flake8-checked-blue)](http://flake8.pycqa.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

# Synchronous to Asynchronous optimization

> Describes how we could optimize our python code based on built-in asynchronous approach.

## Tools

### Production
- python 3.6 +
- asyncIO

### Development

- [travis](https://travis-ci.org/)
- [pytest](https://pypi.org/project/pytest/)
- [black](https://black.readthedocs.io/en/stable/)
- [mypy](http://mypy.readthedocs.io/en/latest)
- [flake8](http://flake8.pycqa.org/en/latest/)

### Quick start

```bash
git clone git@github.com:vyahello/sync-to-async.git
python demo/sync.py
# Done in 9.23 sec.
python demo/async.py
# Done in 1.06 sec.
```

**[⬆ back to top](#synchronous-to-asynchronous-optimization)**

## Development notes

### CI

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`, `flake8`, `mypy`).

To be able to run code analysis, please execute command below:
```bash
./analyse-source-code.sh
```

### Meta

Author – _Vladimir Yahello_.

Distributed under the `MIT` license. See [license](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127/](https://www.linkedin.com/in/volodymyr-yahello-821746127/)

**[⬆ back to top](#synchronous-to-asynchronous-optimization)**
