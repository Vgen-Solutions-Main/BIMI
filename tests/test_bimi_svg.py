"""
Tests for BIMI SVG logo compliance
"""

import os
import xml.etree.ElementTree as ET


def test_svg_exists():
    """Test that the SVG file exists"""
    svg_path = os.path.join(os.path.dirname(__file__), '..', 'IBIMjr.svg')
    assert os.path.exists(svg_path), "IBIMjr.svg file not found"
    print("✓ SVG file exists")


def test_svg_valid_xml():
    """Test that the SVG is valid XML"""
    svg_path = os.path.join(os.path.dirname(__file__), '..', 'IBIMjr.svg')
    try:
        tree = ET.parse(svg_path)
        root = tree.getroot()
        assert root is not None
        print("✓ SVG is valid XML")
    except ET.ParseError as e:
        assert False, f"SVG is not valid XML: {e}"


def test_svg_version_and_profile():
    """Test that SVG has correct version and baseProfile for BIMI"""
    svg_path = os.path.join(os.path.dirname(__file__), '..', 'IBIMjr.svg')
    tree = ET.parse(svg_path)
    root = tree.getroot()
    
    # Check version
    version = root.get('version')
    assert version == '1.2', f"SVG version should be 1.2, got {version}"
    
    # Check baseProfile
    base_profile = root.get('baseProfile')
    assert base_profile == 'tiny-ps', f"SVG baseProfile should be 'tiny-ps', got {base_profile}"
    
    print("✓ SVG has correct version (1.2) and baseProfile (tiny-ps)")


def test_svg_square_dimensions():
    """Test that SVG has square (1:1) dimensions"""
    svg_path = os.path.join(os.path.dirname(__file__), '..', 'IBIMjr.svg')
    tree = ET.parse(svg_path)
    root = tree.getroot()
    
    viewBox = root.get('viewBox')
    assert viewBox is not None, "SVG should have viewBox attribute"
    
    parts = viewBox.split()
    assert len(parts) == 4, "viewBox should have 4 values"
    
    width = int(parts[2])
    height = int(parts[3])
    assert width == height, f"SVG should be square (1:1), got {width}x{height}"
    
    print(f"✓ SVG has square dimensions ({width}x{height})")


def test_svg_has_title():
    """Test that SVG has <title> element for accessibility"""
    svg_path = os.path.join(os.path.dirname(__file__), '..', 'IBIMjr.svg')
    tree = ET.parse(svg_path)
    root = tree.getroot()
    
    # Find title element (handle namespaces)
    namespace = {'svg': 'http://www.w3.org/2000/svg'}
    title = root.find('svg:title', namespace)
    if title is None:
        # Try without namespace
        for child in root:
            if 'title' in child.tag.lower():
                title = child
                break
    
    assert title is not None, "SVG should have <title> element"
    assert title.text and len(title.text.strip()) > 0, "SVG <title> should have text content"
    
    print(f"✓ SVG has <title>: {title.text}")


def test_svg_has_desc():
    """Test that SVG has <desc> element for accessibility"""
    svg_path = os.path.join(os.path.dirname(__file__), '..', 'IBIMjr.svg')
    tree = ET.parse(svg_path)
    root = tree.getroot()
    
    # Find desc element (handle namespaces)
    namespace = {'svg': 'http://www.w3.org/2000/svg'}
    desc = root.find('svg:desc', namespace)
    if desc is None:
        # Try without namespace
        for child in root:
            if 'desc' in child.tag.lower():
                desc = child
                break
    
    assert desc is not None, "SVG should have <desc> element"
    assert desc.text and len(desc.text.strip()) > 0, "SVG <desc> should have text content"
    
    print(f"✓ SVG has <desc>: {desc.text[:50]}...")


def test_svg_file_size():
    """Test that SVG file is under 32KB (BIMI requirement)"""
    svg_path = os.path.join(os.path.dirname(__file__), '..', 'IBIMjr.svg')
    file_size = os.path.getsize(svg_path)
    max_size = 32 * 1024  # 32KB in bytes
    
    assert file_size < max_size, f"SVG file size ({file_size} bytes) exceeds 32KB limit"
    
    print(f"✓ SVG file size is {file_size} bytes (well under 32KB limit)")


def test_svg_no_script_tags():
    """Test that SVG contains no <script> tags"""
    svg_path = os.path.join(os.path.dirname(__file__), '..', 'IBIMjr.svg')
    with open(svg_path, 'r') as f:
        content = f.read()
    
    assert '<script' not in content.lower(), "SVG should not contain <script> tags"
    
    print("✓ SVG contains no script tags")


def test_svg_has_solid_background():
    """Test that SVG has a solid background (not transparent)"""
    svg_path = os.path.join(os.path.dirname(__file__), '..', 'IBIMjr.svg')
    tree = ET.parse(svg_path)
    root = tree.getroot()
    
    # Look for a rect that covers the entire viewBox
    viewBox = root.get('viewBox')
    parts = viewBox.split()
    width = int(parts[2])
    height = int(parts[3])
    
    # Find all rect elements (handle namespaces)
    namespace = {'svg': 'http://www.w3.org/2000/svg'}
    rects = root.findall('.//svg:rect', namespace)
    if not rects:
        rects = [child for child in root if child.tag.endswith('rect')]
    
    # Check if there's a background rect
    has_background = False
    for rect in rects:
        rect_width = rect.get('width')
        rect_height = rect.get('height')
        rect_x = rect.get('x', '0')
        rect_y = rect.get('y', '0')
        
        if (rect_width == str(width) and rect_height == str(height) and 
            rect_x == '0' and rect_y == '0'):
            fill = rect.get('fill')
            assert fill and fill != 'none' and fill != 'transparent', "Background rect should have a solid fill"
            has_background = True
            print(f"✓ SVG has solid background: {fill}")
            break
    
    assert has_background, "SVG should have a solid background rect covering the entire viewBox"


def test_index_html_exists():
    """Test that index.html exists for GitHub Pages"""
    index_path = os.path.join(os.path.dirname(__file__), '..', 'index.html')
    assert os.path.exists(index_path), "index.html file not found"
    print("✓ index.html exists")


def test_index_html_references_svg():
    """Test that index.html references the SVG file"""
    index_path = os.path.join(os.path.dirname(__file__), '..', 'index.html')
    with open(index_path, 'r') as f:
        content = f.read()
    
    assert 'IBIMjr.svg' in content, "index.html should reference IBIMjr.svg"
    assert 'https://jelvanricolcol.pro/IBIMjr.svg' in content or 'jelvanricolcol.pro' in content, \
        "index.html should reference the public URL"
    
    print("✓ index.html references SVG file and public URLs")


def run_all_tests():
    """Run all BIMI compliance tests"""
    print("Running BIMI SVG compliance tests...\n")
    
    test_svg_exists()
    test_svg_valid_xml()
    test_svg_version_and_profile()
    test_svg_square_dimensions()
    test_svg_has_title()
    test_svg_has_desc()
    test_svg_file_size()
    test_svg_no_script_tags()
    test_svg_has_solid_background()
    test_index_html_exists()
    test_index_html_references_svg()
    
    print("\n✓ All BIMI compliance tests passed!")


if __name__ == "__main__":
    run_all_tests()
