# Profile maintenance

`README.md` is the public GitHub profile. Keep its introduction and project descriptions
human-maintained; only the `RECENT-POSTS` block is generated.

## Blog automation

The blog homepage advertises `https://owent.net/index.xml` as its RSS feed.
The updater uses Python's standard library, with no third-party feed service or packages.
It selects the six newest published article URLs, sorts by `pubDate`, removes duplicates,
normalizes Hugo's `//owent.net/...` links to HTTPS, and displays dates in Asia/Shanghai.
Titles come from the feed verbatim, with escaping for Markdown and HTML.

```sh
python scripts/update_recent_posts.py
python scripts/update_recent_posts.py --check
python -m unittest discover -s tests -v
```

For offline verification, use `--feed-file /path/to/feed.xml`. `--limit` changes the count.
The updater preserves everything outside the markers, including the original newline style.
Missing/duplicate markers, an unavailable feed, invalid XML/dates, or a feed without published
articles cause a failing exit status and retain the existing article list. Network requests
have a 30-second timeout, at most three attempts, and a 2 MiB response limit.
Updates use a temporary file and atomic replacement; a failed replacement preserves the README.
Unchanged content causes no write or commit.

[The workflow](../.github/workflows/update-profile.yml) runs at **09:23 and 21:23 Asia/Shanghai**,
on relevant pushes, and through **Actions → Update profile → Run workflow**.
It runs offline tests first. Pull requests and forks only run verification.
Only the default branch of `owent/owent` can run the update job; only that job has
`contents: write`, and it stages only `README.md`. It uses the built-in `GITHUB_TOKEN`.
Actions are pinned to the verified release commit SHAs.

