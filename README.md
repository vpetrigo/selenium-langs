[![Chrome Windows](https://github.com/vpetrigo/selenium-langs/actions/workflows/chrome-win.yml/badge.svg)](https://github.com/vpetrigo/selenium-langs/actions/workflows/chrome-win.yml)
[![Chrome Linux](https://github.com/vpetrigo/selenium-langs/actions/workflows/chrome-linux.yml/badge.svg)](https://github.com/vpetrigo/selenium-langs/actions/workflows/chrome-linux.yml)

# Chrome language switch with CLI

Demonstration on how to use Chrome `--lang` CLI switch to set up browser language in Selenium tests
without using of the following code:

```python
options = ChromeOptions()
options = options.add_experimental_option("prefs", {"intl.accept_languages": language_to_use})
```
