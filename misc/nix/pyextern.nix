{ lib, python3Packages }:

python3Packages.buildPythonApplication rec {
  pname = "pyextern";
  version = "0.1.0";
  pyproject = true;

  src = ../../.;

  build-system = with python3Packages; [ setuptools ];

  dependencies = with python3Packages; [ docutils numpy ];

  meta = {
    description = "Extern generator for the Haxe Python target.";
    homepage = "https://github.com/MolassesLover/pyextern-molasses";
    license = lib.licenses.mit;
  };
}
