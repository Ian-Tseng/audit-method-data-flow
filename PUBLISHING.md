# Publishing

Owner: Ian-Tseng. Package: `skills/audit-method-data-flow/`.

## Release gates

Before enabling managed repair, verify the policy/caller exact SHA agreement,
the `managed-repair-ready` label, required reviewers on both fixed protected
environments, explicit `OPENAI_API_KEY` passing, the Actions PR setting, and a
successful `workflow_dispatch` dry run. This repository is canary 1; activation still requires hosted read-back. A managed
draft never authorizes evidence acceptance, merge, release, publication,
installed replacement, or activation. Roll back policy and caller SHA together.

1. Confirm the worktree and reachable release history contain no credentials,
   confidential manuscripts, reviewer material, or private machine paths.
2. Confirm SOURCE.md still describes the owner decision and transformation.
3. Synchronize VERSION, root and packaged CITATION.cff,
   `references/package-version.json`, CHANGELOG.md, and the release tag.
4. Rebuild and verify the package manifest:

       py -3 -X utf8 skills\audit-method-data-flow\scripts\package_integrity.py build --write
       py -3 -X utf8 skills\audit-method-data-flow\scripts\package_integrity.py verify

5. Run the full suite and official validator in explicit UTF-8 mode:

       py -3 -X utf8 -m unittest discover -s tests -v
       py -3 -X utf8 <skill-creator-root>\scripts\quick_validate.py skills\audit-method-data-flow

   The full suite includes exact-byte accepted-map, current-record, evidence,
   and derived-report freshness checks. CI runs the same suite on Linux, macOS,
   and Windows so committed checkout bytes, rather than an unnormalized local
   worktree view, are the release authority.

6. Review the exact diff, push a versioned feature branch, open a PR whose title
   starts with the release version, and require every PR job to pass.
7. Merge without bypass and require the exact merged main commit to pass every
   main CI job. The initial non-installable repository bootstrap is not a skill
   release; every supported package release uses this PR gate.
8. Before tagging, require an active no-bypass `refs/tags/v*` update/deletion
   ruleset, private vulnerability reporting, and GitHub release immutability.
9. From exact merged main:

       gh skill publish .\skills --dry-run
       gh skill publish .\skills --tag v0.1.2
       gh release verify v0.1.2

10. In separate disposable consumer repositories, test public preview,
    Codex/Claude installation, list, directory-scoped update dry-run, package
    verification, helper execution, cleanup, and fresh activation when each
    client executable exists.

Installation does not prove client discovery or invocation. Structural
validation does not prove scientific validity or native visual rendering. If a
post-publication defect is found, increment the version; never rewrite a tag.
