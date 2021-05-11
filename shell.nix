{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  propagatedBuildInputs = with pkgs; [
    python3Packages.jinja2
  ];
  nativeBuildInputs = with pkgs; [
    python3Packages.pytest
    python3Packages.hypothesis
  ];
}
