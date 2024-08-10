{
  description = "A very basic flake";

  inputs = { nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable"; };

  outputs = { self, nixpkgs }:
    let
      supportedSystems =
        [ "x86_64-linux" "x86_64-darwin" "aarch64-linux" "aarch64-darwin" ];

      forAllSystems = nixpkgs.lib.genAttrs supportedSystems;
    in {
      packages = forAllSystems (system:
        let
          pkgs = (import nixpkgs { inherit system; });
          pyextern = pkgs.callPackage misc/nix/pyextern.nix { };
        in rec {
          inherit pyextern;
          default = pyextern;
          devShell = pkgs.mkShell { inputsFrom = [ pyextern ]; };
        });
    };
}
