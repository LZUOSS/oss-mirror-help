# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Add anaconda / pypi / ubuntu mirrors help page

## [1.0.0] - 2023-02-09

### Added 

- Add alpine / anthon / archlinux / archlinuxcn / centos-altarch / centos / CPAN / CRAN / CTAN / debian / elrepo / epel / fedora / opensuse / openwrt mirrors help page

## [1.1.0] - 2023-02-10

### Added

- Add custom 404 page
- Add coverpage
- Add custom home page
- Add logo and load page
- Add local js/css resouces, but still use cdn
- Add alias for articles in docs, for example, you can use `#/CPAN` to get article to origin `#/docs/CPAN`

### Changed

- Change some contents in navbar
- Change home url in sidebar
- format `index.html`
- Change some meta **description** in `index.html`

### Fixed

- Fixed when loading `#/index.html`, it will alaways be in loading. Use `alias` to fix

## [1.1.1] - 2023-02-12

### Added

- Add docsify tabs

### Fixed

- Fix debian help page render mistake

## [1.2.0] - 2023-02-13

### Added

- Add meta info keyword and author
- Add pagination
- Add footer
- Add hightlight (note/tip/warning/attention/bash/shell)
- Add custom page title

### Changed

- Prettier mirror help pages 

### Deprecated

- deprecate local docsify js/css 

## [1.2.1] - 2023-02-27

### Changed

- Use local res instead of cdn

## opensuse - 2023-02-27

- openSUSE Leap 15.2 or newer help page add command `sudo zypper ref`, thanks to suggestion from [LeBronWen](https://github.com/LeBronWen)

## 2023-03-04

### Changed

- Add Special Thanks

## 2023-10-19

### Changed

- Change lzuoss [website](http://mirror.lzu.edu.cn/lzuoss)

## 2023-12-7

### Changed

- Add AlmaLinux / BlackArch / Debian CD / Debian Security / Flutter / FreeBSD / Gentoo / Gentoo Portage / GNU / Manjaro / Rocky mirror help
- Change debian mirror help to mirrorz
- Add vue.global.prod.js
- Standardize part of the release name
- Set cache-control to 600s

## 2023-12-8

### Changed

- Add debian-ports / deepin-releases / deepin / kernel.org / lfs / openkylin-cdimage / ubuntu-releases / ubuntukylin-cdimage / ubuntukylin mirror help