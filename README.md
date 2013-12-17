SublimeLinter-cppcheck
=========================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter3) provides an interface to [cppcheck](__linter_homepage__). It will be used with files that have the “__syntax__” syntax.

## Installation

### Linter installation
Before installing this plugin, you must ensure that `cppcheck` is installed on your system. To install `cppcheck`, do the following:

1. Install `cppcheck` by typing the following in a terminal:
   ```
   <package manager> install cppcheck
   ```

   or get it from its [homepage](http://cppcheck.sourceforge.net/).

Now you can proceed to install the SublimeLinter-cppcheck plugin.

### Plugin installation
This plugin isn't available in the commonly used [Package Control](https://sublime.wbond.net/installation) and therefore needs to be installed manually from the source.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Settings). For information on generic linter settings, please see [Linter Settings](https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Linter-Settings).

In addition to the standard SublimeLinter settings, SublimeLinter-cppcheck provides its own settings. Those marked as “Inline Setting” or “Inline Override” may also be [used inline](https://github.com/SublimeLinter/SublimeLinter.github.io/wiki/Settings#inline-settings).

|Setting|Description|Inline Setting|Inline Override|
|:------|:----------|:------------:|:-------------:|
|foo|Something.|&#10003;| |
|bar|Something else.| |&#10003;|

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
