# IBIMjr Logo - Email Publishing Assets

This directory contains email-ready versions of the IBIMjr logo.

## Available Formats

### PNG Files (Recommended for Email)
PNG format is recommended for email clients as it has universal support across all email platforms.

- **IBIMjr-150w.png** - Small size (150px wide) - Perfect for email footers or small inline images
- **IBIMjr-200w.png** - Small-medium size (200px wide) - Good for compact email headers
- **IBIMjr-400w.png** - Medium size (400px wide) - Standard email header size
- **IBIMjr-600w.png** - Large size (600px wide) - Full-width email header for desktop
- **IBIMjr-1200w.png** - High-resolution (1200px wide) - For retina displays and print

## Email Usage Instructions

### HTML Email Example

```html
<!-- Simple image tag -->
<img src="IBIMjr-400w.png" alt="IBIMjr Logo" width="400" style="max-width: 100%; height: auto; display: block;" />

<!-- With link -->
<a href="https://yourwebsite.com">
  <img src="IBIMjr-400w.png" alt="IBIMjr Logo" width="400" style="max-width: 100%; height: auto; display: block;" />
</a>

<!-- Responsive for mobile -->
<img src="IBIMjr-600w.png" alt="IBIMjr Logo" width="600" style="max-width: 100%; height: auto; display: block; margin: 0 auto;" />
```

### Best Practices for Email

1. **Always include alt text** - Essential for accessibility and when images don't load
2. **Set explicit width** - Prevents layout issues in email clients
3. **Use inline CSS** - Email clients don't support external or embedded CSS well
4. **Add max-width: 100%** - Ensures images scale on mobile devices
5. **Host images on a reliable server** - Don't embed large images directly in emails
6. **Test across email clients** - Gmail, Outlook, Apple Mail, etc. may render differently

### Size Recommendations

- **Email signature**: 150w or 200w
- **Email header**: 400w or 600w
- **Newsletter banner**: 600w or 1200w
- **Mobile optimization**: Always use `max-width: 100%; height: auto;`

## File Sizes

- IBIMjr-150w.png: ~3KB
- IBIMjr-200w.png: ~4KB
- IBIMjr-400w.png: ~9KB
- IBIMjr-600w.png: ~15KB
- IBIMjr-1200w.png: ~35KB

## Notes

- All PNG files have transparent backgrounds (RGBA format)
- Aspect ratio is preserved across all sizes
- Original SVG source: `../IBIMjr.svg`

## Testing Checklist

Before deploying in production emails:
- [ ] Test in Gmail (web and mobile app)
- [ ] Test in Outlook (Windows, Mac, and web)
- [ ] Test in Apple Mail (iOS and macOS)
- [ ] Test in other popular email clients
- [ ] Verify images load quickly
- [ ] Check mobile responsive behavior
- [ ] Verify alt text displays when images are blocked