The workflow must be on the default branch with Actions enabled. Repository policies
must allow the bot to push; otherwise that step will fail. It never force-pushes, so a
concurrent human push is retained and the update can be retried. Scheduled executions may
be delayed, and GitHub disables schedules in public repositories after 60 days without
repository activity. Re-enable the workflow in Actions when needed.
See [GitHub's schedule documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).

## Repository research

Checked on **2026-10-11**, using the live public GitHub repository directories, each
project's README, and source files where the README was missing or insufficient.
GitHub repository descriptions alone are insufficient: xresconv-gui's metadata still
mentions Electron, while its current README documents Tauri 2 and a Node.js backend.

The old paths below were requested through `https://api.github.com/repos/<old-path>`;
the returned `full_name` and `html_url` identified the current repository.
Keep both current links and old alias links in the public profile.

| Working alias | Current repository / README |
| --- | --- |
| [atframework/atframe_utils](https://github.com/atframework/atframe_utils) | [owent/atframe_utils](https://github.com/owent/atframe_utils/blob/main/README.md) |
| [atframework/libatbus](https://github.com/atframework/libatbus) | [owent/libatbus](https://github.com/owent/libatbus/blob/main/README.md) |
| [atframework/libatapp](https://github.com/atframework/libatapp) | [owent/libatapp](https://github.com/owent/libatapp/blob/main/README.md) |
| [atframework/cmake-toolset](https://github.com/atframework/cmake-toolset) | [owent/cmake-toolset](https://github.com/owent/cmake-toolset/blob/main/README.md) |
| [xresloader/xresloader](https://github.com/xresloader/xresloader) | [owent/xresloader](https://github.com/owent/xresloader/blob/main/README.md) |
| [xresloader/xresconv-cli](https://github.com/xresloader/xresconv-cli) | [owent/xresconv-cli](https://github.com/owent/xresconv-cli/blob/main/README.md) |
| [xresloader/xresconv-gui](https://github.com/xresloader/xresconv-gui) | [owent/xresconv-gui](https://github.com/owent/xresconv-gui/blob/main/README.md) |
| [xresloader/xres-code-generator](https://github.com/xresloader/xres-code-generator) | [owent/xres-code-generator](https://github.com/owent/xres-code-generator/blob/main/README.md) |
| [xresloader/xresloader-protocol](https://github.com/xresloader/xresloader-protocol) | [owent/xresloader-protocol](https://github.com/owent/xresloader-protocol/blob/main/README.md) |
| [xresloader/xresloader-dump-bin](https://github.com/xresloader/xresloader-dump-bin) | [owent/xresloader-dump-bin](https://github.com/owent/xresloader-dump-bin/blob/main/README.md) |

`atframework/libcopp` returned 404. Use [owent/libcopp](https://github.com/owent/libcopp/blob/v2/README.md);
do not invent an organization alias for it.

Additional primary sources for the descriptions:

- [atsf4g-co README](https://github.com/atframework/atsf4g-co/blob/main/README.md) and
  [atframework documentation](https://atframe.work/): server infrastructure and reusable components.
  **atgateway** and **atproxy** are directories inside atsf4g-co, not separate repositories in this inventory.
- [atframe_utils headers](https://github.com/owent/atframe_utils/tree/main/include): utility scope;
  [libatbus topology header](https://github.com/owent/libatbus/blob/main/include/atbus_topology.h): topology registry;
  [libatapp headers](https://github.com/owent/libatapp/tree/main/include/atframe): modules, connectors, and etcd.
- [WAL primitives](https://github.com/owent/atframe_utils/tree/main/include/distributed_system),
  [libatapp discovery/connection management](https://github.com/owent/libatapp/blob/main/src/atframe/modules/service_discovery_module.cpp),
  [stateful object routing](https://github.com/atframework/atsf4g-co/blob/main/doc/docs/architecture/router.md), and
  [game components and reusable services](https://github.com/atframework/atsf4g-co/blob/main/doc/docs/components/overview.md):
  sources checked locally on 2026-10-12 when expanding the user-confirmed professional focus areas.
- [generate-for-pb](https://github.com/atframework/generate-for-pb/tree/main): `mako-generator.py`,
  `jinja2-generator.py`, and `generator_ipc.py` establish its code-generation backends;
  this repository has no root README.
- [atdtool README](https://github.com/atframework/atdtool/blob/main/README.md) and
  [hiredis-happ README](https://github.com/owent/hiredis-happ/blob/main/README.md): deployment and Redis tooling.
  Sentinel in hiredis-happ is design-only and is not advertised as supported.
- [atsf4g-go README](https://github.com/atframework/atsf4g-go/blob/main/README.md),
  [libatapp-go README](https://github.com/atframework/libatapp-go/blob/main/README.md),
  [atframe-utils-go source](https://github.com/atframework/atframe-utils-go/tree/main), and
  [its build settings documentation](https://github.com/atframework/atframe-utils-go/blob/main/build_setting/README.md): Go framework and utility scope.
- [libatbus-go TODOs](https://github.com/atframework/libatbus-go/blob/main/README.md) and
  [libatbus-rs design goals](https://github.com/atframework/libatbus-rs/blob/main/README.md):
  describe development scope without implying transport parity or production readiness.
- [atlist-rs README](https://github.com/atframework/atlist-rs/blob/master/README.md),
  [jiffies-timer-rs README](https://github.com/atframework/jiffies-timer-rs/blob/main/README.md), and
  [protoc-ext-render-rs README](https://github.com/atframework/protoc-ext-render-rs/blob/main/README.md): Rust supporting libraries and protoc customization.
- [Atapp-CSharp README](https://github.com/atframework/Atapp-CSharp/blob/master/README.md),
  [AtgwInnerCli-CSharp README](https://github.com/atframework/AtgwInnerCli-CSharp/blob/master/README.md),
  [simulator-co source](https://github.com/atframework/simulator-co/tree/main), and
  [libsimulator_uv README](https://github.com/atframework/simulator-co/blob/main/libsimulator_uv/README.md): bindings and simulation components.
- [xres-code-generator templates](https://github.com/owent/xres-code-generator/tree/main/template),
  [xresloader-protocol core](https://github.com/owent/xresloader-protocol/tree/main/core),
  [xresconv-conf specification](https://github.com/xresloader/xresconv-conf/blob/main/README.md), and
  [DynamicMessage-net README](https://github.com/xresloader/DynamicMessage-net/blob/master/README.md): loading, protocol, and batch configuration scope.
- [xresloader documentation source](https://github.com/xresloader/xresloader-docs) and
  [upload-to-github-release README](https://github.com/xresloader/upload-to-github-release/blob/v1/README.md): supporting projects.
- [llm-usage README](https://github.com/owent/llm-usage/blob/main/README.md) and
  [documentation](https://llm-usage.atframe.work/): desktop usage dashboard and pre-alpha status.
- [AICodeReviewer README](https://github.com/atframework/AICodeReviewer/blob/main/README.md) and
  [documentation](https://aicr.atframe.work/en/): review orchestration, VCS integrations, and output contracts.

The profile covers the main runtime, server, export/loading, deployment, and binding projects.
Website deployment mirrors, release-action test repositories, unrelated forks, and small
internal support repositories are omitted from the main directory.

## Profile components

The profile uses linked documentation/RSS badges, a Mermaid project map, and native
`<details>` sections for supporting projects. These work within GitHub's README renderer;
the diagram source remains readable if a client cannot render Mermaid. Badges are the only
external image service, and each badge has descriptive alt text plus a plain-link counterpart.

Useful later additions include locally generated contribution SVGs or release summaries
for selected repositories. A contribution animation can be decorative, but should not
replace the project explanations. Public statistics cards depend on their provider and
often exclude private/organization work, so no aggregate contribution claims are added.

GitHub READMEs do not run arbitrary interactive JavaScript. Keep richer interactive demos
in the project documentation sites and link them from the profile. See
[GitHub diagram support](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams)
and [GitHub Markup sanitization](https://github.com/github/markup#github-markup).

## Local verification on 2026-10-11

- 14 offline regression tests passed with Python 3.15.0, including feed failure,
  date/URL handling, escaping, marker boundaries, idempotence, and failed atomic replacement.
- The updater fetched the live RSS successfully, and a second `--check` reported no changes.
  The feed, all six generated article URLs, and the five project documentation entrypoints returned HTTP 200.
- markdownlint-cli2 0.23.3 passed for both Markdown files; actionlint 1.7.12 passed for the workflow.
- GitHub's Markdown API returned HTTP 200 and recognized five tables, two details sections,
  and a Mermaid enrichment container. This is renderer evidence, not browser/SVG visual validation.
- `git diff --check` passed. The workflow has not been run on GitHub; its Python 3.13 runner
  and bot push will be exercised after the change reaches the default branch.
