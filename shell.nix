{ pkgs ? import <nixpkgs> { } }:

pkgs.python3Packages.buildPythonPackage {
  name = "qutelaunch";
  src = ./.;
  propagatedBuildInputs = with pkgs; [
    python3Packages.jinja2
  ];
  nativeBuildInputs = with pkgs; [
    python3Packages.pytest
    python3Packages.hypothesis
  ];
  QUTELAUNCH_DEBUG = "1";
}
