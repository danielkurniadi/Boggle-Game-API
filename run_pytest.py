import pytest

if __name__ == '__main__':
    try:
        result = pytest.main(['-s', '-vv', '-W ignore::DeprecationWarning'])
        if result:
            raise Exception({'failure': True})
    except Exception as e:
        print(e)
