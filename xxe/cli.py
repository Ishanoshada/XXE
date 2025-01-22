"""Command line interface for XXE scanning tool."""

import argparse
import json
import sys
import logging
from .core import XXEAnalyzer

__version__ = '0.1.5'
__author__ = 'Ishan Oshada'
__email__ = 'ishan.kodithuwakku.offical@gamil.com'



def setup_logging(verbose):
    """Configure logging based on verbosity level."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def cli():
    """Command line interface for XXE scanning"""
    parser = argparse.ArgumentParser(
        description='XXE vulnerability scanner',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'file',
        help='XML file to scan'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    parser.add_argument(
        '--output',
        choices=['json', 'text'],
        default='text',
        help='Output format (default: text)'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version=f'XXE Scanner v{__version__}'
    )
    
    args = parser.parse_args()
    
    try:
        setup_logging(args.verbose)
        analyzer = XXEAnalyzer(verbose=args.verbose)
        report = analyzer.analyze_file(args.file)
        
        if args.output == 'json':
            print(json.dumps(report, indent=2))
        else:
            print("\nXXE Vulnerability Scan Report")
            print("=" * 30)
            print(f"File: {args.file}")
            print(f"Scan time: {report['scan_time']}")
            print("\nVulnerability Summary:")
            print(f"Total: {report['summary']['total_vulnerabilities']}")
            print(f"High: {report['summary']['severity_counts']['HIGH']}")
            print(f"Medium: {report['summary']['severity_counts']['MEDIUM']}")
            print(f"Low: {report['summary']['severity_counts']['LOW']}")
            
            if report['vulnerabilities']:
                print("\nDetailed Findings:")
                for vuln in report['vulnerabilities']:
                    print(f"\n{vuln['severity']}: {vuln['type']}")
                    print(f"Description: {vuln['description']}")
                    if vuln.get('details'):
                        print(f"Details: {json.dumps(vuln['details'], indent=2)}")
            else:
                print("\nNo vulnerabilities found.")
        
        sys.exit(0)
        
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        sys.exit(1)

def main():
    """Entry point for console script"""
    cli()

if __name__ == '__main__':
    main()