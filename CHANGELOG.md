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