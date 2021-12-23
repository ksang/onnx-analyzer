import argparse, sys
import logging
from onnx_analyzer import analyze_single, analyze, report

def main():
    parser = argparse.ArgumentParser(description='ONNX analyzer')
    parser.add_argument('-p', '--path', type=str, help='Parent path to ONNX models.')
    parser.add_argument('-m', '--model', type=str, help='Path to an ONNX model.')
    parser.add_argument('-macs', '--calculate-macs', action='store_true', help='Calculate MACs.')
    parser.add_argument('-vis', '--visualize', action='store_true', help='Display visualizations.')
    parser.add_argument('-out', type=str, default='result.png', help='Output file for visualizations.')
    parser.add_argument('--loglevel', default='warning', type=str,
                        help='Provide logging level. Example --loglevel debug' )
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel.upper(), format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')

    if args.path != None:
        results = analyze(args.path, args.calculate_macs)
    elif args.model != None:
        results = analyze_single(args.model, args.calculate_macs)
    else:
        print("No path or model specified!")
        sys.exit(1)
    
    report(results, args.out, args.visualize)

if __name__ == '__main__':
    main()