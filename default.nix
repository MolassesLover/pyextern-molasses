{ pkgs ? import <nixpkgs> { } }: pkgs.callPackage ./misc/nix/pyextern.nix { }
