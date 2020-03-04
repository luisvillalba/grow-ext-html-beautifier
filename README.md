# grow-ext-html-beautifier

A Grow extension to pretty format HTML.

## Requires

Grow 0.5.1 or higher

## Usage

### Initial setup

1. Create an `extensions.txt` file within your pod.
1. Add to the file: `git+git://github.com/luisvillalba/grow-ext-html-beautifier`
1. Run `grow install`.
1. Add the following section to `podspec.yaml`:

```yaml
ext:
- extensions.html_min.HtmlBeautifierExtension
```

### Options

You can also specify custom parameters in your podspec:
- **tab_size** (*Default 2*):
  Tab size in spaces.
- **trigger** (*Default False*):
  When set to True, only documents containing `html_beautify: True`
  will be beautified. If False, it will beautify all your .html files.
- **strict_validation** (*Default True*):
  When set to True, a strict HTML5 validation will be done on every
  page. If errors are found, it will raise an exception and cancel
  the build.

Example:
```yaml
ext:
- extensions.html_beautifier.HtmlBeautifierExtension:
    options:
      tab_size: 2
      trigger: True
      strict_validation: False
```

## Contributing
Set up a development environment.
```yaml
git clone https://github.com/luisvillalba/grow-ext-html-beautifier.git
cd example/
grow install && grow build
```

