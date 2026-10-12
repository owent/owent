# Hi, I'm OWenT 👋

I develop **distributed systems frameworks and solutions**, **game server software and solutions**, and **cross-platform middleware for game servers and clients**. I also build runtime libraries and developer tools.

I work with **C++**, **Rust**, **Go**, **Lua**, **JavaScript**, **TypeScript**, and **Java**.

[![Blog](https://img.shields.io/badge/Blog-owent.net-126d78)](https://owent.net/)
[![atframework docs](https://img.shields.io/badge/Docs-atframework-426a91)](https://atframe.work/)
[![xresloader docs](https://img.shields.io/badge/Docs-xresloader-66508d)](https://xresloader.atframe.work/)
[![libcopp docs](https://img.shields.io/badge/Docs-libcopp-426a91)](https://libcopp.atframe.work/)
[![AICodeReviewer docs](https://img.shields.io/badge/Docs-AICodeReviewer-426a91)](https://aicr.atframe.work/)
[![LLM Usage docs](https://img.shields.io/badge/Docs-LLM%20Usage-426a91)](https://llm-usage.atframe.work/)
[![RSS](https://img.shields.io/badge/Subscribe-RSS-126d78)](https://owent.net/index.xml)

- Maintainer of [@atframework](https://github.com/atframework) and [@xresloader](https://github.com/xresloader)
- Member of [@open-telemetry](https://github.com/open-telemetry), Approver for [OpenTelemetry C++](https://github.com/open-telemetry/opentelemetry-cpp)
- Based in Shanghai, China
- Writing notes, deep dives, and engineering case studies at [owent.net](https://owent.net/)

## What I work on

- **Distributed systems & cloud-native infrastructure**: server frameworks and deployment solutions, communication systems, gateway services, service discovery, topology-driven routing, and automatic reconnection
- **Game server development & solutions**: backend architectures, stateful object routing, write-ahead logging (WAL) based distributed transactions and message queues, and reusable components for rank board, chatting, friend, guild, matchmaking, teams, High-performance player-to-player (P2P) marketplaces(support search across multiple attributes and tags, exchange-style trading with dynamic pricing, and direct-trade modes for competitive order claiming, flash sales, and auctions), Unreal Engine Dedicated Servers supporting/optimization and etc.
- **Cross-platform server/client middleware**: communication libraries, RPC frameworks, protocol integration, client SDKs, shared gameplay components, and configuration/data loading pipelines
- **Runtime & concurrency**: coroutine libraries, task scheduling, channels, and low-overhead components
- **Observability**: OpenTelemetry integration, metrics/tracing pipelines, diagnostics, and performance tuning
- **Build & engineering**: CMake toolchains, CI/CD workflows, configuration/code generation, data export pipelines, and game server/client build, packaging, and deployment tooling

## Featured projects

| Project | What it does | Start here |
| --- | --- | --- |
| **libcopp** | C++ stackful coroutines, C++20 coroutines, tasks, and channels | [Repo](https://github.com/owent/libcopp) · [Docs](https://libcopp.atframe.work/) |
| **atframework / atsf4g-co** | Cloud-native game server framework with coroutines, communication/gateways, generated RPCs, WAL, stateful object routing, distributed transactions/message queues, reusable game services, and observability | [Repo](https://github.com/atframework/atsf4g-co) · [Docs](https://atframe.work/) |
| **xresloader** | Excel export, batch conversion, validation, and generated data loaders | [Repo](https://github.com/owent/xresloader) · [Docs](https://xresloader.atframe.work/) |
| **llm-usage** | Desktop dashboard for local AI agent usage: tokens, requests, cache statistics, trends, import/merge, and budget reminders. **Pre-alpha.** | [Repo](https://github.com/owent/llm-usage) · [Docs](https://llm-usage.atframe.work/) · [Download](https://github.com/owent/llm-usage/releases/latest) |
| **AICodeReviewer** | Self-hosted AI review orchestration across GitHub, GitLab, Gitea/Forgejo, Perforce, and SVN, with agent adapters and structured findings | [Repo](https://github.com/atframework/AICodeReviewer) · [Docs](https://aicr.atframe.work/en/) |

## atframework ecosystem

[Documentation](https://atframe.work/) · [Organization](https://github.com/atframework)

Some repositories now live under `owent`; their original organization URLs remain working aliases.
The project links below point to current repositories, with the original paths kept alongside them.

| Project | Function | Original path / alias |
| --- | --- | --- |
| [atframe_utils](https://github.com/owent/atframe_utils) | Shared C++ utilities: logging, configuration, CLI parsing, algorithms, crypto, memory/data structures, and distributed-system primitives including WAL | [atframework/atframe_utils](https://github.com/atframework/atframe_utils) |
| [libatbus](https://github.com/owent/libatbus) | Async messaging over shared memory and network connections, with topology-driven node routing | [atframework/libatbus](https://github.com/atframework/libatbus) |
| [libatapp](https://github.com/owent/libatapp) | Application lifecycle, modules, configuration, messaging connectors, etcd service discovery, and topology-driven connection management/reconnection | [atframework/libatapp](https://github.com/atframework/libatapp) |
| [libcopp](https://github.com/owent/libcopp) | Coroutine and task runtime used by the server framework | — |
| [atsf4g-co](https://github.com/atframework/atsf4g-co) | Cloud-native game server framework with **atgateway** and **atproxy**, generated RPCs, WAL, stateful object routing, Redis, OpenTelemetry, distributed transactions and message queues (DTMQ), leaderboards, friends, matchmaking/teams, shared gameplay components, and Orbit UE Dedicated Server management | — |
| [cmake-toolset](https://github.com/owent/cmake-toolset) | CMake helpers, dependency builds, custom package versions/mirrors, and cross-compilation support | [atframework/cmake-toolset](https://github.com/atframework/cmake-toolset) |
| [generate-for-pb](https://github.com/atframework/generate-for-pb) | Protobuf-driven code generation with Mako and Jinja2 templates | — |
| [atdtool](https://github.com/atframework/atdtool) | Deployment tooling: merge values, render per-instance configuration/scripts, generate IDs, and watch files | — |
| [hiredis-happ](https://github.com/owent/hiredis-happ) | Async C++ Redis connector with reconnect/retry and Redis Cluster routing | — |

<details>
<summary>Go, Rust, C# bindings, and simulation tools</summary>

| Project | Function / status |
| --- | --- |
| [atsf4g-go](https://github.com/atframework/atsf4g-go) | Go game server framework intended to work with atsf4g-co |
| [libatapp-go](https://github.com/atframework/libatapp-go) | Go application lifecycle, module, event, and configuration framework |
| [libatbus-go](https://github.com/atframework/libatbus-go) | Go service communication layer; its README still lists core transport/routing work as TODO |
| [atframe-utils-go](https://github.com/atframework/atframe-utils-go) | Go utility packages and build-tool/configuration management |
| [libatbus-rs](https://github.com/atframework/libatbus-rs) | Rust communication middleware under development; its README describes design goals |
| [atlist-rs](https://github.com/atframework/atlist-rs) | Rust linked list with independently held iterators; other iterators survive insertions, moves, and removals |
| [jiffies-timer-rs](https://github.com/atframework/jiffies-timer-rs) | Rust jiffies timer implementation |
| [protoc-ext-render-rs](https://github.com/atframework/protoc-ext-render-rs) | protoc plugin for customizing generated code |
| [Atapp-CSharp](https://github.com/atframework/Atapp-CSharp) | C# access to libatapp through its C binding |
| [AtgwInnerCli-CSharp](https://github.com/atframework/AtgwInnerCli-CSharp) | C# access to the atgateway internal protocol through its C binding |
| [simulator-co](https://github.com/atframework/simulator-co) | Command-driven server/client simulation components with libuv and Lua integration |

</details>

## xresloader ecosystem

[Documentation](https://xresloader.atframe.work/) · [Organization](https://github.com/xresloader)

| Project | Function | Original path / alias |
| --- | --- | --- |
| [xresloader](https://github.com/owent/xresloader) | Java Excel export engine for Protobuf, MessagePack, Lua, JavaScript, JSON, XML, and UE data; validation, aliases, and merged tables | [xresloader/xresloader](https://github.com/xresloader/xresloader) |
| [xresconv-cli](https://github.com/owent/xresconv-cli) | Rust CLI for XML-configured batch conversion, scheme selection, parallel jobs, and command previews | [xresloader/xresconv-cli](https://github.com/xresloader/xresconv-cli) |
| [xresconv-gui](https://github.com/owent/xresconv-gui) | Tauri 2 desktop batch converter with a Node.js backend, search, output selection, previews, cancellation, and logs | [xresloader/xresconv-gui](https://github.com/xresloader/xresconv-gui) |
| [xresconv-conf](https://github.com/xresloader/xresconv-conf) | Shared XML batch-conversion configuration specification and examples for the CLI and GUI | — |
| [xres-code-generator](https://github.com/owent/xres-code-generator) | Generates configuration loaders and indexes from Protobuf declarations; C++, Lua, C#, Go, and UE templates | [xresloader/xres-code-generator](https://github.com/xresloader/xres-code-generator) |
| [xresloader-protocol](https://github.com/owent/xresloader-protocol) | Data headers and Protobuf extensions used by the export/loading pipeline | [xresloader/xresloader-protocol](https://github.com/xresloader/xresloader-protocol) |
| [xresloader-dump-bin](https://github.com/owent/xresloader-dump-bin) | Inspect binary exports as readable text and extract strings/tagged fields | [xresloader/xresloader-dump-bin](https://github.com/xresloader/xresloader-dump-bin) |
| [DynamicMessage-net](https://github.com/xresloader/DynamicMessage-net) | Dynamic Protobuf messages and indexed configuration loading for .NET using protobuf-net | — |
| [xresloader-docs](https://github.com/xresloader/xresloader-docs) | Documentation source and examples | — |
| [upload-to-github-release](https://github.com/xresloader/upload-to-github-release) | GitHub Action for uploading release assets, including overwrite support | — |

## Recent writing

Latest posts from [owent.net](https://owent.net/) · [Subscribe via RSS](https://owent.net/index.xml)

<!-- RECENT-POSTS:START -->
<!-- Generated from https://owent.net/index.xml; do not edit this block manually. -->

- 2026-09-07 · [大语言模型的基石：Transformer 入坑笔记（四） - 线性注意力(Linear Attention) 的基础](https://owent.net/2026/2611.html)
- 2026-06-28 · [大语言模型的基石：Transformer 入坑笔记（三） - 注意力机制和 Transformer](https://owent.net/2026/2610.html)
- 2026-06-25 · [大预言模型的基石：Transformer 入坑笔记（二） - 基本原理和 Word Embeddings](https://owent.net/2026/2609.html)
- 2026-05-01 · [大预言模型的基石：Transformer 入坑笔记（一） - 大模型训练链路](https://owent.net/2026/2608.html)
- 2026-05-01 · [国产大模型编码能力实测(GLM 5.1、Kimi K2.6、Mimo v2.5 Pro 和 DeepSeek V4 Pro)](https://owent.net/2026/2607.html)
- 2026-04-23 · [国产大模型（GLM 5.1、Kimi K2.6）真实场景效果和 Coding Plan 额度测试](https://owent.net/2026/2606.html)

<!-- RECENT-POSTS:END -->

<details>
<summary>More tools I maintain</summary>

| Project | Focus |
| --- | --- |
| [wxwork_robotd](https://github.com/owent/wxwork_robotd) | Enterprise WeChat bot access service |
| [ddns-cli](https://github.com/owent/ddns-cli) | DDNS client for Cloudflare / DNSPod |
| [coredns-nftables](https://github.com/owent/coredns-nftables) | CoreDNS plugin for nftables integration |
| [coredns-filter](https://github.com/owent/coredns-filter) | CoreDNS response filtering plugin |

</details>

## Around the web

- [GitHub](https://github.com/owent)
- [Blog / Notes](https://owent.net/)

<!-- Repository maintenance notes: docs/profile-maintenance.md -->
