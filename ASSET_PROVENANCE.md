# Asset Provenance Documentation

This document establishes the complete genealogical documentation for every TraceLogging provider dataset in the TLGMapper repository.

## Windows 11 Provider Index

**File:** `TraceLoggingProviders/tlg_provider_index_Windows11_10.0.26200.7705.json`

**Origin:** Extracted from Windows 11 build 10.0.26200.7705 system binaries using TLGMapper's metadata extraction capabilities.

**Extraction Methodology:**
- Binary analysis performed on official Microsoft Windows 11 installation media
- TraceLogging metadata blobs parsed from x64 PE binaries
- Provider and event structures resolved using data-flow and call-graph analysis
- Output validated for structural correctness and completeness

**Build Number:** 10.0.26200.7705 (Windows 11 23H2)

## Windows Server 2025 Provider Index

**File:** `TraceLoggingProviders/tlg_provider_index_WindowsServer2025_10.0.26100.32230.json`

**Origin:** Extracted from Windows Server 2025 build 10.0.26100.32230 system binaries using TLGMapper's metadata extraction capabilities.

**Extraction Methodology:**
- Binary analysis performed on official Microsoft Windows Server 2025 installation media
- TraceLogging metadata blobs parsed from x64 PE binaries
- Provider and event structures resolved using data-flow and call-graph analysis
- Output validated for structural correctness and completeness

**Build Number:** 10.0.26100.32230 (Windows Server 2025)

## Redistribution Guidance

Before redistributing any TraceLogging provider data from this repository:

1. Verify the source licensing terms for the Windows binaries from which the data was extracted
2. Ensure compliance with Microsoft's terms of service for Windows system components
3. Document the redistribution in accordance with applicable software licensing agreements
4. Consider the intellectual property implications of redistributing Microsoft-owned metadata

## Forward-Looking Extensibility

All future additions of TraceLogging provider datasets to this repository must include:

- Complete provenance documentation following this template
- Build number specification with exact version information
- Extraction methodology description
- Validation of structural correctness
- Licensing compliance verification

This ensures that every dataset in the repository maintains the same level of supply-chain transparency and auditability.