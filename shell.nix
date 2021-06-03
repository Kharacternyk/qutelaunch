{ pkgs ? import <nixpkgs> { } }:

pkgs.python3Packages.buildPythonPackage {
  name = "qutelaunch";
  src = ./.;
  propagatedBuildInputs = with pkgs; [
    python3Packages.flask
  ];
}
