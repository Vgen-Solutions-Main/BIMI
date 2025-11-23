# BIMI Compliance Documentation

## Overview

This document describes the BIMI (Brand Indicators for Message Identification) compliance implementation for the IBIMjr logo.

## BIMI Requirements

BIMI requires brand logos to meet specific technical requirements to be displayed in email clients:

### 1. SVG Format Requirements

✅ **SVG Tiny 1.2 Portable/Secure (PS) Profile**
- The logo uses `version="1.2"` and `baseProfile="tiny-ps"`
- Compliant with the SVG Tiny 1.2 PS specification

✅ **No Scripts**
- The SVG contains no JavaScript or executable code

✅ **No External Images**
- The SVG uses only vector graphics (paths, circles, rectangles)
- No embedded base64 images or external image references

✅ **No Animations**
- The SVG is static with no `<animate>`, `<animateTransform>`, or other animation elements

✅ **No Embedded Fonts**
- The SVG uses only basic vector shapes, no custom fonts or `@font-face` declarations

✅ **Accessibility Elements**
- Includes `<title>` element: "IBIMjr Logo"
- Includes `<desc>` element with full description

### 2. File Size Requirements

✅ **Under 32KB**
- Current file size: **1.2KB** (1,177 bytes)
- Well under the recommended 32KB limit

### 3. Public Accessibility

✅ **Publicly Accessible HTTPS URL**
- The logo is hosted on GitHub Pages at: `https://jelvanricolcol.pro/BIMI.svg`
- Alternative URL: `https://vgen-solutions-main.github.io/BIMI.svg`
- Both URLs are accessible via HTTPS

## Logo Location

The BIMI-compliant SVG logo is located at:
- **Repository path**: `/BIMI.svg`
- **Public URL**: `https://jelvanricolcol.pro/BIMI.svg`
- **Fallback URL**: `https://vgen-solutions-main.github.io/BIMI.svg`

## BIMI DNS Record Example

To use this logo in your BIMI record, add the following TXT record to your DNS:

```
default._bimi.yourdomain.com. IN TXT "v=BIMI1; l=https://jelvanricolcol.pro/BIMI.svg"
```

Replace `yourdomain.com` with your actual domain name.

## Validation

You can validate the BIMI compliance of the logo using:
- [BIMI Validator](https://bimivalidator.com/)
- [BIMI Group Tools](https://bimigroup.org/bimi-generator/)

## Logo Design

The logo features:
- A blue circular background (#2563eb with #1e40af border)
- White "IBIM" text using simple geometric shapes
- Clean, minimal design optimized for email display
- Scalable vector graphics for crisp rendering at any size

## Technical Specifications

- **Format**: SVG 1.2 Tiny PS
- **Dimensions**: 200x200 viewBox
- **File Size**: 1,177 bytes (1.2KB)
- **Color Depth**: RGB colors
- **Compression**: None (plain XML for maximum compatibility)

## Maintenance

When updating the logo:
1. Ensure it remains under 32KB
2. Maintain SVG Tiny 1.2 PS compliance
3. Keep `<title>` and `<desc>` elements updated
4. Avoid scripts, external images, animations, or embedded fonts
5. Test with BIMI validators before deployment

## References

- [BIMI Group Specification](https://bimigroup.org/)
- [SVG Tiny 1.2 Specification](https://www.w3.org/TR/SVGTiny12/)
- [DMARC.org BIMI Information](https://dmarc.org/bimi/)
