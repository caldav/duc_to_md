# duc_to_md

A very simple MarkDown exporter for developer.ubuntu.com pages.

## Basic usage

The exporter script takes an url as an argument and outputs a MarkDown version of the `main-content` div.

## Examples

### Single page export

```bash
python3 duc_to_md.py <url> > data/<filename>.md
```

### Batch export

This example shows how to use a list of urls, the `list_phone_pages` file, to create multiple markdown files.

To generate user friendly file names, it uses the `cut` command to strip `http://developer.ubuntu.com/` from the URL and replace any remaining slashes with underscores.

eg. `https://developer.ubuntu.com/en/phone/apps/html-5/` -> `en_phone_apps_html-5_.md`

```bash
for e in `cat list_phone_pages`;do python3 duc_to_md.py $e > "data/"`echo "$e.md" | cut -d "/" -f 4- --output-delimiter="_" -z`;done
```

## TODO

* Handle relative links gracefully
* Handle relative image paths
