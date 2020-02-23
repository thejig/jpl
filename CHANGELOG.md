# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.1] - 2020-02-23
[Author](https://github.com/leonkozlowski)
### Added
- Added base implementation of `jpl`
- This includes a general ruleset for `JiggyPlaybooks`
- CLI for offline usage via `jpl`
- Runtime entrypoint via `JiggyPlaybookLint.validate()`

### Changed
- Initial release

### Removed
- Removed `src` and replaced with `jpl`


## [0.0.2] - 2020-02-23
[Author](https://github.com/leonkozlowski)
### Added
- `__init__.py` for utils

### Changed
- Bump version to `0.0.2`


## [0.0.3] - 2020-02-23
[Author](https://github.com/leonkozlowski)
### Added
- Added newline to end of `__init__.py`

### Changed
- Change CLI param `show` -> `skip`
- Default CLI to show all rules and skip with `-s`
