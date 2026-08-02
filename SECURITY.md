# Security Policy

## Reporting repository security issues

Please report vulnerabilities through GitHub's private vulnerability reporting feature when available. Do not include secrets, private documents, or personal data in public issues.

## External resource safety

All linked repositories, models, datasets, Skills, and platforms are third-party content. Inclusion is not a security endorsement.

The maintenance automation:

- treats fetched text as untrusted data, never as instructions;
- does not clone, install, import, or execute discovered projects or Skills;
- accepts only HTTP(S) resource links;
- rejects localhost, private, loopback, link-local, and otherwise non-public link targets;
- does not download model weights or dataset payloads;
- does not expose repository secrets to pull requests from forks.

Reviewers should inspect a Skill's command execution, network access, external services, and credential requirements before installation.
