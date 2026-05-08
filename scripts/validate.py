#!/usr/bin/env python3
"""
TLGMapper Repository Validation Script

Validates repository integrity, governance compliance, and structural correctness.
Run this script locally before committing or in CI to ensure repository health.
"""

import os
import sys
import json
import glob
from pathlib import Path

def validate_file_presence():
    """Validate that all required governance files exist."""
    required_files = [
        'ASSET_PROVENANCE.md',
        'SECURITY.md',
        'DEPENDENCIES.md',
        '.github/CODEOWNERS',
        '.github/workflows/ci.yml',
        '.gitignore',
        'README.md',
        'TLGMapper.py'
    ]

    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)

    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False

    print("✅ All required governance files present")
    return True

def validate_python_syntax():
    """Validate Python syntax for all Python files."""
    python_files = ['TLGMapper.py', 'scripts/validate.py']

    for file_path in python_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                compile(f.read(), file_path, 'exec')
        except SyntaxError as e:
            print(f"❌ Syntax error in {file_path}: {e}")
            return False
        except Exception as e:
            print(f"❌ Error reading {file_path}: {e}")
            return False

    print("✅ Python syntax validation passed")
    return True

def validate_provider_indexes():
    """Validate TraceLogging provider index JSON files."""
    provider_dir = Path('TraceLoggingProviders')
    if not provider_dir.exists():
        print("❌ TraceLoggingProviders directory not found")
        return False

    json_files = list(provider_dir.glob('tlg_provider_index_*.json'))
    if not json_files:
        print("❌ No provider index JSON files found")
        return False

    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Basic structural validation
            if not isinstance(data, dict):
                print(f"❌ Invalid structure in {json_file}: not a JSON object")
                return False

            # Check for expected top-level keys (adjust based on actual structure)
            expected_keys = ['providers', 'metadata']  # Adjust as needed
            if not any(key in data for key in expected_keys):
                print(f"⚠️  Warning: Unexpected structure in {json_file}")

        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON in {json_file}: {e}")
            return False
        except Exception as e:
            print(f"❌ Error reading {json_file}: {e}")
            return False

    print(f"✅ Provider index validation passed ({len(json_files)} files)")
    return True

def validate_provenance_accuracy():
    """Validate that files declared in ASSET_PROVENANCE.md actually exist."""
    provenance_file = 'ASSET_PROVENANCE.md'

    try:
        with open(provenance_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract file references from provenance documentation
        declared_files = []
        for line in content.split('\n'):
            if line.startswith('**File:**'):
                file_path = line.split('**File:**')[1].strip().strip('`')
                declared_files.append(file_path)

        missing_provenance_files = []
        for file_path in declared_files:
            if not os.path.exists(file_path):
                missing_provenance_files.append(file_path)

        if missing_provenance_files:
            print(f"❌ Provenance-declared files missing: {', '.join(missing_provenance_files)}")
            return False

        print("✅ Provenance documentation accuracy validated")
        return True

    except Exception as e:
        print(f"❌ Error validating provenance: {e}")
        return False

def main():
    """Run all validation checks."""
    print("🔍 TLGMapper Repository Validation")
    print("=" * 40)

    checks = [
        validate_file_presence,
        validate_python_syntax,
        validate_provider_indexes,
        validate_provenance_accuracy
    ]

    all_passed = True
    for check in checks:
        if not check():
            all_passed = False

    print("=" * 40)
    if all_passed:
        print("🎉 All validation checks passed!")
        return 0
    else:
        print("❌ Validation failed. Please fix the issues above.")
        return 1

if __name__ == '__main__':
    sys.exit(main())