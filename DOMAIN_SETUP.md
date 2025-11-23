# Custom Domain Setup Guide

This guide explains how to configure your custom domain `jelvanricolcol.pro` on Namecheap to work with this GitHub Pages site.

## Prerequisites

- GitHub Pages is enabled for this repository
- You have access to your Namecheap account for `jelvanricolcol.pro`
- The `CNAME` file in this repository contains your domain name

## DNS Configuration on Namecheap

### Option 1: Using A Records (Recommended for Apex Domain)

1. Log in to your Namecheap account
2. Go to Domain List and click "Manage" for `jelvanricolcol.pro`
3. Go to "Advanced DNS" tab
4. Add the following A Records:

   | Type | Host | Value | TTL |
   |------|------|-------|-----|
   | A Record | @ | 185.199.108.153 | Automatic |
   | A Record | @ | 185.199.109.153 | Automatic |
   | A Record | @ | 185.199.110.153 | Automatic |
   | A Record | @ | 185.199.111.153 | Automatic |

5. Add a CNAME record for www subdomain (optional):

   | Type | Host | Value | TTL |
   |------|------|-------|-----|
   | CNAME Record | www | vgen-solutions-main.github.io. | Automatic |

### Option 2: Using CNAME Record (For Subdomain like www or ibim)

If you want to use a subdomain like `ibim.jelvanricolcol.pro`:

1. Update the `CNAME` file in this repository to contain: `ibim.jelvanricolcol.pro`
2. In Namecheap DNS settings, add:

   | Type | Host | Value | TTL |
   |------|------|-------|-----|
   | CNAME Record | ibim | vgen-solutions-main.github.io. | Automatic |

## Verification

1. After configuring DNS, wait for propagation (can take 5 minutes to 24 hours)
2. Check DNS propagation: https://dnschecker.org
3. Visit your domain: https://jelvanricolcol.pro
4. Verify the SVG displays correctly

## HTTPS/SSL

GitHub Pages automatically provisions an SSL certificate for your custom domain. This may take a few hours after DNS configuration.

## Troubleshooting

### SVG Not Showing

- Ensure the `CNAME` file exists in the repository root
- Verify DNS records are correctly configured
- Check that Jekyll build includes the SVG (see `_config.yml`)
- Clear browser cache and try again

### Domain Not Working

- Verify DNS records using: `dig jelvanricolcol.pro`
- Check GitHub Pages settings in repository settings
- Ensure HTTPS is enforced in GitHub Pages settings

### 404 Errors

- Ensure the `_config.yml` has correct `url` and `baseurl` settings
- Verify the GitHub Actions workflow completed successfully
- Check that all required files are committed to the repository

## Files Involved

- `CNAME` - Contains your custom domain name
- `_config.yml` - Jekyll configuration with domain URL
- `.github/workflows/jekyll-gh-pages.yml` - GitHub Actions deployment workflow

## Support

For DNS issues, contact Namecheap support: https://www.namecheap.com/support/
For GitHub Pages issues, check: https://docs.github.com/pages
