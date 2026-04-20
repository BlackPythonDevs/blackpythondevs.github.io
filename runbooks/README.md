# Runbooks

Step-by-step guides for common maintenance tasks on `blackpythondevs.github.io`,
derived from the merged PRs of the last ~12 months.

| Task                               | Runbook                                                        | Example PRs            |
| ---------------------------------- | -------------------------------------------------------------- | ---------------------- |
| Add a foundational supporter       | [add-foundational-supporter.md](add-foundational-supporter.md) | #893, #879, #870       |
| Add a corporate sponsor            | [add-corporate-sponsor.md](add-corporate-sponsor.md)           | #888, #866             |
| Add a BPD Council member           | [add-council-member.md](add-council-member.md)                 | #853, #851, #849       |
| Publish a blog post / announcement | [publish-blog-post.md](publish-blog-post.md)                   | #888, #864             |
| Add or update a sponsored event    | [add-sponsored-event.md](add-sponsored-event.md)               | #863, #854             |
| Fix a broken link or 404           | [fix-broken-link.md](fix-broken-link.md)                       | #892, #890, #856       |
| Update site navigation             | [update-navigation.md](update-navigation.md)                   | #844, #840, #830, #829 |

## Before you start

Every runbook assumes:

1. You have cloned the repo and installed dependencies: `just sync`
2. You branch from `gh-pages` (the default branch) and open a PR back to `gh-pages`.
3. You run `just pre-commit` and `just test` before pushing.
4. You preview locally with `just serve` (render-engine dev server).

See `CONTRIBUTING.md` and `MAINTAINERS.md` for repository-wide conventions.
