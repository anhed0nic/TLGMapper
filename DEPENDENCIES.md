# Dependencies

This document inventories all dependencies required for TLGMapper development, testing, and operation.

## Runtime Dependencies

TLGMapper has no runtime Python package dependencies. It operates using only Python standard library modules and IDA Pro's built-in IDAPython environment.

**Python Version Requirement:** Python 3.8+ (compatible with IDA Pro's embedded Python)

**System Requirements:**
- IDA Pro 8.x+ with IDAPython support
- Windows, macOS, or Linux host system (IDA Pro compatibility)

## Development Dependencies

### Python Packages

| Package | Version | Purpose | License |
|---------|---------|---------|---------|
| None | N/A | Core functionality uses only stdlib | N/A |

### Development Tools

| Tool | Version | Purpose | License |
|------|---------|---------|---------|
| IDA Pro | 8.x+ | Primary development and testing environment | Proprietary |

## Testing Dependencies

| Package | Version | Purpose | License |
|---------|---------|---------|---------|
| None | N/A | Validation scripts use only stdlib | N/A |

## CI/CD Dependencies

| Service | Version | Purpose | License |
|---------|---------|---------|---------|
| GitHub Actions | N/A | Automated validation pipeline | Proprietary |
| Ubuntu | latest | CI runner environment | Various |

## License Inventory

All dependencies are licensed under permissive terms compatible with TLGMapper's MIT license:

- Python Standard Library: PSF License (permissive)
- IDA Pro: Commercial license (development tool, not distributed)

## SBOM Integration

For Software Bill of Materials (SBOM) purposes:

- **Primary Component:** TLGMapper.py (MIT License)
- **No External Dependencies:** Zero third-party runtime dependencies
- **Development Tools:** IDA Pro (commercial, not included in SBOM)
- **CI Infrastructure:** GitHub Actions (SaaS, not included in SBOM)

This minimal dependency footprint ensures TLGMapper can be safely integrated into enterprise environments with strict dependency policies.