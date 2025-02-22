# DongTai
[![django-project](https://img.shields.io/badge/django%20versions-3.0.3-blue)](https://www.djangoproject.com/)
[![license Apache-2.0](https://img.shields.io/github/license/HXSecurity/DongTai-agent-java)](https://github.com/HXSecurity/DongTai-agent-java/blob/main/LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/HXSecurity/DongTai?label=DongTai)](https://github.com/HXSecurity/DongTai/releases)

[![GitHub release](https://img.shields.io/github/v/release/HXSecurity/Dongtai-webapi?label=Dongtai-webapi)](https://github.com/HXSecurity/DongTai-webapi/releases)
[![GitHub release](https://img.shields.io/github/v/release/HXSecurity/Dongtai-openapi?label=Dongtai-openapi)](https://github.com/HXSecurity/DongTai-openapi/releases)
[![GitHub release](https://img.shields.io/github/v/release/HXSecurity/Dongtai-engine?label=Dongtai-engine)](https://github.com/HXSecurity/DongTai-engine/releases)
[![GitHub release](https://img.shields.io/github/v/release/HXSecurity/Dongtai-web?label=Dongtai-web)](https://github.com/HXSecurity/DongTai-web/releases)
[![GitHub release](https://img.shields.io/github/v/release/HXSecurity/DongTai-agent-java?label=DongTai-agent-java)](https://github.com/HXSecurity/DongTai-agent-java/releases)
[![GitHub release](https://img.shields.io/github/v/release/HXSecurity/DongTai-agent-python?label=DongTai-agent-python)](https://github.com/HXSecurity/DongTai-agent-python/releases)



[中文版本(Chinese version)](README-zh.md)

## About DongTai IAST
`DongTai IAST` is an open-source passive interactive security testing (IAST) product. It uses dynamic hooks and taint tracking algorithms to achieve **universal vulnerability detection** and **multiples request associated with vulnerability detection (including but not limited to unauthorized vulnerabilities, overpower vulnerabilities)**, **Third-party component vulnerability detection**, etc. Currently, applications in Java and Python are supported for vulnerability detection.

## Architecture 
`DongTai IAST` has multiple basic services, including `DongTai-web`, `DongTai-webapi`, `DongTai-openapi`, `DongTai-engine`, `agent`, `DongTai-deploy`, ` DongTai-Base-Image` and `DongTai-Plugin-IDEA`:
- `DongTai-web` is the product page of DongTai, which is used to handle the interaction between users and cave states.
- `DongTai-webapi` is responsible for handling user-related operations.
- `DongTai-openapi` is used to process the registration/heartbeat/call method/third-party component/error log data reported by `agent`, issue hook strategy, issue probe control commands, etc.
- `DongTai-engine` analyzes whether there are vulnerabilities in HTTP/HTTPS/RPC requests according to the calling method data and taint tracking algorithm, and is also responsible for other related timing tasks.
- `agent` is a probe module of DongTai, including data collection terminals in different programming languages, used to collect data during application runtime and report to the `DongTai-OpenAPI` service.
- `DongTai-deploy` is used for the deployment of DongTai IAST, including docker-compose single-node deployment, Kubernetes cluster deployment, etc. If you want a deployment plan, you can add features or contribute to the deployment plan.
- `DongTai-Base-Image` contains the basic services that DongTai depends on runtime, including MySql, Redis.
- `DongTai-Plugin-IDEA` is the IDEA plug-in corresponding to the Java probe. You can run the Java probe directly through the plug-in and detect the vulnerabilities directly in IDEA.

## Scenario
The usage scenarios of "DongTai IAST" include but not limited to:

- Embed the `DevSecOps` process to realize automatic detection of application vulnerabilities/third-party component combing/third-party component vulnerability detection.
- Common vulnerability mining for open source software/open source components.
- Security testing before release, etc.

## Quick start
`DongTai IAST` supports **SaaS Service** and **Localized Deployment**. Please refer to [**Deployment Document**](./deploy) for localized deployment.

### 1. SaaS Version
  - Fill out the [Online Form](https://jinshuju.net/f/I9PNmf) to register an account.
  - Log in to the [DongTai IAST] (https://iast.io).
  - Have a quick start with [Online Guideline](https://docs.dongtai.io/docs/category/%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B).

### 2. Localized Deployment Version

`DongTai IAST` supports a variety of deployment schemes which refer to [Deployment Document](./deploy):

- Stand-alone Deployment
  - [x] [Docker-compose](./deploy/docker-compose)
  - [ ] docker - pending upgrade
- Cluster Deployment
  - [x] [Kubernetes](./deploy/kubernetes)

#### Docker-compose
```shell script
$ git clone git@github.com:HXSecurity/DongTai.git
$ cd DongTai
$ chmod u+x build_with_docker_compose.sh
$ ./build_with_docker_compose.sh
```

## Contributing
Contributions are welcomed and greatly appreciated. Further reading — [CONTRIBUTING.md](https://github.com/HXSecurity/DongTai/blob/main/CONTRIBUTING.md) for details on submitting patches and contribution workflow.

Any questions? Let's discuss in [#DongTai discussions](https://github.com/HXSecurity/DongTai/discussions)

## Futher Resources
- [Documentation](https://docs.dongtai.io/)
- [DongTai WebSite](https://dongtai.io)
