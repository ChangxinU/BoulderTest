from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--weights", required=False, help="Path to trained weights")
    parser.add_argument("--output", required=False, help="Path to Core ML package")
    args = parser.parse_args()

    print("Core ML export scaffold only.")
    print("Implement once model framework is selected and weights are available.")
    print(f"weights={args.weights}")
    print(f"output={args.output}")


if __name__ == "__main__":
    main()
