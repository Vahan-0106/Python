import sys
import urllib.request
import importlib.abc
import importlib.util

RAW_TMPL = "https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}.py"

class RepoLoader(importlib.abc.Loader):
    def __init__(self, source, origin):
        self._source = source
        self._origin = origin

    def create_module(self, spec):
        return None  

    def exec_module(self, module):
        code = compile(self._source, self._origin, "exec")
        exec(code, module.__dict__)

class RepoFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        try:
            owner, repo, *rest = fullname.split("__", 2)
            py_path = rest[0].replace(".", "/")
        except ValueError:
            return None

        url = RAW_TMPL.format(owner=owner,
                              repo=repo,
                              branch="master",
                              path=py_path)

        try:
            with urllib.request.urlopen(url) as r:
                if r.status != 200:
                    return None
                source = r.read().decode("utf-8")
        except Exception:
            return None

        loader = RepoLoader(source, origin=url)
        return importlib.util.spec_from_loader(fullname, loader, origin=url)

sys.meta_path.insert(0, RepoFinder())

module = importlib.import_module("blackbird71SR__Hello-World__HelloWorld")
